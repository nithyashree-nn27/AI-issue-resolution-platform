import unittest

from app.services.authorization import is_authorized


class TestAuthorization(unittest.TestCase):

    def test_supported_role_is_authorized(self):
        self.assertTrue(is_authorized("support"))

    def test_role_check_is_case_insensitive(self):
        self.assertTrue(is_authorized("SUPPORT"))

    def test_unsupported_role_is_rejected(self):
        self.assertFalse(is_authorized("guest"))

    def test_empty_role_is_rejected(self):
        self.assertFalse(is_authorized(""))


if __name__ == "__main__":
    unittest.main()