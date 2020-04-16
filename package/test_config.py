import unittest
from config import create_api


class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.api = create_api()

    def test_create_api(self):
        self.assertIsNotNone(self.api)


if __name__ == '__main__':
    unittest.main()
