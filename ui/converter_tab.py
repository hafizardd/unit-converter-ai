import streamlit as st

from converters import CATEGORIES, convert_unit


def converter_tab(category):
    data = CATEGORIES[category]
    units = data["units"]
    value = st.number_input("Nilai", value=1.0, format="%.8g", key=f"{category}_value")
    left, right = st.columns(2)
    with left:
        from_unit = st.selectbox("Dari", units, key=f"{category}_from")
    with right:
        to_unit = st.selectbox("Ke", units, index=1, key=f"{category}_to")
    try:
        conversion = convert_unit(category, value, from_unit, to_unit)
        st.success(f"{value:.12g} {from_unit} = {conversion['result']:.12g} {to_unit}")
        with st.expander("Bandingkan dengan satuan lain"):
            st.table(
                [
                    {"Satuan": unit, "Nilai": f"{data['convert'](value, from_unit, unit):.12g}"}
                    for unit in units
                ]
            )
    except ValueError as error:
        st.error(str(error))
    if category == "force":
        st.caption("kgf adalah satuan gaya; kg adalah satuan massa.")
    if category == "temperature":
        st.caption("C: Celsius · F: Fahrenheit · K: Kelvin · R: Rankine")
