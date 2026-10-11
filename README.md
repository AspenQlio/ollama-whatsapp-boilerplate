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

This first milestone defines the local Ollama bridge. A production deployment still needs a Meta WhatsApp Cloud API adapter, webhook signature verification, outbound delivery, persistence, and rate limiting.

## Quality gates

```bash
uv run ruff check .
uv run ruff format --check .
uv run basedpyright
uv run pytest
```
