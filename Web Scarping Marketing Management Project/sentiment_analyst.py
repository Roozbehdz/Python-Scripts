import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
import numpy as np
import pandas as pd
import os

def sentiment_analyzer_scores(sentence):
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(sentence)
    return score


def VaderAnalyzer(df):

    db = df
    sentiment_db = pd.DataFrame(columns=['negative_sentiment','neutral_sentiment',
                                                    'positive_sentiment','compound_sentiment'])

    for Text in db.Text:
        scores = sentiment_analyzer_scores(Text)
        new_entry = []
        new_entry += [scores['neg'],scores['neu'],scores['pos'],scores['compound']]
        single_db = pd.DataFrame([new_entry], columns=['negative_sentiment','neutral_sentiment',
                                                        'positive_sentiment','compound_sentiment'])
        sentiment_db= sentiment_db.append(single_db, ignore_index=True)

    db['negative_sentiment'] = sentiment_db.negative_sentiment
    db['positive_sentiment'] = sentiment_db.positive_sentiment
    db['neutral_sentiment'] = sentiment_db.neutral_sentiment
    db['compound_sentiment'] = sentiment_db.compound_sentiment

    return db