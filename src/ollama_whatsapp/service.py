"""Application service and Ollama adapter."""

from dataclasses import dataclass
from typing import Protocol

import httpx2

from ollama_whatsapp.models import (
    IncomingMessage,
    OllamaRequest,
    OllamaResponse,
    OutgoingMessage,
)


class ChatModel(Protocol):
    """Capability required from a text-generation backend."""

    async def generate(self, prompt: str) -> str:
        """Generates one response for the supplied prompt."""
        ...


@dataclass(frozen=True, slots=True)
class OllamaClient:
    """HTTP adapter for Ollama's non-streaming generation endpoint."""

    host: str
    model: str
    timeout_seconds: float

    async def generate(self, prompt: str) -> str:
        """Requests one non-streaming response from Ollama."""
        request = OllamaRequest(model=self.model, prompt=prompt)
        async with httpx2.AsyncClient(
            base_url=self.host,
            timeout=self.timeout_seconds,
        ) as client:
            response = await client.post("/api/generate", json=request.model_dump())
            _ = response.raise_for_status()
        return OllamaResponse.model_validate_json(response.content).response


@dataclass(frozen=True, slots=True)
class WebhookService:
    """Turns normalized incoming messages into normalized replies."""

    model: ChatModel

    async def reply_to(self, message: IncomingMessage) -> OutgoingMessage:
        """Preserves the sender as the reply recipient."""
        text = await self.model.generate(message.text)
        return OutgoingMessage(recipient=message.sender, text=text)
