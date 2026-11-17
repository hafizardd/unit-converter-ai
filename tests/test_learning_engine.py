"""Mesin hitung belajar/index.html dibandingkan dengan konverter Python."""

import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

from converters import convert_unit
from converters import force as force_mod
from converters import length as length_mod
from converters import pressure as pressure_mod
from converters import temperature as temperature_mod

HTML = Path(__file__).resolve().parents[1] / "belajar" / "index.html"
NODE = shutil.which("node")

DRIVER = r"""
const fs = require('fs');
const html = fs.readFileSync(process.argv[1], 'utf8');
const core = /<script id="core">([\s\S]*?)<\/script>/.exec(html)[1];
const mod = { exports: {} };
new Function('module', core)(mod);
const C = mod.exports;
const cases = JSON.parse(fs.readFileSync(0, 'utf8'));
const run = (c) => {
  switch (c.op) {
    case 'linear': return C.convertLinear(c.cat, c.value, c.from, c.to);
    case 'linsteps': return C.convertSteps(c.cat, c.value, c.from, c.to).result;
    case 'temp': return C.convertTemperature(c.value, c.from, c.to);
    case 'tempsteps': return C.temperatureSteps(c.value, c.from, c.to).result;
    case 'delta': return C.convertDelta(c.value, c.from, c.to);
    case 'deltasteps': return C.deltaSteps(c.value, c.from, c.to).result;
    case 'delta_details': return C.deltaSteps(c.value, c.from, c.to);
    case 'power': return C.powerSteps(c.value, c.from, c.to, c.power).result;
    case 'feetinches': return C.feetInchesSteps(c.feet, c.inches).result;
    case 'gauge': return C.gaugeToAbsolute(c.gauge, c.gu, c.atm, c.au, c.out).result;
    case 'pf': return C.pressureFromForce(c.F, c.A).result;
    case 'newton': return C.newtonSteps(c.m, c.a).result;
    case 'accel': return C.accelerationSteps(c.F, c.m).result;
    case 'weight': return C.weightSteps(c.m, c.g).result;
    case 'parse': return C.parseNumber(c.text);
    case 'fmt': return C.fmt(c.value, c.digits);
    case 'check': return C.checkNumeric(c.user, c.expected, c.dp).ok;
    default: throw new Error('op tidak dikenal ' + c.op);
  }
};
const out = cases.map((c) => {
  try { return { value: run(c) }; } catch (e) { return { error: e.message }; }
});
process.stdout.write(JSON.stringify(out));
"""


@pytest.fixture(autouse=True)
def require_node():
    assert NODE, "Node.js diperlukan untuk memverifikasi mesin hitung HTML."


def run_js(cases):
    done = subprocess.run(
        [NODE, "-e", DRIVER, str(HTML)],
        input=json.dumps(cases),
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return json.loads(done.stdout)


LINEAR_CATEGORIES = {
    "pressure": pressure_mod.UNITS,
    "force": force_mod.UNITS,
    "length": length_mod.UNITS,
}
LINEAR_VALUES = [0, 1, -1.5, 3.14159, 250, 1e-6, 1e6, 123456.789]
TEMPERATURE_VALUES = [-300, -273.15, -100, -40, 0, 25, 37, 98.6, 100, 212, 300, 1e6]


def linear_cases(op):
    return [
        {"op": op, "cat": cat, "value": v, "from": a, "to": b}
        for cat, units in LINEAR_CATEGORIES.items()
        for a in units
        for b in units
        for v in LINEAR_VALUES
    ]


@pytest.mark.parametrize("op", ["linear", "linsteps"])
def test_linear_pairs_match_python(op):
    cases = linear_cases(op)
    for case, got in zip(cases, run_js(cases), strict=True):
        expected = convert_unit(case["cat"], case["value"], case["from"], case["to"])["result"]
        assert got["value"] == pytest.approx(expected, rel=1e-12, abs=0), case


@pytest.mark.parametrize("op", ["temp", "tempsteps"])
def test_temperature_pairs_match_python(op):
    cases = [
        {"op": op, "value": v, "from": a, "to": b}
        for a in temperature_mod.UNITS
        for b in temperature_mod.UNITS
        for v in TEMPERATURE_VALUES
    ]
    for case, got in zip(cases, run_js(cases), strict=True):
        try:
            expected = convert_unit("temperature", case["value"], case["from"], case["to"])
        except ValueError:
            assert "error" in got, case
            continue
        assert "value" in got, case
        assert got["value"] == pytest.approx(expected["result"], rel=1e-12, abs=1e-9), case


def test_unknown_units_rejected():
    cases = [
        {"op": "linear", "cat": "force", "value": 1, "from": "kg", "to": "N"},
        {"op": "temp", "value": 1, "from": "X", "to": "C"},
        {"op": "linear", "cat": "pressure", "value": 1e308, "from": "MPa", "to": "Pa"},
    ]
    assert all("error" in item for item in run_js(cases))


ACCEPTANCE = [
    ({"op": "pf", "F": 500, "A": 0.25}, 2000),
    ({"op": "linear", "cat": "pressure", "value": 250, "from": "kPa", "to": "bar"}, 2.5),
    ({"op": "linear", "cat": "pressure", "value": 1, "from": "atm", "to": "bar"}, 1.01325),
    (
        {"op": "gauge", "gauge": 32, "gu": "psi", "atm": 1, "au": "atm", "out": "bar"},
        3.2195723338,
    ),
    ({"op": "newton", "m": 2, "a": 3}, 6),
    ({"op": "linear", "cat": "force", "value": 1, "from": "kgf", "to": "N"}, 9.80665),
    ({"op": "linear", "cat": "force", "value": 500, "from": "lbf", "to": "kN"}, 2.2241108076),
    ({"op": "linear", "cat": "length", "value": 5, "from": "ft", "to": "cm"}, 152.4),
    ({"op": "linear", "cat": "length", "value": 100, "from": "mi", "to": "km"}, 160.9344),
    ({"op": "feetinches", "feet": 5, "inches": 10}, 177.8),
    ({"op": "power", "value": 2, "from": "m", "to": "cm", "power": 2}, 20000),
    ({"op": "power", "value": 1, "from": "m", "to": "cm", "power": 3}, 1000000),
    ({"op": "temp", "value": 25, "from": "C", "to": "F"}, 77),
    ({"op": "temp", "value": 98.6, "from": "F", "to": "C"}, 37),
    ({"op": "temp", "value": 300, "from": "K", "to": "F"}, 80.33),
    ({"op": "temp", "value": -40, "from": "C", "to": "F"}, -40),
    ({"op": "temp", "value": 0, "from": "K", "to": "F"}, -459.67),
    ({"op": "delta", "value": 10, "from": "C", "to": "F"}, 18),
    ({"op": "delta", "value": -10, "from": "C", "to": "F"}, -18),
    ({"op": "delta", "value": 18, "from": "F", "to": "K"}, 10),
    ({"op": "weight", "m": 70, "g": 9.80665}, 686.4655),
    ({"op": "accel", "F": 12, "m": 4}, 3),
    ({"op": "deltasteps", "value": 10, "from": "C", "to": "F"}, 18),
]


def test_acceptance_values_from_plan():
    results = run_js([case for case, _ in ACCEPTANCE])
    for (case, expected), got in zip(ACCEPTANCE, results, strict=True):
        assert got["value"] == pytest.approx(expected, rel=1e-9, abs=1e-9), case


def test_below_absolute_zero_rejected():
    cases = [
        {"op": "temp", "value": -300, "from": "C", "to": "K"},
        {"op": "tempsteps", "value": -1, "from": "K", "to": "C"},
        {"op": "gauge", "gauge": -2, "gu": "bar", "atm": 1, "au": "atm", "out": "kPa"},
    ]
    assert all("error" in item for item in run_js(cases))


def test_invalid_physics_inputs_rejected():
    cases = [
        {"op": "pf", "F": 10, "A": 0},
        {"op": "pf", "F": 10, "A": -1},
        {"op": "newton", "m": 0, "a": 3},
        {"op": "accel", "F": 5, "m": 0},
        {"op": "weight", "m": 5, "g": 0},
    ]
    assert all("error" in item for item in run_js(cases))


def test_negative_gauge_above_vacuum_is_valid():
    got = run_js([{"op": "gauge", "gauge": -0.5, "gu": "atm", "atm": 1, "au": "atm", "out": "atm"}])
    assert got[0]["value"] == pytest.approx(0.5)


@pytest.mark.parametrize(
    "text,expected",
    [
        ("1,5", 1.5),
        ("1.5", 1.5),
        ("0,001", 0.001),
        ("-3,25", -3.25),
        ("3,307", 3.307),
        ("1e3", 1000),
        (" 12 ", 12),
    ],
)
def test_parse_accepts_decimal_comma_and_point(text, expected):
    assert run_js([{"op": "parse", "text": text}])[0]["value"]["value"] == expected


@pytest.mark.parametrize(
    "text", ["", "   ", "abc", "1 000", "1.000,5", "1,000,5", "1.000", "1e999"]
)
def test_parse_rejects_empty_ambiguous_and_invalid(text):
    got = run_js([{"op": "parse", "text": text}])[0]["value"]
    assert got["ok"] is False
    assert got["error"]


@pytest.mark.parametrize(
    "value,expected",
    [(1013.25, "1.013,25"), (101325, "101.325"), (0.3048, "0,3048"), (-40, "−40"), (1e-5, "10⁻⁵")],
)
def test_format_uses_indonesian_separators(value, expected):
    assert run_js([{"op": "fmt", "value": value}])[0]["value"] == expected


def test_page_has_no_network_dependencies():
    html = HTML.read_text(encoding="utf-8")
    assert not re.search(r"""(?:src|href)\s*=\s*["']https?:""", html)
    assert not re.search(r"@import|fetch\(|XMLHttpRequest|WebSocket|sendBeacon", html)


def test_delta_explanation_uses_the_selected_units():
    solution = run_js([{"op": "delta_details", "value": -18, "from": "F", "to": "K"}])[0]["value"]
    assert solution["result"] == pytest.approx(-10)
    explanation = " ".join(solution["steps"][-1]["lines"])
    assert "°F dan K" in explanation
    assert "penurunan tetap penurunan" in explanation
    assert "titik 18 °C" not in explanation


def test_quiz_records_revealed_answers_as_assisted():
    driver = r"""
const fs = require('fs');
const html = fs.readFileSync(process.argv[1], 'utf8');
const storeCode = html.slice(html.indexOf('const Store = (function'),
    html.indexOf('/* ---------- Kuis satu per satu'));
const memory = {};
const window = {localStorage: {getItem: k => memory[k] || null,
    setItem: (k, v) => { memory[k] = v; }}};
const S = new Function('window', storeCode + ';return Store;')(window);
S.markRevealed('revealed');
S.recordCheck('revealed', true);
S.recordCheck('direct', true);
S.recordCheck('retry', false);
S.recordCheck('retry', true);
S.markHint('hinted');
S.recordCheck('hinted', true);
S.markLesson('suhu');
const result = {revealed: S.get('revealed'), direct: S.get('direct'),
    retry: S.get('retry'), hinted: S.get('hinted'), lesson: S.lessonDone('suhu')};
S.reset(); result.reset = S.get('direct') === null && !S.lessonDone('suhu');
const blocked = {get localStorage() {throw Error('storage disabled');}};
const B = new Function('window', storeCode + ';return Store;')(blocked);
B.recordCheck('offline', true);
result.fallback = !B.persistent() && B.get('offline').solved;
console.log(JSON.stringify(result));
"""
    done = subprocess.run(
        [NODE, "-e", driver, str(HTML)], capture_output=True, text=True, check=True
    )
    got = json.loads(done.stdout)
    assert got["revealed"]["assisted"] is True
    assert got["direct"]["assisted"] is False
    assert got["retry"]["first"] == "salah"
    assert got["retry"]["solved"] is True
    assert got["hinted"]["assisted"] is True
    assert got["lesson"] is True
    assert got["reset"] is True
    assert got["fallback"] is True


def test_answer_rounding_matches_the_requested_precision():
    cases = [
        ({"user": 4.137, "expected": 4.136854, "dp": 3}, True),
        ({"user": 4.136854, "expected": 4.136854, "dp": 3}, True),
        ({"user": 4.1364, "expected": 4.136854, "dp": 3}, False),
        ({"user": 2.50001, "expected": 2.5, "dp": "exact"}, False),
    ]
    results = run_js([{"op": "check", **case} for case, _ in cases])
    assert [got["value"] for got in results] == [expected for _, expected in cases]


def test_quiz_bank_has_independently_checked_answers():
    driver = r"""
const fs = require('fs');
const html = fs.readFileSync(process.argv[1], 'utf8');
const scripts = [...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].map(x => x[1]);
scripts.forEach(x => new Function(x));
const Q = new Function(scripts[0] + scripts[1] + ';return QUIZ;')();
console.log(JSON.stringify(Object.fromEntries(Object.entries(Q).map(([topic, qs]) =>
    [topic, qs.map(q => ({id:q.id, value:q.type === 'num' ? q.solve().result : q.correct,
        steps:q.type === 'num' ? q.solve().steps.length : null}))]))));
"""
    done = subprocess.run(
        [NODE, "-e", driver, str(HTML)], capture_output=True, text=True, check=True
    )
    bank = json.loads(done.stdout)
    # Posisi pilihan konsep diperiksa terhadap pernyataan fisika pada setiap soal.
    # Nilai numerik berikut adalah acuan terpisah dari closure solve() HTML.
    expected = {
        "tekanan": [0, 0, 0, 2000, 2.5, 4.1368543759008, 303.975, 1, 2, 3.21957233381376],
        "gaya": [0, 1, 0, 6, 49.03325, 203.94324259558564, 2.22411080763025, 1, 0, 113.4 / 9.80665],
        "panjang": [0, 1, 0, 2.5, 152.4, 160.9344, 1.968503937007874, 20000, 1, 177.8],
        "suhu": [0, 1, 1, 77, 37, 273.15, -459.67, 18, 2, 80.33],
    }
    ids = []
    for topic, values in expected.items():
        assert len(bank[topic]) == 10
        for question, value in zip(bank[topic], values, strict=True):
            assert question["value"] == pytest.approx(value), question["id"]
            if question["steps"] is not None:
                assert question["steps"] == 6
            ids.append(question["id"])
    assert len(bank["gabungan"]) == 12
    for topic in expected:
        for index in (0, 5, 9):
            question = next(q for q in bank["gabungan"] if q["id"] == f"gabungan-{topic}-{index}")
            assert question["value"] == pytest.approx(expected[topic][index])
            ids.append(question["id"])
    assert len(ids) == len(set(ids)) == 52
