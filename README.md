# fifty-shades-of-trump

This is a work in progress to support the forthcoming "Fifty Shades of Trump" Twitter bot. 

Currently, the script contains a tweet scraping utility, `scrape_tweets.py`, which scrapes tweets in batches of 200 (the max allowed by Twitter's GET status API) and stores the raw results into a database. The utility also supports an `update_tweet_db` function for maintaining a database of all tweets that can be continuously updated (allowing the user to obtain more than 3200 tweets by repeated scrapes), and an `output_text` function for writing a single text file with each tweet in the entire tweet cache separated by a newline.

#Usage: 3 steps to tweet text

##Step 1: `scrape`

`python scrape_tweets.py scrape`

This scrapes tweets in batches of 200 (max allowed by Twitter). You'll know it's working when you see:
```
fetching tweet batch 0 for user realdonaldtrump
fetching tweet batch 1 for user realdonaldtrump
fetching tweet batch 2 for user realdonaldtrump
fetching tweet batch 3 for user realdonaldtrump
fetching tweet batch 4 for user realdonaldtrump
fetching tweet batch 5 for user realdonaldtrump
...
```

This builds a database that you can use to create/update your cache of tweets (which is the only way to exceed Twitter's limit of 3200 tweets--there is no convenient way to get tweets older than user's most recent 3200 tweets, so use this to build and update your cache of tweets regularly).

##Step 2: `update_tweet_db`

`python scrape_tweets.py update_tweet_db`

This uses the results of `scrape` to build a new database, basically a cache of tweets. This is a new table in the existing database (because I like to keep things simple and tidy--fewer files this way). Every time you `scrape`, you can `update_tweet_db` afterward which will automatically add any new tweets to the tweet cache. 

##Step 3: `output_text`

`python scrape_tweets.py update_tweet_db`

This writes your entire tweet cache to a text file, separated by newlines:

```
The new NBC POLL has me in first place but said I was third in the debate - I demand a recount (just kidding!). EVERY other poll had me #1.  
I see Marco Rubio just landed another billionaire to give big money to his Superpac, which are total scams. Marco must address him as "SIR"!  
I am leaving for Norfolk, Virginia - the great battleship U.S.S. Wisconsin - for a big rally and really big crowd. See you soon!  
I told you so-@politico just lost it's top person. Poor results and no money to pay him. If they were legit, they would be doing far better!  
The @WSJ Wall Street Journal loves to write badly about me. They better be careful or I will unleash big time on them. Look forward to it!  
.@ColinCowherd said such nice things about me during the debate that I thought I'd do his show, @TheHerd, on Monday (2:30pm EST). 
```


Now, go forth and support democracy! 
