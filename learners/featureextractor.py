from sklearn.feature_extraction import FeatureHasher
from sklearn.feature_extraction.text import CountVectorizer
import re

corpus = ["This is going to :) ", "This is an array :(", "of all the tweets :)"];
bigram_vectorizer = CountVectorizer(ngram_range=(2, 2), token_pattern=r'\b\w+\b', min_df=1)

def getBigrams( corpus ):
    analyze = bigram_vectorizer.build_analyzer()
    out = []
    for s in corpus:
        out.append(analyze(s))
    hasher = FeatureHasher(input_type='string')
    return hasher.transform(out)
    #return out

def getVectorizedBigrams( corpus ): 
    X_2 = bigram_vectorizer.fit_transform(corpus).toarray()
    return X_2

def getEmoticons( corpus ):
    out = []
    for s in corpus:
        found = re.search('[0-9A-Za-z\&\-\.\/()=:;]+', s).group(1)
        if found:
            out.append(found)
        else:
            out.append("")
    return out

if __name__ == "__main__":
    print(getEmoticons(corpus))
    print(getBigrams(corpus))
    print(getVectorizedBigrams(corpus))
