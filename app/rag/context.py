def build_context(documents: list[str]) -> str:
    """Combine retrieved documents into model-ready context."""

    if not documents:
        return ""

    return "\n\n---\n\n".join(documents)