from dataclasses import dataclass
from typing import override

from fastapi.testclient import TestClient

from ollama_whatsapp.api import app, get_chat_model
from ollama_whatsapp.service import ChatModel


@dataclass(frozen=True, slots=True)
class FakeChatModel(ChatModel):
    @override
    async def generate(self, prompt: str) -> str:
        return f"Eco: {prompt}"


def test_webhook_returns_typed_reply() -> None:
    # Given
    app.dependency_overrides[get_chat_model] = FakeChatModel
    client = TestClient(app)

    # When
    response = client.post("/webhook", json={"sender": "56912345678", "text": "Hola"})

    # Then
    assert response.status_code == 200
    assert response.json() == {"recipient": "56912345678", "text": "Eco: Hola"}
    app.dependency_overrides.clear()
