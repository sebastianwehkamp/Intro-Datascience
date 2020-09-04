from nltk.corpus import gutenberg
import nltk
import numpy as np
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

token_dict = []
stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    cleantext = (w for w in tokens if (w.isalpha() and w not in stopwords.words('english')))
    stems = stem_tokens(cleantext, stemmer)
    return stems


#Append all gutenberg texts to dictionairy
##for fileid in gutenberg.fileids():
#    token_dict.append(gutenberg.raw(fileid))
    
#Three manually added texts if needed
token_dict.append(gutenberg.raw('austen-sense.txt'))
token_dict.append(gutenberg.raw('austen-emma.txt'))
token_dict.append(gutenberg.raw('austen-persuasion.txt'))

#Create TFIDF model
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english', lowercase = True, ngram_range=(1,3))
tfs = tfidf.fit_transform(token_dict)
idf = tfidf._tfidf.idf_
feature_names = np.array(tfidf.get_feature_names())

#Calculate the top n words for every document
top_n = 10
for i in range(len(token_dict)):
    wordindexes =  tfs.getrow(i).todense().A1.argsort()[-top_n:][::-1]
    print (wordindexes)
    wordfeatures = tfidf.get_feature_names()
    for i in wordindexes:
        print (wordfeatures[i])
    print ("-----------------------next doc")
    