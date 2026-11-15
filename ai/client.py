"""Maksimal dua panggilan API per pertanyaan: tool lalu penjelasan."""

import json

from groq import APIConnectionError, APIStatusError, AuthenticationError, RateLimitError

from ai.config import create_client
from ai.guardrails import check_input
from ai.prompts import system_prompt
from ai.tools import TOOL, execute_tool


def reply(prompt, history):
    rejection = check_input(prompt, history)
    if rejection:
        return {"answer": rejection, "calculations": []}
    calculations = []
    try:
        client, model = create_client()
        # Hanya pesan teks dari UI; payload tool tetap lokal dalam satu giliran.
        messages = [{"role": "system", "content": system_prompt()}]
        messages += [
            {"role": item["role"], "content": item["content"]}
            for item in history[-6:]
            if item.get("role") in {"user", "assistant"} and isinstance(item.get("content"), str)
        ]
        messages.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=[TOOL],
            tool_choice="auto",
            temperature=0.2,
            max_completion_tokens=1024,
        )
        message = response.choices[0].message
        if message.tool_calls:
            if len(message.tool_calls) > 2:
                return {"answer": "Tanyakan maksimal dua konversi sekaligus.", "calculations": []}
            # Kirim hanya field permintaan; respons model bisa berisi metadata lain.
            messages.append(
                {
                    "role": "assistant",
                    "content": message.content,
                    "tool_calls": [
                        {
                            "id": call.id,
                            "type": "function",
                            "function": {
                                "name": call.function.name,
                                "arguments": call.function.arguments,
                            },
                        }
                        for call in message.tool_calls
                    ],
                }
            )
            for call in message.tool_calls:
                result = execute_tool(call.function.name, call.function.arguments)
                if "error" not in result:
                    calculations.append(result)
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": call.id,
                        "content": json.dumps(result, allow_nan=False),
                    }
                )
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                tools=[TOOL],
                tool_choice="none",
                temperature=0.2,
                max_completion_tokens=1024,
            )
            message = response.choices[0].message
        answer = message.content or "Belum ada penjelasan. Gunakan tab konverter untuk hasil angka."
        return {"answer": answer, "calculations": calculations}
    except ValueError:
        answer = "Konfigurasi AI belum siap. Isi GROQ_API_KEY di .env."
    except AuthenticationError:
        answer = "API key tidak diterima. Periksa konfigurasi lokal."
    except RateLimitError:
        answer = "Kuota Groq penuh (429). Tunggu giliran; key satu organisasi berbagi kuota."
    except APIConnectionError:
        answer = "Koneksi ke Groq gagal. Konverter tetap dapat dipakai."
    except APIStatusError:
        answer = "Groq belum dapat menjawab. Periksa akses model dan coba lagi nanti."
    return {"answer": answer, "calculations": calculations}
