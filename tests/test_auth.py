import unittest

from logic.auth import SessionState, hash_password, verify_password


class AuthTests(unittest.TestCase):
    def test_password_hash_and_verify(self):
        hashed = hash_password("clave-segura-123")
        self.assertNotEqual(hashed, "clave-segura-123")
        self.assertTrue(verify_password("clave-segura-123", hashed))
        self.assertFalse(verify_password("incorrecta", hashed))

    def test_short_password_rejected(self):
        with self.assertRaises(ValueError):
            hash_password("123")

    def test_session_timeout(self):
        state = SessionState(user_id=1, role_name="Admin")
        self.assertFalse(state.is_expired())


if __name__ == "__main__":
    unittest.main()
