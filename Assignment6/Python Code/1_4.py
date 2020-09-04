import nltk
import time
from nltk.corpus import state_union
from nltk.collocations import *
from nltk.stem import WordNetLemmatizer
from nltk.corpus import names

#Check for names
allNames = ([name for name in names.words("male.txt")] +
           [name for name in names.words("female.txt")])
def maxOneName((a,b,c)):
    return not ((a in allNames and b in allNames) or (a in allNames and c in allNames) or (b in allNames and c in allNames))

def findNbest(finder, n):
    trigram_measures = nltk.collocations.TrigramAssocMeasures()
    resultList = []
    for col in finder.nbest(trigram_measures.pmi, n*3):
        if (len(resultList) >= n): break
        if maxOneName(col): resultList.append(col)
    return resultList

def performTrigram(wordSet, windowSize, printTime = False):
    start = time.time()
    finder = TrigramCollocationFinder.from_words(wordSet, window_size=windowSize)
    end = time.time()
    if printTime:
        print(end - start)
    return finder

def printResults(set):
    i = 1
    for (a,b,c) in set:
        print("\\item "+a+" "+b+" "+c)

#ADD 1.3 code here!!!!

printResults(findNbest(performTrigram(state_union.words(), 3, True), 10))
printResults(findNbest(performTrigram(state_union.words(), 5, True), 10))
printResults(findNbest(performTrigram(state_union.words(), 10, True), 10))
