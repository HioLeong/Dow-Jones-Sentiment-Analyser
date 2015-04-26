from abstract_learner import DowJonesLearner

from sklearn import linear_model
from featureextractor import *

class LinearRegressionLearner(DowJonesLearner):
    def __init__(self, labelled_tweets):
        self.learner = linear_model.LinearRegression()
        self.labelled_tweets = labelled_tweets

    def train(self):
        features = self.get_tweets_feature_set(self.labelled_tweets[0])
        self.learner.fit(features, self.labelled_tweets[1])

    def classify_tweet(self, tweet_features):
        self.learner.predict(tweet_features)

    def classify(self, tweet):

if __name__ == '__main__':
    tweets = ['hello, is it me', 'are looking for']
    labelled_tweets = [tweets, [0,1]]
    lr = LinearRegressionLearner(labelled_tweets)
    lr.train()
