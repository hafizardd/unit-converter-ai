import pytest

from ai import config


@pytest.fixture(autouse=True)
def empty_environment(monkeypatch):
    monkeypatch.setattr(config, "load_dotenv", lambda *args, **kwargs: None)
    for name in ("GROQ_API_KEY", "GROQ_API_KEYS", "GROQ_KEY_INDEX", "GROQ_MODEL"):
        monkeypatch.delenv(name, raising=False)


def test_read_single_key_and_default_model(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "  test-personal  ")
    assert config.get_settings() == ("test-personal", "openai/gpt-oss-20b")


def test_workshop_settings_do_not_override_single_key(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "test-personal")
    monkeypatch.setenv("GROQ_API_KEYS", "test-first,test-second")
    monkeypatch.setenv("GROQ_KEY_INDEX", "not-used")
    assert config.get_settings()[0] == "test-personal"


def test_workshop_list_alone_does_not_supply_personal_key(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEYS", "test-first,test-second")
    with pytest.raises(ValueError, match="API key"):
        config.get_settings()


@pytest.mark.parametrize("key", ["", "   ", "YOUR_GROQ_API_KEY"])
def test_reject_empty_or_placeholder_key(monkeypatch, key):
    monkeypatch.setenv("GROQ_API_KEY", key)
    with pytest.raises(ValueError, match="API key"):
        config.get_settings()


def test_model_can_be_configured(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "test-personal")
    monkeypatch.setenv("GROQ_MODEL", "test-model")
    assert config.get_settings() == ("test-personal", "test-model")


def test_missing_key_is_actionable():
    with pytest.raises(ValueError, match="API key"):
        config.get_settings()
