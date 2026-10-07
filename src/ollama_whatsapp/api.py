"""FastAPI application exposing the normalized webhook."""

from typing import Annotated

from fastapi import Depends, FastAPI

from ollama_whatsapp.models import IncomingMessage, OutgoingMessage
from ollama_whatsapp.service import ChatModel, OllamaClient, WebhookService
from ollama_whatsapp.settings import Settings

app = FastAPI(title="Ollama WhatsApp Boilerplate", version="0.1.0")


def get_chat_model() -> ChatModel:
    """Build the configured Ollama adapter for one request."""
    settings = Settings()
    return OllamaClient(
        host=settings.ollama_host,
        model=settings.ollama_model,
        timeout_seconds=settings.request_timeout_seconds,
    )


ChatModelDependency = Annotated[ChatModel, Depends(get_chat_model)]


@app.get("/health")
async def health() -> dict[str, str]:
    """Report that the HTTP process is accepting requests."""
    return {"status": "ok"}


@app.post("/webhook")
async def webhook(
    message: IncomingMessage,
    model: ChatModelDependency,
) -> OutgoingMessage:
    """Generate a reply for one normalized inbound message."""
    return await WebhookService(model=model).reply_to(message)
