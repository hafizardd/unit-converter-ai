import streamlit as st

from ai.client import reply


def show_calculations(calculations):
    for item in calculations:
        st.success(
            f"Hasil fungsi Python: {item['value']:.12g} {item['from_unit']} = "
            f"{item['result']:.12g} {item['to_unit']}"
        )


def chat_tab():
    st.caption("Angka dari tool ditampilkan tersendiri. Periksa juga satuan yang dipilih AI.")
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.chat_requests = 0
    if st.button("Hapus percakapan"):
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            show_calculations(message.get("calculations", []))
    prompt = st.chat_input("Contoh: ubah 1 Pa menjadi bar", max_chars=500)
    if prompt:
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            if st.session_state.chat_requests >= 20:
                response = {
                    "answer": "Batas latihan sesi ini tercapai (20 pertanyaan).",
                    "calculations": [],
                }
            else:
                st.session_state.chat_requests += 1
                with st.spinner("Menyiapkan jawaban..."):
                    response = reply(prompt, st.session_state.messages)
            st.write(response["answer"])
            show_calculations(response["calculations"])
        st.session_state.messages += [
            {"role": "user", "content": prompt},
            {
                "role": "assistant",
                "content": response["answer"],
                "calculations": response["calculations"],
            },
        ]
        st.session_state.messages = st.session_state.messages[-6:]
