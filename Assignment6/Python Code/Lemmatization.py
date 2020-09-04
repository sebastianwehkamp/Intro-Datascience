import nltk
from nltk.corpus import state_union
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

#declare lematizer
lemmatizer=WordNetLemmatizer()
stemmer=PorterStemmer()

#get all non-stopwords and lemmatize them
all_lemmas =(lemmatizer.lemmatize(w.lower()) for w in state_union.words () if (w.isalpha ()) and 
          (w.lower() not in nltk.corpus.stopwords.words('english')))

#create empy list for stemmed lemmas
stemmed_lemmas=[]

#populate list
for word in all_lemmas:
    stemmed_lemmas.append(stemmer.stem(word))

