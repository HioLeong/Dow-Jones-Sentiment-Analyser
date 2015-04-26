from sklearn.feature_extraction import FeatureHasher
from sklearn.feature_extraction.text import CountVectorizer
import re

corpus = ["This is going to :) ", "This is an array :(", "of all the tweets"];
bigram_vectorizer = CountVectorizer(ngram_range=(2, 2), token_pattern=r'\b\w+\b', min_df=1)
emojiset = set([":)",":-)","=)",":(",":-(","=(",":D"])

def getBigrams( corpus ):
    analyze = bigram_vectorizer.build_analyzer()
    out = []
    for s in corpus:
        out.append(analyze(s))
    hasher = FeatureHasher(input_type='string', non_negative=True)
    return hasher.transform(out)
    #return out

def getVectorizedBigrams( corpus ): 
    X_2 = bigram_vectorizer.fit_transform(corpus).toarray()
    return X_2

def getEmoticons( corpus ):
    out = []
    for tweet in corpus :
        found = False
        for emoji in emojiset:
            if emoji in tweet:
                out.append(emoji)
                found = True
        if not found:
            out.append("")
    return out

if __name__ == "__main__":
    print(getEmoticons(corpus))
