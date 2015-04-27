from abstract_learner import DowJonesLearner

from sklearn import linear_model
from sklearn.metrics import roc_curve
from featureextractor import *

class LinearRegressionLearner(DowJonesLearner):
    def __init__(self, labelled_tweets):
        self.learner = linear_model.LinearRegression()
        self.labelled_tweets = labelled_tweets

    def train(self):
        features = self.get_tweets_feature_set(self.labelled_tweets[0])
        self.learner.fit(features, self.labelled_tweets[1])

    def results_threshold(self,label):
        if label < -0.5:
            return -1
        elif label > 0.5:
            return 1
        else: 
            return 0

    def classify_tweet(self, tweet_features):
        scores = self.learner.predict(tweet_features)
        return map(self.results_threshold, self.labelled_tweets[1])

    def classify(self, tweets):
        features = self.get_tweets_feature_set(tweets)
        return self.classify_tweet(features)
