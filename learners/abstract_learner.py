from abc import ABCMeta, abstractmethod

class DowJonesLearner(object):
    __metaclass__ = ABCMeta

    def get_tweets_feature_set(self, tweets):
        pass

    @abstractmethod
    def train(self, training_set):
        pass

    @abstractmethod
    def classify_tweet(self, tweet_features):
        pass
