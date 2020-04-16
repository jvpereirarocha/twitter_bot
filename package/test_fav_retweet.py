import unittest
import tweepy
from favretweet import FavRetweetListener
from config import create_api


class FavRetweetTestCase(unittest.TestCase):
    def setUp(self):
        api = create_api()
        self.fav_retweet = FavRetweetListener(api)

    def test_on_status_is_not_none(self):
        self.assertIsNotNone(self.fav_retweet.on_status)

    def test_on_status(self):
        self.assertIsInstance(self.fav_retweet, tweepy.StreamListener)

    def test_is_true(self):
        self.assertFalse(self.fav_retweet == tweepy.StreamListener)


if __name__ == '__main__':
    unittest.main()
