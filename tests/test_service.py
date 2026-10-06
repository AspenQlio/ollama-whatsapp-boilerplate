from dataclasses import dataclass
from typing import override

import pytest

from ollama_whatsapp.models import IncomingMessage
from ollama_whatsapp.service import ChatModel, WebhookService


@dataclass(frozen=True, slots=True)
class FakeChatModel(ChatModel):
    reply: str

    @override
    async def generate(self, prompt: str) -> str:
        del prompt
        return self.reply


@pytest.mark.anyio
async def test_service_returns_model_reply() -> None:
    # Given
    service = WebhookService(model=FakeChatModel(reply="Hola desde Ollama"))
    message = IncomingMessage(sender="56912345678", text="Hola")

    # When
    reply = await service.reply_to(message)

    # Then
    assert reply.recipient == "56912345678"
    assert reply.text == "Hola desde Ollama"
