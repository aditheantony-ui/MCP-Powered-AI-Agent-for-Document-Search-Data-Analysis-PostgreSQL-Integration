"""Evaluation entry point placeholder."""


def evaluate(predictions: list[str], references: list[str]) -> dict[str, float]:
    """Return exact-match accuracy for a lightweight baseline evaluator."""
    if len(predictions) != len(references):
        raise ValueError("predictions and references must have the same length")
    if not references:
        return {"exact_match": 0.0}
    matches = sum(prediction.strip() == reference.strip() for prediction, reference in zip(predictions, references))
    return {"exact_match": matches / len(references)}
