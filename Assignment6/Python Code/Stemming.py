import nltk
from nltk.corpus import state_union
from nltk.stem.porter import PorterStemmer

#stemmer declaration
stemmer=PorterStemmer()

#retrieve all non-stopwords and stem them
all_stems =(stemmer.stem(w.lower()) for w in state_union.words () if (w.isalpha ()) and 
           (w.lower() not in nltk.corpus.stopwords.words('english')))

#list of all unique stems in the collection
dist_stems=set(all_stems)
