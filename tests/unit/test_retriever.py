import unittest

from app.rag.retriever import retrieve_context


class TestRetriever(unittest.TestCase):

    def test_refund_query_retrieves_context(self):
        results = retrieve_context(
            "My refund is still pending"
        )

        self.assertGreater(len(results), 0)

    def test_order_query_retrieves_context(self):
        results = retrieve_context(
            "Where is my order delivery?"
        )

        self.assertGreater(len(results), 0)

    def test_unrelated_query_returns_no_context(self):
        results = retrieve_context(
            "Tell me something completely unrelated"
        )

        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()