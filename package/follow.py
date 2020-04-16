import tweepy
import logging
import time
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Follow:
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def follow_followers(self):
        logger.info('Retrieving and following followers')
        try:
            for follower in tweepy.Cursor(self.api.followers).items():
                if not follower.following:
                    follower.follow()
                    logger.info('Following {}'.format(follower.name))
                return True
        except Exception:
            logger.error('Error to follow users', exc_info=True)
            return False


def main():
    api = create_api()
    f = Follow(api)
    while True:
        f.follow_followers()
        logger.info('Waiting...')
        time.sleep(60)


if __name__ == '__main__':
    main()
