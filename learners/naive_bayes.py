from abstract_learner import DowJonesLearner

from sklearn import linear_model

class NaiveBayesLearner(DowJonesLearner):
    def __init__(self, tweets):
        self.learner = linear_model.LinearRegression()
        self.tweets = tweets

    def train(self, training_set):
        self.learner.fit(training_set.features, training_set.labels)

    def classify_tweet(self, tweet_features)
        self.learner.predict(tweet_features)
