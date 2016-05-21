# fifty-shades-of-trump

This is a work in progress to support the "Fifty Shades of Trump" Twitter bot. Currently, the script contains a tweet scraping utility, `scrape_tweets.py`, which scrapes tweets in batches of 200 (the max allowed by Twitter's GET status API) and stores the raw results into a database. The utility also supports an `update_tweet_db` function for maintaining a database of all tweets that can be continuously updated (allowing the user to obtain more than 3200 tweets by repeated scrapes), and an `output_text` function for writing a single text file with each tweet in the entire tweet cache separated by a newline.

#Usage: 3 steps to tweet text

##Step 1: `scrape`

`python scrape_tweets.py scrape`

This scrapes tweets in batches of 200 (max allowed by Twitter). You'll know it's working when you see:

`fetching tweet batch 0 for user realdonaldtrump
fetching tweet batch 1 for user realdonaldtrump
fetching tweet batch 2 for user realdonaldtrump
fetching tweet batch 3 for user realdonaldtrump
fetching tweet batch 4 for user realdonaldtrump
fetching tweet batch 5 for user realdonaldtrump
...`

