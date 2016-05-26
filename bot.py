
#code from https://videlais.com/2015/03/02/how-to-create-a-basic-twitterbot-in-python/

#import HMM model generator, neural net model, 
#or change TWEET_FILE to file of pre-generated tweets

#TODO: docstrings for functions

#TODO: make this a click/cli program??

import tweepy, json

#load Twitter credentials; you can define below instead
j = json.load(open('../private/trump_keys.json', 'r'))
CONSUMER_KEY = j['CONSUMER_KEY']
CONSUMER_SECRET = j['CONSUMER_SECRET']
ACCESS_TOKEN = j['ACCESS_TOKEN']
ACCESS_SECRET = j['ACCESS_SECRET']

TWEET_FILE = "robotweets.txt"
HANDLE = "@50shadesofDJT"



class TwitterAPI:
    def __init__(self):
        consumer_key = CONSUMER_KEY
        consumer_secret = CONSUMER_SECRET
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = ACCESS_TOKEN
        access_token_secret = ACCESS_SECRET
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self):
        with open(TWEET_FILE, 'r') as robotweets:
            while True:
            #TODO: implement prompt user check for tweet approval 
                t = robotweets.readline()
                print (
                    "TWEET: \n\n%s\n\nWOULD YOU LIKE TO APPROVE THIS TWEET?" % (t))
                response = input(
                    "TYPE 1 for 'YES' or 0 for 'NO', 'E' for EXIT:\n")
                
                if response == '1':
                    self.api.update_status(status = t)
                    print("%s TWEETED: %s" %(HANDLE, t))
                    break
                if response == '0':
                    pass
                if response == 'E':
                    print('EXITED.')
                    break
                else:
                    print("INVALID RESPONSE, TRY AGAIN.")
                    pass
            


        #self.api.update_status(status=message)


if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet()