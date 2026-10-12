# Ollama WhatsApp Boilerplate

A typed FastAPI foundation for connecting normalized messaging webhooks to local models through Ollama.

## Features

- Pydantic request and response boundaries.
- Async Ollama adapter using `httpx2`.
- Dependency-injected FastAPI webhook.
- Docker Compose development stack.
- Strict Ruff, BasedPyright, and pytest gates.

## Quickstart

```bash
uv sync
uv run uvicorn ollama_whatsapp.api:app --reload
```

Send a normalized message:

```bash
curl -X POST http://localhost:8000/webhook \
  -H 'content-type: application/json' \
  -d '{"sender":"56912345678","text":"Hola"}'
```

## Scope

This first milestone defines the local Ollama bridge. The planned messaging adapter uses a self-hosted WhatsApp Web bridge such as Baileys, not Meta WhatsApp Cloud API. A production deployment still needs authenticated bridge requests, outbound delivery, persistence, reconnection handling, and rate limiting.

## Quality gates

```bash
uv run ruff check .
uv run ruff format --check .
uv run basedpyright
uv run pytest
```
