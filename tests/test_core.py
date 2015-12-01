import unittest
from core import split_entry


class KeepassTestCase(unittest.TestCase):
    def test_entry_split(self):
        password, salt, length = split_entry('password:salt')
        self.assertEqual('password', password)
        self.assertEqual('salt', salt)
        self.assertEqual(10, length)

    def test_entry_split_with_length(self):
        password, salt, length = split_entry('password:salt:15')
        self.assertEqual('password', password)
        self.assertEqual('salt', salt)
        self.assertEqual(15, length)


if __name__ == '__main__':
    unittest.main()
