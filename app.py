import streamlit as st

from converters import CATEGORIES
from ui.chat_tab import chat_tab
from ui.converter_tab import converter_tab

st.set_page_config(page_title="Unit Converter + AI", page_icon="🔄", layout="centered")
st.title("Unit Converter + AI")
st.caption("Materi lanjutan workshop Python · Streamlit · Groq")
tabs = st.tabs([data["label"] for data in CATEGORIES.values()] + ["Asisten AI"])
for tab, category in zip(tabs, CATEGORIES):
    with tab:
        converter_tab(category)
with tabs[-1]:
    chat_tab()
