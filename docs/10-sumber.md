# 10. Sumber resmi dan catatan riset

Diperiksa 15 November 2026. Layanan dapat berubah; dashboard akun mengalahkan
asumsi kuota dalam materi. Tidak ada jaminan gratis tanpa batas.

- [Groq: rate limits](https://console.groq.com/docs/rate-limits): batas di tingkat
  organisasi; request dan token sama-sama dapat menjadi pembatas. Periksa limit akun.
- [Groq: deprecations](https://console.groq.com/docs/deprecations): Llama 8B dan 70B
  dihentikan bagi free/developer tier pada 16 Agustus 2026; pengganti 8B adalah GPT OSS 20B.
- [Groq: models](https://console.groq.com/docs/models) dan
  [GPT OSS 20B](https://console.groq.com/docs/model/openai/gpt-oss-20b): ketersediaan dan kemampuan model.
- [Groq: tool use](https://console.groq.com/docs/tool-use/overview): aplikasi menerima
  permintaan tool, mengeksekusi fungsi, lalu mengirim hasil kembali ke model.
- [Streamlit: chat_input](https://docs.streamlit.io/develop/api-reference/chat/st.chat_input): input chat.
- [Streamlit: AppTest](https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest):
  simulasi aplikasi untuk menguji widget dan hasil tanpa browser.
- [Streamlit: secrets](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management):
  pengaturan key saat deployment, terpisah dari repository.
- [NIST SP 811](https://www.nist.gov/pml/special-publication-811): rujukan satuan dan faktor konversi.

Versi dependency runtime dipatok dalam requirements untuk reproduksibilitas kelas.
Pin ini bukan klaim bahwa semua versi di masa depan kompatibel. API nyata harus
diuji menjelang acara menggunakan key dan model yang memang tersedia.
