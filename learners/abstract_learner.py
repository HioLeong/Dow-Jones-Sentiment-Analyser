from abc import ABCMeta, abstractmethod
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn import cross_validation
from featureextractor import *

from sklearn.metrics import roc_curve, confusion_matrix

import pylab as pl
import numpy as np

class DowJonesLearner(object):
    __metaclass__ = ABCMeta

    def get_tweets_feature_set(self, tweets):
        #features = FeatureUnion([('bigrams', getBigrams(tweets)),('emoticons',getEmoticons(tweets))])
        #return np.array(zip(getBigrams(tweets),getEmoticons(tweets)))
        return getBigrams(tweets)

    def cross_validate(self):
        features = self.get_tweets_feature_set(self.labelled_tweets[0])
        scores = cross_validation.cross_val_score(self.learner, features, self.labelled_tweets[1], cv=10)
        return scores

    def draw_roc(self):
        scores = self.classify(self.labelled_tweets[0])
        print scores
        fpr, tpr, thresholds = roc_curve(scores, self.labelled_tweets[1], pos_label=1)
        print fpr
        print tpr
        pl.plot([0, 1], [0, 1], 'k--')
        pl.xlim([0.0, 1.0])
        pl.ylim([0.0, 1.0])
        pl.xlabel('False Positive Rate')
        pl.ylabel('True Positive Rate')
        pl.plot(fpr, tpr)
        pl.show()

    def confusion_matrix(self):
        scores = self.classify(self.labelled_tweets[0])
        print confusion_matrix(scores, self.labelled_tweets[1])

    def accuracy():
        pass

    @abstractmethod
    def train(self, training_set):
        pass

    @abstractmethod
    def classify_tweet(self, tweet_features):
        pass
