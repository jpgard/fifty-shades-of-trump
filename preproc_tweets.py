"""
Imports a corpus of tweets, each separated by a newline character, and converts to standard Penn Tree Bank (PTB)
format, with end-of-sentence markers and a special token <unk> for rare words.

The output of this module is specifically designed to match the data in the data/ directory of the PTB dataset from Tomas Mikolov's webpage: http://www.fit.vutbr.cz/~imikolov/rnnlm/simple-examples.tgz for use in the Google TensorFlow tutorial on language modeling with LSTMs.
"""

import nltk, click
