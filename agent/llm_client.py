"""Optional OpenAI-compatible LLM client."""

import os
from typing import Any


class LLMClient:
    """Thin adapter that keeps the base project usable without an API key."""

    def __init__(self, model: str | None = None) -> None:
        self.model = model or os.getenv("LLM_MODEL", "gpt-4o-mini")

    def available(self) -> bool:
        return bool(os.getenv("OPENAI_API_KEY"))

    def complete(self, prompt: str) -> str:
        """Generate a completion when the optional OpenAI package is configured."""
        if not self.available():
            raise RuntimeError("OPENAI_API_KEY is not configured")
        try:
            from openai import OpenAI
        except ImportError as error:
            raise RuntimeError("Install the optional 'openai' dependency") from error
        response: Any = OpenAI().chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content or ""
