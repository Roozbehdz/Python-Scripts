import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
import numpy as np
import pandas as pd
import os

def sentiment_analyzer_scores(sentence):
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(sentence)
    return score

def sentiment_analyst(file_input):

    db = file_input

    sentiment_db = pd.DataFrame(columns=['negative_sentiment','neutral_sentiment',
                                                    'positive_sentiment','compound_sentiment'])
    
    for review in db.review:
        scores = sentiment_analyzer_scores(review)
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


df = pd.read_csv(r'C:\Users\10\Desktop\Python Scripts\file1.csv',
                                            index_col=0, 
                                            parse_dates=True,
                                            squeeze=True)
# df = df[0:10]
# df = df.to_frame()
# df  = sentiment_analyst(df)

# print(df)

# print(df['compound_sentiment'].mean())
# print(df['positive_sentiment'].mean())
# print(df['negative_sentiment'].mean())
# print(df['neutral_sentiment'].mean())

for i in range(0,5):
    print(df[i])
    print(sentiment_analyzer_scores(df[i]))

# # An "interface" to matplotlib.axes.Axes.hist() method
# n, bins, patches = plt.hist(x=df['compound_sentiment'], bins='auto', color='#0504aa',
#                             alpha=0.7, rwidth=0.85)
# plt.grid(axis='y', alpha=0.75)
# plt.xlabel('VADER Score')
# plt.ylabel('Frequency')
# plt.title('Compound Sentiment Histogram')
# maxfreq = n.max()
# # Set a clean upper y-axis limit.
# plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
# plt.show()

# n, bins, patches = plt.hist(x=df['positive_sentiment'], bins='auto', color='#28a745',
#                             alpha=0.7, rwidth=0.85)
# plt.grid(axis='y', alpha=0.75)
# plt.xlabel('VADER Score')
# plt.ylabel('Frequency')
# plt.title('Positive Sentiment Histogram')
# maxfreq = n.max()
# # Set a clean upper y-axis limit.
# plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
# plt.show()

# n, bins, patches = plt.hist(x=df['negative_sentiment'], bins='auto', color='#e53e1e',
#                             alpha=0.7, rwidth=0.85)
# plt.grid(axis='y', alpha=0.75)
# plt.xlabel('VADER Score')
# plt.ylabel('Frequency')
# plt.title('Negative Sentiment Histogram')
# maxfreq = n.max()
# # Set a clean upper y-axis limit.
# plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
# plt.show()
