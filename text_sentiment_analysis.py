# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:49:38 2022

@author: weron
"""

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import string


def sentiment_analysis(filepath):
    
    ''' This function takes filepath of txt file as an input and analyse the text for its sentiment.
    Returns text sentiment (in a scale on -1 to 1) and most common words that appeared in it (chooses
    only adjectives, nouns and verbs, so we can easily find pictures by keywords).
    '''

    f = open(filepath,"r")
    text = f.read()
    
    stopwords = nltk.corpus.stopwords.words("english")
    words = nltk.word_tokenize(text)
    words = [w for w in words if w.lower() not in stopwords] #remove stopwords like "a", "the" etc.
    words = list(filter(lambda words: words not in string.punctuation, words)) #remove punctuation
    tagged = nltk.pos_tag(words) #recognize parts of speech
    POS = ['NN', 'NNP', 'NNS','JJ','VB','VBD','VBG','VBP','VBN', 'VBZ']
    new_words = []
    for i in range(0, len(tagged)):
        for j in range(0,len(POS)):
            if (tagged[i][1] == POS[j]):
                new_words.append(tagged[i][0])
    
    fd = nltk.FreqDist(new_words)
    most_common_words = fd.most_common(6) # finds 6 most common words with number of occurences
    
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    compound = scores["compound"]
    
    return most_common_words, compound