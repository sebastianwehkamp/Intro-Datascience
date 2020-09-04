from nltk.corpus import state_union
import nltk

#remove punctuation and stopwords
all_words=(w.lower() for w in state_union.words() if (w.isalpha()) and (w.lower() not in nltk.corpus.stopwords.words('english')))

#Word freq count
cfd = nltk.FreqDist(all_words)

#Calculate 50 most common words
mostcommon = cfd.most_common(50)

#Plot 50 most common words and print them
cfd.plot(50)
print(mostcommon)