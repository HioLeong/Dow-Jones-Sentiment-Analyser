from abc import ABCMeta, abstractmethod

class DowJonesLearner(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def train(self, training_set):
        pass

    @abstractmethod
    def classify_one(self, tweet):
        pass

    def classify_many(self, tweets):
        pass
