"""Validated API boundary models."""

from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field


class IncomingMessage(BaseModel):
    """Normalized inbound text message."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    sender: str = Field(min_length=1, max_length=64)
    text: str = Field(min_length=1, max_length=8_000)


class OutgoingMessage(BaseModel):
    """Normalized outbound text message."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    recipient: str
    text: str


class OllamaRequest(BaseModel):
    """Request accepted by Ollama's generate endpoint."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    model: str
    prompt: str
    stream: bool = False


class OllamaResponse(BaseModel):
    """Subset of Ollama's response consumed by the bridge."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True)

    response: str
