"""Simple workflow coordinating local context and an optional LLM."""

from pathlib import Path

from agent.llm_client import LLMClient
from document_processing.loader import load_document


def answer_from_document(document_path: str | Path, question: str, client: LLMClient | None = None) -> str:
    """Build a grounded prompt from a document and ask the configured model."""
    context = load_document(Path(document_path))
    prompt = f"Use only this document to answer the question.\n\nDocument:\n{context}\n\nQuestion: {question}"
    return (client or LLMClient()).complete(prompt)
