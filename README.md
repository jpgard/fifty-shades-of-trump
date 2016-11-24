# fifty-shades-of-trump

This is a work in progress to support the forthcoming "Fifty Shades of Trump" Twitter bot. 

Currently, the script contains a tweet scraping utility, `scrape_tweets.py`, which scrapes tweets in batches of 200 (the max allowed by Twitter's GET status API) and stores the raw results into a database. The utility also supports an `update_tweet_db` function for maintaining a database of all tweets that can be continuously updated (allowing the user to obtain more than 3200 tweets by repeated scrapes), and an `output_text` function for writing a single text file with each tweet in the entire tweet cache separated by a newline.

#Usage: 3 steps to scraping tweet text

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

This builds a database that you can use to create/update your cache of tweets (which is the only way to exceed Twitter's limit of 3200 tweets--there is no convenient way to get tweets older than user's most recent 3200 tweets, so use this to build and update your cache of tweets regularly). This script will be modified to prompt you for the twitter handle; right now it goes straight for DJT.

##Step 2: `update_tweet_db`

`python scrape_tweets.py update_tweet_db`

This uses the results of `scrape` to build a new database, basically a cache of tweets. This is a new table in the existing database (because I like to keep things simple and tidy--fewer files this way). Every time you `scrape`, you can `update_tweet_db` afterward which will automatically add any new tweets to the tweet cache.  **Be patient**--this step might take a minute or two if you scraped lots of tweets.

##Step 3: `output_text`

`python scrape_tweets.py output_text`

This writes your entire tweet cache to a text file, separated by newlines:

```
The new NBC POLL has me in first place but said I was third in the debate - I demand a recount (just kidding!). EVERY other poll had me #1.  
I see Marco Rubio just landed another billionaire to give big money to his Superpac, which are total scams. Marco must address him as "SIR"!  
I am leaving for Norfolk, Virginia - the great battleship U.S.S. Wisconsin - for a big rally and really big crowd. See you soon!  
I told you so-@politico just lost it's top person. Poor results and no money to pay him. If they were legit, they would be doing far better!  
The @WSJ Wall Street Journal loves to write badly about me. They better be careful or I will unleash big time on them. Look forward to it!  
.@ColinCowherd said such nice things about me during the debate that I thought I'd do his show, @TheHerd, on Monday (2:30pm EST). 
```

The next step is to train a model (HMM n-gram model, neural network, etc.) using these tweets (and potentially other text), and to use the model to post pseudorandom text and post it to a Twitter account using a module like Tweepy.


#Tweet Generation Using TensorFlow LSTM:

This script (forthcoming) uses Google's TensorFlow library to train a LSTM model on the tweets generated using the steps above, as well as whichever saucy text you'd like to use.

If you're new to LSTMs or are interested in learning more, check out the following resources:

* [Understanding LSTMs](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
* [Google TensorFlow Tutorial - RNNs for Language Modeling](https://www.tensorflow.org/versions/master/tutorials/recurrent/index.html#tutorial-files)

:us: Now, go forth and support democracy! :us:
