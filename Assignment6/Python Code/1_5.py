# -*- coding: utf-8 -*-
from nltk.corpus import gutenberg
import nltk
from nltk.corpus import stopwords
from sklearn.decomposition import NMF

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



#texts = gutenberg.fileids()
#for text in texts:
#    token_dict.append(gutenberg.raw(text))
#    break
    
#Three manually added texts if needed
token_dict.append(gutenberg.raw('austen-sense.txt'))
token_dict.append(gutenberg.raw('austen-emma.txt'))
token_dict.append(gutenberg.raw('austen-persuasion.txt'))
    
print("Docs added!")

tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english', lowercase = True, ngram_range=(1,3))
print("Vectorizer created!")
tfs = tfidf.fit_transform(token_dict)
print("Model fit!")

#tfidf = vectorizer.fit_transform(dataset.data)

nmf = NMF(n_components=2, random_state=1)
X = nmf.fit_transform(tfs)
print("NMF done!")
print(X)