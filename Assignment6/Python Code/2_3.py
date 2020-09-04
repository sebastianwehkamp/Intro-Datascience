# -*- coding: utf-8 -*-
from nltk.corpus import gutenberg
import nltk
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

# Function to do stemming
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

# Tokenizer removing punctuation and remoivng capitals
def tokenize(text):
    tokens = nltk.word_tokenize(text)
    cleantext = (w for w in tokens if (w.isalpha() and w not in stopwords.words('english')))
    stems = stem_tokens(cleantext, stemmer)
    return stems


# Function calculating the tfidf rating for every document
def get_corpus_rep_words(corpus, top_n):
    #Append all gutenberg texts to dictionairy
    token_dict = []
    repwords = []
    for fileid in corpus.fileids():
        token_dict.append(corpus.raw(fileid))
    
    #Create TFIDF model
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english', lowercase = True, ngram_range=(1,3))
    tfs = tfidf.fit_transform(token_dict)

    #Calculate the top n words for every document
    for j in range(len(token_dict)):
        wordindexes =  tfs.getrow(j).todense().A1.argsort()[-top_n:][::-1]
        wordfeatures = tfidf.get_feature_names()
        templist = []
        for i in wordindexes:
            templist.append(wordfeatures[i])
        repwords.append(templist)
    return repwords

# Converting a index to the docuement name
def get_doc_from_IDX(index, corpus):
   docList = corpus.fileids()
   return docList[index]    
    
# Where was that function from assignement        
def where_was_that(text, corpus):
    repWords = get_corpus_rep_words(corpus, 1000)
    stems = tokenize(text)
    matches = []
    for idx, doc in enumerate(repWords):
        # Add a tuple to list consisting of (document index, document name, number of matches)
        matches.append((idx, get_doc_from_IDX(idx, corpus), (len(set(doc) & set(stems)))))

    # Sort based on number of matches
    sortedList = sorted(matches, key=lambda tup: tup[2], reverse=True)
    return(sortedList[:10])
  
     
# Sample texts from assignement
textWonderland = "story with the girl falling into a rabbit hole"
textMoby = "Story with the sailor and the whale"
print(where_was_that(textMoby, gutenberg))         
