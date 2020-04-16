import tweepy
from config import create_api
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class ReplyTo(tweepy.API):
	def __init__(self, api):
		self.api = api
		self.me = api.me()

	def search(self, keyword):
		try:
			founds = self.api.search(q=keyword)
			for f in founds:
				print(f.text)
				if keyword in f.text:
					u = f.user.screen_name
					msg = "Nice post, @{}!".format(u)
					f = self.api.update_status(msg, f.id)
					logger.info('Replied with success')

		except Exception:
			logger.error("Error", exc_info=True)

def main(keyword_search):
	api = create_api()
	reply = ReplyTo(api)
	reply.search(keyword_search)

if __name__ == '__main__':
	main('programming')
