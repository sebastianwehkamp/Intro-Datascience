import numpy as np
from sklearn import tree
import itertools


#the trainign samples
trainingData=np.genfromtxt("merged.csv", delimiter=",", skip_header=1, usecols=range(2, 187), max_rows=179 )

#the class of each of the training data
classes=np.genfromtxt("merged.csv", delimiter=",", skip_header=1, usecols=(1), max_rows=179 )

#the data we want to predict
testData=np.loadtxt("merged.csv", delimiter=",", skiprows=180, usecols=range(2, 187), )


clf = tree.DecisionTreeClassifier()
clf = clf.fit(trainingData, classes)

#make the prediction
prediction=clf.predict(testData)


#print each sample and prediction
print("Sample    Prediction")

for i, j in itertools.zip_longest(range(len(prediction)), range(179, 359)):
    print(j, "        ", prediction[i])