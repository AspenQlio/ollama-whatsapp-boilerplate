"""Runtime configuration parsed from environment variables."""

from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Immutable Ollama connection settings."""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(env_prefix="", frozen=True)

    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "qwen3:8b"
    request_timeout_seconds: float = 30.0
