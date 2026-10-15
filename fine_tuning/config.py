"""Configuration defaults for future fine-tuning jobs."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TrainingConfig:
    base_model: str = "gpt-4o-mini"
    epochs: int = 3
    output_dir: str = "artifacts/model"
