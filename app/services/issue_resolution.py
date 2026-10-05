from app.rag.context import build_context
from app.rag.retriever import retrieve_context
from app.services.fallback import fallback_response


def classify_issue(query: str) -> str | None:
    """
    Representative classification logic.

    The internship solution used AI-powered classification and
    routing. This simplified implementation is provided only
    to demonstrate the public architecture.
    """

    text = query.lower()

    if any(
        word in text
        for word in ["refund", "refund pending", "money back"]
    ):
        return "refund"

    if any(
        word in text
        for word in ["order", "delivery", "shipment", "tracking"]
    ):
        return "order"

    if any(
        word in text
        for word in ["access", "login", "permission"]
    ):
        return "access"

    return None


def resolve_issue(query: str) -> dict[str, str]:
    category = classify_issue(query)

    if category is None:
        return fallback_response()

    documents = retrieve_context(query)

    if not documents:
        return fallback_response()

    context = build_context(documents)

    return {
        "status": "resolved",
        "category": category,
        "message": (
            "Relevant knowledge was retrieved for the request. "
            f"Context length: {len(context)} characters."
        ),
        "source": "sanitized-rag-demo",
    }