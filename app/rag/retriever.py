from app.rag.local_retriever import LocalRetriever


_retriever = LocalRetriever()


def retrieve_context(query: str) -> list[str]:
    """
    Retrieve context using the configured public-demo retriever.

    The service layer depends on this function rather than directly
    depending on the underlying retrieval implementation.
    """

    return _retriever.retrieve(query)