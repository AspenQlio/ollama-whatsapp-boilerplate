# Ollama WhatsApp Boilerplate

> A typed FastAPI foundation for connecting normalized messaging webhooks to local LLMs through Ollama.

This project provides a robust development stack to bridge messaging events with local open-source models. It defines a strict API boundary, handles asynchronous LLM requests, and enforces code quality through modern Python tooling.

## Features

- **API Boundaries:** Strict request and response models via Pydantic.
- **Asynchronous Adapter:** Non-blocking Ollama integration using `httpx2`.
- **Dependency Injection:** Modular FastAPI webhook routing.
- **Development Ready:** Included Docker Compose development stack.
- **Strict Quality Gates:** Enforced by Ruff, BasedPyright, and pytest.

## Architecture

The boilerplate implements a FastAPI web service that receives normalized messaging webhooks. These events are processed asynchronously and forwarded to a local Ollama instance. The initial milestone targets local testing; a production deployment will require an authenticated bridge (e.g., Baileys for WhatsApp Web), outbound delivery mechanisms, persistence, and rate limiting.

## Tech Stack

- **Framework:** FastAPI, Pydantic
- **LLM Engine:** Ollama
- **Tooling:** uv, Ruff, BasedPyright, pytest, Docker Compose

## Getting Started

### Prerequisites

- Python 3.11+
- `uv` package manager installed.
- Ollama installed and running locally.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AspenQlio/ollama-whatsapp-boilerplate.git
   cd ollama-whatsapp-boilerplate
   ```
2. **Sync dependencies:**
   ```bash
   uv sync
   ```

## Usage

Start the development server:

```bash
uv run uvicorn ollama_whatsapp.api:app --reload
```

Send a normalized message to test the webhook:

```bash
curl -X POST http://localhost:8000/webhook \
  -H 'content-type: application/json' \
  -d '{"sender":"56912345678","text":"Hola"}'
```

To run the quality gates:

```bash
uv run ruff check .
uv run ruff format --check .
uv run basedpyright
uv run pytest
```

## License

This project is licensed under the MIT License.
