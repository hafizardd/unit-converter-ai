"""Uji HTML offline di Chromium/Edge terpasang, tanpa server atau dependency baru.

Jalankan: python scripts/check_learning_browser.py [--browser PATH]
"""

import argparse
import html
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HARNESS = r"""
const report = {errors: [], pages: [], questions: 0, examples: 0, width: innerWidth};
window.addEventListener('error', e => report.errors.push(e.message));
const assert = (condition, message) => { if (!condition) throw Error(message); };
const click = (root, text) => {
  const b = [...root.querySelectorAll('button')].find(x => x.textContent.trim() === text);
  assert(b, 'Missing button: ' + text); b.click();
};
const input = (el, value) => {el.value = value; el.dispatchEvent(new Event('input'));};
addEventListener('DOMContentLoaded', () => {
  try {
    Store.reset();
    for (const id of ['mulai', 'tekanan', 'gaya', 'panjang', 'suhu', 'kuis', 'rumus']) {
      location.hash = id; route();
      const main = document.getElementById('utama');
      assert(main.querySelector('h1'), id + ': missing heading');
      assert(!main.textContent.includes('sedang disusun'), id + ': placeholder');
      assert(!/\b(?:undefined|null|NaN|Infinity)\b/.test(main.textContent), id + ': invalid text');
      assert(document.documentElement.scrollWidth <= innerWidth + 2, id + ': page overflow: ' +
        [...main.querySelectorAll('*')].filter(e => e.getBoundingClientRect().right > innerWidth + 2)
          .slice(0, 8).map(e => e.tagName + '.' + e.className + ':' + Math.round(e.getBoundingClientRect().width)).join(', '));
      for (const svg of main.querySelectorAll('svg')) {
        assert(svg.getAttribute('aria-label') || svg.querySelector('title'), id + ': unlabeled SVG');
      }
      for (const example of main.querySelectorAll('.example')) {
        click(example, 'Tampilkan semua');
        assert(example.querySelectorAll('.steps > li').length === 6, id + ': missing example steps');
        report.examples++;
      }
      const questions = QUIZ[id === 'kuis' ? 'gabungan' : id];
      if (questions) {
        questions.forEach((q, index) => {
          main.querySelectorAll('.dot')[index].click();
          const quiz = main.querySelector('.quiz');
          click(quiz, 'Periksa jawaban');
          assert(!Store.get(q.id), q.id + ': empty answer counted');
          if (q.type === 'mc') {
            main.querySelectorAll('.qcard input[type=radio]')[q.correct].click();
          } else {
            const sol = q.solve();
            input(main.querySelector('.qcard input[type=text]'),
              (q.dp === 'exact' ? String(sol.result) : sol.result.toFixed(q.dp)).replace('.', ','));
          }
          click(quiz, 'Periksa jawaban');
          assert(quiz.querySelector('.fb.ok'), q.id + ': correct answer rejected');
          click(quiz, 'Pembahasan');
          if (q.type === 'num') assert(quiz.querySelectorAll('.steps > li').length === 6, q.id + ': missing solution');
          report.questions++;
        });
      }
      for (const conv of main.querySelectorAll('.conv')) {
        const field = conv.querySelector('input[type=text]');
        input(field, 'abc');
        assert(conv.querySelector('.err-box'), id + ': invalid converter input accepted');
        input(field, '1,5');
        assert(!conv.querySelector('.err-box'), id + ': comma input rejected');
        assert(conv.querySelectorAll('.steps > li').length === 6, id + ': converter steps missing');
        click(conv, 'Tukar satuan');
        assert(!conv.querySelector('.err-box'), id + ': swap failed');
        const advanced = conv.querySelector('input[type=checkbox]');
        advanced.click();
        assert(!conv.querySelector('.err-box'), id + ': advanced toggle failed');
      }
      for (const range of main.querySelectorAll('input[type=range]')) {
        input(range, range.max);
        assert(!main.querySelector('.result.err-box'), id + ': slider failed');
      }
      if (id === 'tekanan') {
        const fields = main.querySelector('[data-key=visual1]').querySelectorAll('input[type=text]');
        input(fields[0], '0'); input(fields[1], '1e-300');
        assert(!main.querySelector('[data-key=visual1] .err-box'), 'small pressure axis failed');
      }
      if (id === 'gaya') {
        const fields = main.querySelector('[data-key=visual0]').querySelectorAll('input[type=text]');
        input(fields[1], '1e-20');
        assert(!main.querySelector('[data-key=visual0] .err-box'), 'small force axis failed');
      }
      if (id === 'suhu') {
        const visual = main.querySelector('[data-key=visual1]');
        const field = visual.querySelector('input[type=text]');
        input(field, '-10');
        assert(visual.textContent.includes('penurunan'), 'negative temperature delta failed');
        const selects = visual.querySelectorAll('select');
        selects[2].value = 'point'; selects[2].dispatchEvent(new Event('change'));
        input(field, '-300');
        assert(visual.querySelector('[role=alert]'), 'below absolute zero accepted');
      }
      report.pages.push(id);
    }
    assert(report.questions === 52, 'Expected 52 questions');
    assert(report.examples >= 16, 'Expected at least 16 examples');
  } catch (e) { report.errors.push(e.message + '\n' + e.stack); }
  parent.postMessage({lessonReport: report}, '*');
});
"""


def find_browser():
    for name in ("chromium", "chromium-browser", "google-chrome", "msedge"):
        if path := shutil.which(name):
            return path
    edge = Path("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
    return str(edge) if edge.exists() else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--browser", default=find_browser())
    args = parser.parse_args()
    if not args.browser:
        parser.error("Browser tidak ditemukan. Gunakan --browser PATH ke Chromium/Edge.")
    source = (ROOT / "belajar/index.html").read_text(encoding="utf-8")
    for width in (360, 768, 1280):
        with tempfile.TemporaryDirectory(prefix="lesson-browser-") as directory:
            folder = Path(directory)
            page = folder / "lesson.html"
            page.write_text(
                source.replace("</body>", "<script>" + HARNESS + "</script></body>"),
                encoding="utf-8",
            )
            # Iframe menjamin lebar 360 meski browser desktop punya minimum window size.
            wrapper = folder / "check.html"
            wrapper.write_text(
                '<meta charset="utf-8"><body style="margin:0">'
                '<pre id="report">pending</pre><script>'
                "addEventListener('message',e=>{if(e.data.lessonReport)"
                "document.getElementById('report').textContent="
                "JSON.stringify(e.data.lessonReport)});</script>"
                f'<iframe src="{page.as_uri()}" style="width:{width}px;height:900px;'
                'border:0"></iframe></body>',
                encoding="utf-8",
            )
            done = subprocess.run(
                [
                    args.browser,
                    "--headless=new",
                    "--disable-gpu",
                    "--allow-file-access-from-files",
                    f"--user-data-dir={folder / 'profile'}",
                    "--virtual-time-budget=5000",
                    "--dump-dom",
                    wrapper.as_uri(),
                ],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=45,
                check=True,
            )
            match = re.search(r'<pre id="report">(.*?)</pre>', done.stdout, re.S)
            if not match or match[1] == "pending":
                raise RuntimeError("Browser tidak menghasilkan laporan: " + done.stderr[-1000:])
            report = json.loads(html.unescape(match[1]))
            print(json.dumps(report, ensure_ascii=False))
            if report["errors"] or report["width"] != width:
                raise RuntimeError(f"Pemeriksaan browser gagal pada lebar {width}")


if __name__ == "__main__":
    main()
