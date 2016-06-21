"""
Utility for training HMM models on text files and using the model to generate
short pseudorandom text segments, and optionally tweet them using hashtags.
"""

import tweepy, json, markov_sentence_generator, click

#load Twitter credentials; you can define below instead
j = json.load(open('../private/twitter_keys.json', 'r'))
CONSUMER_KEY = j['CONSUMER_KEY']
CONSUMER_SECRET = j['CONSUMER_SECRET']
ACCESS_TOKEN = j['ACCESS_TOKEN']
ACCESS_SECRET = j['ACCESS_SECRET']
#UNCOMMENT TO DEFINE MANUALLY INSTEAD
#CONSUMER_KEY = ''
#CONSUMER_SECRET = ''
#ACCESS_TOKEN = ''
#ACCESS_SECRET = ''
TWEET_FILE = '/Users/joshgardner/Documents/Github/private/tweets_fifty.txt'
HANDLE = '@50shadesofDJT'





@click.group()
def cli():
	"""
	Tool to train Hidden Markov Model and use it to generate tweets.
	"""
	pass

@cli.command()
def hmm_tweet():
    """

    :return: None (prints tweet to command line; usually tweets require some
        manual inspection before posting directly to twitter.
    """
    click.echo('\nFetching your tweet from the Trump Train...\n')
    t = markov_sentence_generator.sentence_from_file(
        tweet_file, markovLength)