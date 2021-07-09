import scipy, numpy, pandas

import nltk 
from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt
import random

# nltk.download('twitter_samples')

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

print('Number of positive tweets: ', len(all_positive_tweets))
print('Number of negative tweets: ', len(all_negative_tweets))

print('\nThe type of all_positive_tweets is: ', type(all_positive_tweets))
print('The type of a tweet entry is: ', type(all_negative_tweets[0]))

fig = plt.figure(figsize=(5, 5))
labels = 'ML-BSB-Lec', 'ML-HAP-Lec','ML-HAP-Lab'

sizes = [40, 35, 25]

plt.pie(sizes, labels=labels, autopct='%.2f%%',
shadow=True, startangle=90)

plt.axis('equal')
plt.show()