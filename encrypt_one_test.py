import unittest

import encrypt_one


class TestHashing(unittest.TestCase):
    def test_hashing(self):
        self.assertTrue(encrypt_one.check_token(
            "kosgei", encrypt_one.hash_token('kosgei')))


if __name__ == '__main__':
    unittest.main()
