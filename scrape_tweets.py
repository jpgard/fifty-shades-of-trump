# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import dataset, time, json, math, click
import funcy as fy

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
RESULTS_DB_FILENAME = "tweets.db"
OUTPUT_TEXT_FILENAME = "tweets.txt"
db = dataset.connect('sqlite:///' + RESULTS_DB_FILENAME)
TABLE = db['raw_tweets']
ID_TABLE = db['tweets_by_id']
TWITTER_USER = 'realdonaldtrump'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter = Twitter(auth=oauth)


@click.group()
def cli():
	"""
	Tool to scrape user tweets.
	"""
	pass

def extract_tweets_and_ids(results):
	"""
	Generator yielding tweed IDs and text for incremental updates of ID_TABLE
	"""

	rawresults = json.loads(results['tweetdata']) 

	for tweet in rawresults:
		yield (tweet['text'], tweet['id'])

def extract_tweet_details(results):
	"""
	Generator yielding dict of full tweet details for each tweet.
	"""
	#TODO
	click.echo(
		"This should not print-extract_tweet_details is not implemented yet.")

@cli.command()
@click.argument('output_csv', type=click.File('wb'))
def output_csv(output_csv):
	'''Write csv file with more detailed tweet data'''
	#TODO
	#create csvwriter and write row for each tweet
	click.echo(
		"This should not print - output_csv is not implemented yet.")

@cli.command()
def output_text(output_text_filename = OUTPUT_TEXT_FILENAME): 
	#FLAG - parameters
	'''Write all tweets in the database into lines in a text file.'''
	tweets = [row['text'] for row in ID_TABLE.all()]
	count = 0
	with open(output_text_filename, 'w') as tweetfile:
		click.echo("writing " + output_text_filename)
		for tweet in tweets:
			tweetfile.write(tweet + '\n')
			count += 1
	click.echo(('wrote %s tweets to %s') % (count, output_text_filename))

def request_tweet_batch(batch_num, max_id):
	click.echo("fetching tweet batch %s for user %s" % (batch_num, TWITTER_USER))
	if batch_num == 0:
		tweets = twitter.statuses.user_timeline(
		screen_name=TWITTER_USER, count = 200) 
		#don't specify max_id for first batch, because twitter
	if batch_num != 0:
			tweets = twitter.statuses.user_timeline(screen_name=TWITTER_USER, count = 200, max_id = max_id)
	return tweets

@cli.command()
def update_tweet_db():
	"""
	Use this command after scraping a fresh batch of results using scrape.
	This adds any new tweets from the results to the tweet db, using IDs.
	"""

	tweets_w_id = fy.cat(extract_tweets_and_ids(row) for row in TABLE.all())

	for text,id in tweets_w_id:
		ID_TABLE.upsert(
			dict(id = id, text = text), 
			keys = ['id', 'tweet']
			)

	click.echo("tweet text database updated.")

@cli.command()
def scrape():
	'''Request tweets from API in batches of 200.'''
	batch_num = 0
	id_header = math.inf
	tweets = [None, None]

	while len(tweets) > 0 and id_header > 0:
		tweets = request_tweet_batch(batch_num, id_header)
		TABLE.upsert(dict(batch_num = batch_num, tweetdata = json.dumps(tweets)), keys = ['batch_num', 'tweetdata'])
		try: id_header = min([tweet['id'] for tweet in tweets]) - 1
		except ValueError: 
			id_header = 0
		batch_num += 1
		#wait 5 seconds to fall under limt of 300 requests per 15 minutes
		time.sleep(5.0)

	click.echo("complete.")

if __name__ == '__main__':
	cli()
