from abstract_learner import DowJonesLearner

from sklearn.naive_bayes import MultinomialNB
from featureextractor import *

class NaiveBayesLearner(DowJonesLearner):
    def __init__(self, labelled_tweets):
        self.learner = MultinomialNB()
        self.labelled_tweets = labelled_tweets

    def train(self):
        features = self.get_tweets_feature_set(self.labelled_tweets[0])
        self.learner.fit(features, self.labelled_tweets[1])

    def classify_tweet(self, tweet_features):
        scores = self.learner.predict(tweet_features)
        print scores
        #return map(self.results_threshold, self.labelled_tweets[1])

    def classify(self, tweets):
        features = self.get_tweets_feature_set(tweets)
        return self.classify_tweet(features)
