from pathlib import Path

from app.rag.base import Retriever


class LocalRetriever(Retriever):
    """
    Local retrieval implementation used by the public demo.

    The knowledge base contains synthetic examples and is intentionally
    separate from the proprietary enterprise knowledge source used
    during the internship.
    """

    def __init__(self, knowledge_base_path: Path | None = None):
        self.knowledge_base_path = (
            knowledge_base_path
            or Path(__file__).resolve().parents[2]
            / "examples"
            / "knowledge_base.md"
        )

    def load_knowledge_base(self) -> str:
        """Load the local demonstration knowledge base."""

        if not self.knowledge_base_path.exists():
            return ""

        return self.knowledge_base_path.read_text(
            encoding="utf-8"
        )

    def retrieve(self, query: str) -> list[str]:
        """
        Retrieve relevant sections using lightweight keyword matching.

        This is a public demonstration implementation.
        It is not the production retrieval implementation used
        during the internship.
        """

        knowledge = self.load_knowledge_base()

        if not knowledge:
            return []

        query_terms = set(query.lower().split())

        sections = knowledge.split("\n## ")

        matches: list[tuple[int, str]] = []

        for section in sections:
            section_lower = section.lower()

            score = sum(
                1
                for term in query_terms
                if len(term) > 2 and term in section_lower
            )

            if score > 0:
                matches.append((score, section))

        matches.sort(
            key=lambda item: item[0],
            reverse=True
        )

        return [
            section
            for _, section in matches[:3]
        ]