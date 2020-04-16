import tweepy
import logging
from config import create_api
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            return "Ignored"
        if not tweet.favorited:
            try:
                tweet.favorite()
                logger.info(f"Tweet {tweet.id} favorited with success")
            except Exception as e:
                logger.error('Error on like tweet', exc_info=True)
                raise e
        else:
            logger.info(f"{tweet.id} Already favorited")

        if not tweet.retweeted:
            try:
                tweet.retweet()
                logger.info(f"Tweet {tweet.id} retweeted with success")
            except Exception as e:
                logger.error('Error on retweet', exc_info=True)
        else:
            logger.info(f"{tweet.id} Already favorited")

    def on_error(self, status):
        logger.error(status)


def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=['en'])


if __name__ == '__main__':
    main(["Python", "Javascript"])
