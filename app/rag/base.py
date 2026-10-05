from abc import ABC, abstractmethod


class Retriever(ABC):
    """
    Abstract interface for retrieving knowledge relevant to a query.

    Different retrieval implementations can be plugged into the
    issue-resolution workflow without changing the API layer.
    """

    @abstractmethod
    def retrieve(self, query: str) -> list[str]:
        """
        Retrieve relevant knowledge for the given query.
        """
        raise NotImplementedError