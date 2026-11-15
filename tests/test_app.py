from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = Path(__file__).resolve().parents[1] / "app.py"


def test_four_tabs_and_small_result():
    app = AppTest.from_file(str(APP), default_timeout=15).run()
    assert not app.exception
    assert len(app.tabs) == 5
    app.selectbox(key="pressure_from").select("Pa")
    app.selectbox(key="pressure_to").select("bar").run()
    assert "1e-05" in app.success[0].value or "0.00001" in app.success[0].value


def test_negative_temperature_and_absolute_zero_error():
    app = AppTest.from_file(str(APP), default_timeout=15).run()
    app.selectbox(key="temperature_from").select("C")
    app.selectbox(key="temperature_to").select("F")
    app.number_input(key="temperature_value").set_value(-40).run()
    assert "-40 C = -40 F" in app.success[-1].value
    app.number_input(key="temperature_value").set_value(-274).run()
    assert not app.exception
    assert "nol mutlak" in app.error[0].value


def test_chat_refusal_without_network():
    app = AppTest.from_file(str(APP), default_timeout=15).run()
    app.chat_input[0].set_value("Buat puisi cinta").run()
    assert not app.exception
    assert "konversi" in app.session_state.messages[-1]["content"]
