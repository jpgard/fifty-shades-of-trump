
#code from https://videlais.com/2015/03/02/how-to-create-a-basic-twitterbot-in-python/

#import HMM model generator, neural net model, 
#or change TWEET_FILE to file of pre-generated tweets

#TODO: docstrings for functions

#TODO: make this a funcy program??

#load Twitter credentials; you can define below instead

j = json.load(open('../private/twitter_keys.json', 'r'))
CONSUMER_KEY = j['CONSUMER_KEY']
CONSUMER_SECRET = j['CONSUMER_SECRET']
ACCESS_TOKEN = j['ACCESS_TOKEN']
ACCESS_SECRET = j['ACCESS_SECRET']

TWEET_FILE = "robotweets.txt"

import tweepy

class TwitterAPI:
    def __init__(self):
        consumer_key = ""
        consumer_secret = ""
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = ""
        access_token_secret = ""
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self):
        with open(TWEET_FILE, 'r') as robotweets:
            #TODO: implement prompt user check for tweet approval 
            #t = robotweets.readline()
            # print (t)

            # message = t

        self.api.update_status(status=message)


if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet("I'm posting a tweet!")