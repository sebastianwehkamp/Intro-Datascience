import nltk
from nltk.corpus import gutenberg
from nltk.corpus import state_union
from pylab import *

def createPlot(source):
    #Word freq count
    cfd = nltk.FreqDist(source.words())

    #Add the Frequency vs Frequency Rank
    wordList = [0]
    freqList = [0]
    rankList = [0]
    curRank = 1
    for word in cfd.most_common(len(cfd.items())):
        wordList.append(word[0])
        freqList.append(word[1])
        rankList.append(curRank)
        curRank += 1
    loglog(rankList, freqList, marker=".")


    #Add the zipf function
    zipfFreqList = []
    zipfRankList = []
    for n in rankList:
        if (not (n==0)):
            zipfFreqList.append(freqList[1]/n)
            zipfRankList.append(n)
    loglog(zipfRankList, zipfFreqList, marker=".")

    grid(True)
    title("Frequency vs Frequency Rank")
    xlabel("Frequency rank")
    ylabel("Frequency")
    for n in [1,10,100,1000,10000]:
        text(rankList[n], freqList[n], wordList[n])
    show()

createPlot(state_union)
createPlot(gutenberg)