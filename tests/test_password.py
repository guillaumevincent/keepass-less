import unittest

from password import make_password


class PasswordTestCase(unittest.TestCase):
    def test_password_hash(self):
        self.assertEqual('MjE5Y2I1OG', make_password("password", "facebook"))

    def test_password_length_equal_10(self):
        self.assertEqual(10, len(make_password("password", "facebook")))

    def test_password_length_can_change(self):
        self.assertEqual(4, len(make_password("password", "facebook", 4)))


if __name__ == '__main__':
    unittest.main()
