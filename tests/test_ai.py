import json
from types import SimpleNamespace

import httpx
import pytest
from groq import RateLimitError
from groq.types.chat import ChatCompletionMessage

from ai import client
from ai.tools import execute_tool


def completion(message):
    return SimpleNamespace(choices=[SimpleNamespace(message=message)])


def test_tool_arguments_are_validated():
    valid = json.dumps({"category": "pressure", "value": 1, "from_unit": "Pa", "to_unit": "bar"})
    assert execute_tool("convert_unit", valid)["result"] == pytest.approx(0.00001)
    for name, arguments in [
        ("run_python", valid),
        ("convert_unit", "not-json"),
        ("convert_unit", "[]"),
        ("convert_unit", '{"category": "pressure"}'),
        ("convert_unit", valid.replace('"Pa"', '"kg"')),
        ("convert_unit", valid.replace('"pressure"', "[]")),
        ("convert_unit", valid.replace('"value": 1', '"value": NaN')),
    ]:
        assert "error" in execute_tool(name, arguments)


def test_model_calls_python_then_receives_tool_result(monkeypatch):
    first = ChatCompletionMessage(
        role="assistant",
        content=None,
        tool_calls=[
            {
                "id": "call-1",
                "type": "function",
                "function": {
                    "name": "convert_unit",
                    "arguments": json.dumps(
                        {
                            "category": "pressure",
                            "value": 1,
                            "from_unit": "Pa",
                            "to_unit": "bar",
                        }
                    ),
                },
            }
        ],
    )
    responses = iter(
        [
            completion(first),
            completion(ChatCompletionMessage(role="assistant", content="Bagilah dengan 100000.")),
        ]
    )
    calls = []

    def create(**kwargs):
        calls.append({**kwargs, "messages": list(kwargs["messages"])})
        return next(responses)

    fake = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))
    monkeypatch.setattr(client, "create_client", lambda: (fake, "test-model"))
    response = client.reply("Ubah 1 Pa menjadi bar", [])
    assert response["calculations"][0]["result"] == pytest.approx(0.00001)
    assert response["answer"] == "Bagilah dengan 100000."
    assert len(calls) == 2
    assert calls[1]["tool_choice"] == "none"
    tool_message = calls[1]["messages"][-1]
    assert tool_message["tool_call_id"] == "call-1"
    assert json.loads(tool_message["content"])["result"] == pytest.approx(0.00001)


def test_refusal_never_creates_client(monkeypatch):
    def fail():
        raise AssertionError("API client should not be created")

    monkeypatch.setattr(client, "create_client", fail)
    assert "konversi" in client.reply("Buat puisi cinta", [])["answer"]


def test_rate_limit_is_reported_without_retry(monkeypatch):
    calls = []

    def create(**kwargs):
        calls.append(kwargs)
        request = httpx.Request("POST", "https://example.invalid")
        response = httpx.Response(429, request=request)
        raise RateLimitError("rate limit", response=response, body=None)

    fake = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))
    monkeypatch.setattr(client, "create_client", lambda: (fake, "test-model"))
    result = client.reply("Jelaskan Pa", [])
    assert "429" in result["answer"]
    assert len(calls) == 1
