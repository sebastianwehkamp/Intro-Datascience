from nltk.corpus import gutenberg
import nltk
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


texts = gutenberg.fileids()
for text in texts:
    token_dict.append(gutenberg.raw(text))

#this can take some time
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english', lowercase = True, ngram_range=(1,3))
tfs = tfidf.fit_transform(token_dict)

#Print the word names with tf-idf score
feature_names = tfidf.get_feature_names()
for col in tfs.nonzero()[1]:
    print(feature_names[col], ' - ', tfs[0, col])