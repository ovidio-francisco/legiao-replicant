import tweepy
import logging
import os

logger = logging.getLogger()


def get_consumer_key():
	return os.getenv("CONSUMER_KEY")       

def get_consumer_secret():
	return os.getenv("CONSUMER_SECRET")    

def get_access_token():
	return os.getenv("ACCESS_TOKEN")       

def get_access_token_secret ():
	return os.getenv("ACCESS_TOKEN_SECRET")




def create_api():
	consumer_key        = get_consumer_key()
	consumer_secret     = get_consumer_secret()
	access_token        = get_access_token()
	access_token_secret = get_access_token_secret()

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	
	#  api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	api = tweepy.API(auth, wait_on_rate_limit=True)
 
	#  print(consumer_key)

	try:
		api.verify_credentials()
		logger.info("Credintials verified!")
		#  pass
	except Exception as e:
		logger.error("Error creating API", exc_info=True)
		raise e

	logger.info("API created!")
	print("OK")

	return api

