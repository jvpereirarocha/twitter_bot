import unittest
from config import create_api
from follow import Follow


class FollowTestCase(unittest.TestCase):
    def setUp(self):
        api = create_api()
        self.follow = Follow(api)

    def test_follow_followers(self):
        self.assertIsNotNone(self.follow.follow_followers)


if __name__ == '__main__':
    unittest.main()
