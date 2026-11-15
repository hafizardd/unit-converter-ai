import pytest

from ai import config


@pytest.fixture(autouse=True)
def empty_environment(monkeypatch):
    monkeypatch.setattr(config, "load_dotenv", lambda *args, **kwargs: None)
    for name in ("GROQ_API_KEY", "GROQ_API_KEYS", "GROQ_KEY_INDEX", "GROQ_MODEL"):
        monkeypatch.delenv(name, raising=False)


def test_select_one_key_without_rotation(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEYS", "test-first,test-second")
    monkeypatch.setenv("GROQ_KEY_INDEX", "1")
    assert config.get_settings() == ("test-second", "openai/gpt-oss-20b")


@pytest.mark.parametrize("index", ["-1", "2", "not-an-index"])
def test_reject_invalid_key_index(monkeypatch, index):
    monkeypatch.setenv("GROQ_API_KEYS", "test-first,test-second")
    monkeypatch.setenv("GROQ_KEY_INDEX", index)
    with pytest.raises(ValueError):
        config.get_settings()


def test_missing_key_is_actionable():
    with pytest.raises(ValueError, match="API key"):
        config.get_settings()
