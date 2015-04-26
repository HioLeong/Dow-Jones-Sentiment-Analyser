import data_access.dow_jones as dj
import data_access.tweets as ts

from learners.linear_regression import LinearRegressionLearner
from learners.logistic_regression import LogisticRegressionLearner
from learners.naive_bayes import NaiveBayesLearner

from sklearn.metrics import confusion_matrix

from pymongo import MongoClient
from random import shuffle

client = MongoClient()
db = client.dowjones_sa

threshold_map = {'chevron':0.21289, 'coca cola': 0.05657, 'exxon':0.19253}

def label_company_threshold(tweet):
    threshold = threshold_map[tweet['company']]
    if tweet['price'] > threshold:
        return 1
    elif tweet['price'] < -threshold:
        return -1
    else: 
        # Neutral
        return 0

def get_label_counts(target):
    print target.count(1)
    print target.count(0)
    print target.count(-1)


if __name__ == '__main__':
    #tweets = ['hello, is it me', 'are looking for']
    tweets = list(db.tweetswithprices.find({},{'text':1, 'price':1, 'company':1}))
    tweets_len = len(tweets)
    print 'shuffling'
    shuffle(tweets)
    target = map(label_company_threshold, tweets)
    #get_label_counts(target)
    tweet_texts = map(lambda x: x['text'], tweets)
    labelled_tweets = [tweet_texts, target]

    print 'learning now'
    training_tweets = tweet_texts[:2100]
    training_target = target[:2100]
    learner = LinearRegressionLearner([training_tweets[210:], training_target[210:]])
    learner.train()

    l = learner.classify(training_tweets[:210])
    print confusion_matrix(l, training_target[:210])

    '''
    ts.store_data('data/tweets.csv')
    dj.store_data('data/ChevronCVX.csv', 'chevron')
    dj.store_data('data/ExxonXOM.csv', 'exxon')
    dj.store_data('data/ColaKO.csv', 'coca cola')
    '''
