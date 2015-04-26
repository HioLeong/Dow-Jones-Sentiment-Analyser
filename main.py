from learners.linear_regression import LinearRegressionLearner
from learners.logistic_regression import LogisticRegressionLearner
from learners.naive_bayes import NaiveBayesLearner

if __name__ == '__main__':
    tweets = ['hello, is it me', 'are looking for']
    labelled_tweets = [tweets, [0,1]]
    lr = LogisticRegressionLearner(labelled_tweets)
    lr.train()
