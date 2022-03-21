#!/usr/bin/python3

import tweepy
import logging
import config

from LyricsAnswerer import LyricsAnswerer
from datetime import datetime


logging.basicConfig(level=logging.INFO, filename="legiaoreplicant.log")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())


class MyStreamListener(tweepy.Stream):

	def __init__(self, api_key, api_key_secret, access_token, access_token_secret):
		super().__init__(api_key, api_key_secret, access_token, access_token_secret)

		self.la = LyricsAnswerer()
		self.api = config.create_api()



	def on_status(self, tweet):

		if not tweet.truncated:
			text = tweet.text
		else:
			text = tweet.extended_tweet["full_text"]


		ans = self.la.answer(text)


		#  if (self.la.containsVerse(text)):
		if (len(ans) > 0):
			a = self.la.format_answer(ans)

			time = datetime.now().time().strftime("%H:%M:%S")
			logger.info(f"[{time}] ---------------")
			print("Original: \n" + text)

			self.like(tweet)
			self.reply(tweet, a)



	def reply(self, tweet, answer):

		if tweet.user.screen_name == "legiaoreplicant":
			logger.info(f"\nIt's me. tweet.user.screen_name: '{tweet.user.screen_name}'")
			return

		if tweet.retweeted:
			return
			
		tweet_user = tweet.user.screen_name
		tweet_id   = tweet.id

		try:
			self.api.update_status(
				status=answer,
				in_reply_to_status_id=tweet.id,
				auto_populate_reply_metadata=True
			)

			logger.info("---- Replied ----")
			logger.info(f"Answer = '{answer}'\n")
		except:
			logger.error("Error on reply", exc_info=True)




	def like(self, tweet):
		if not tweet.favorited:
			
			try:
				self.api.create_favorite(tweet.id)
				logger.info("Liked...")
			except Exception as e:
				logger.error("Error on like")
				







loc_brazil  = [-74.5 ,-34.2,-33.7,5.9 ]  # Location Brasil
loc_western = [-139.8,-56.4,48.3 ,71.3]  # Location Ocidente

def start_stream():
	while True:
		logger.info("Here we go!")
		try:

			consumer_key = config.get_consumer_key()
			consumer_secret = config.get_consumer_secret()
			access_token = config.get_access_token()
			access_token_secret = config.get_access_token_secret()

			#  print("key " + config.get_consumer_key())

			tweets_listener = MyStreamListener(consumer_key, consumer_secret, access_token, access_token_secret)


			#  langs = ["pt","es"]
			langs = ["pt"]
			logger.info(f"langs={langs}")

			tweets_listener.filter(locations=loc_brazil, languages=langs)

		except KeyboardInterrupt as e:
			logger.info(e)
			logger.info("\nBye :)")
			break

		except Exception as e:
			logger.info(e)
			time = datetime.now().time().strftime("%H:%M:%S")
			logger.info("\n======================================================================")
			logger.info(f"[{time}]")
			logger.info("Restarting stream\n")
			continue



start_stream()






