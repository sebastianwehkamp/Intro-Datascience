import nltk
from nltk.corpus import state_union

#Word freq count
cfd = nltk.FreqDist(state_union.words())
cfd.plot(50)

j=1
for word in cfd.most_common(200):
    print(str(j)+" & "+str(word[0])+" & "+str(word[1])+"\\\\")
    j += 1