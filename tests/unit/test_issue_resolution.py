import unittest

from app.services.issue_resolution import classify_issue


class TestIssueClassification(unittest.TestCase):

    def test_refund_issue(self):
        result = classify_issue("My refund is still pending")
        self.assertEqual(result, "refund")

    def test_order_issue(self):
        result = classify_issue("Where is my order?")
        self.assertEqual(result, "order")

    def test_access_issue(self):
        result = classify_issue("I cannot access my account")
        self.assertEqual(result, "access")

    def test_unknown_issue(self):
        result = classify_issue("This does not match any category")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()