def fallback_response() -> dict[str, str]:
    return {
        "status": "fallback",
        "category": "unknown",
        "message": (
            "The request could not be confidently classified. "
            "Please provide additional details or route the issue "
            "to the appropriate support team."
        ),
        "source": "fallback",
    }