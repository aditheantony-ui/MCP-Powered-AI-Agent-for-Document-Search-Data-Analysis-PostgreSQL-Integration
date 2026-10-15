"""Fine-tuning entry point placeholder."""

from fine_tuning.config import TrainingConfig


def train(config: TrainingConfig | None = None) -> None:
    """Validate configuration before connecting a training backend."""
    selected = config or TrainingConfig()
    if selected.epochs < 1:
        raise ValueError("epochs must be at least 1")
    print(f"Training configuration ready for {selected.base_model}")


if __name__ == "__main__":
    train()
