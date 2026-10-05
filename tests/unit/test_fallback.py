import unittest

from app.services.fallback import fallback_response


class TestFallback(unittest.TestCase):

    def test_fallback_status(self):
        result = fallback_response()

        self.assertEqual(result["status"], "fallback")

    def test_fallback_category(self):
        result = fallback_response()

        self.assertEqual(result["category"], "unknown")

    def test_fallback_source(self):
        result = fallback_response()

        self.assertEqual(result["source"], "fallback")


if __name__ == "__main__":
    unittest.main()