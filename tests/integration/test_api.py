import unittest

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


class TestIssueResolutionAPI(unittest.TestCase):

    def test_health_endpoint(self):
        response = client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "healthy")

    def test_resolve_refund_issue(self):
        response = client.post(
            "/api/v1/resolve",
            json={
                "query": "My refund is still pending",
                "user_role": "support",
            },
        )

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["category"], "refund")
        self.assertEqual(data["status"], "resolved")

    def test_unauthorized_user(self):
        response = client.post(
            "/api/v1/resolve",
            json={
                "query": "My refund is still pending",
                "user_role": "guest",
            },
        )

        self.assertEqual(response.status_code, 403)

    def test_unknown_query_uses_fallback(self):
        response = client.post(
            "/api/v1/resolve",
            json={
                "query": "Something completely unrelated",
                "user_role": "support",
            },
        )

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["status"], "fallback")


if __name__ == "__main__":
    unittest.main()