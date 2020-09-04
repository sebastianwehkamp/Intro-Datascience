import numpy as np
from sklearn import tree
from sklearn.decomposition import PCA
import itertools


#the trainign samples
trainingData=np.genfromtxt("merged.csv", delimiter=",", skip_header=1, usecols=range(2, 187), max_rows=160)

#the class of each of the training data
classes=np.genfromtxt("merged.csv", delimiter=",", skip_header=1, usecols=(1), max_rows=160)

test=np.genfromtxt("merged.csv", delimiter=",", skip_header=161, usecols=range(2, 187), max_rows=19)
testClass=np.genfromtxt("merged.csv", delimiter=",", skip_header=161, usecols=(1), max_rows=19)


pca = PCA(n_components = 5)
classifier = tree.DecisionTreeClassifier ()
X_t_train = pca.fit_transform(trainingData)
classifier.fit(X_t_train , classes)
X_t_test = pca.transform(test)


#make the prediction
prediction=classifier.predict(X_t_test)

x=0

for i in range(len(prediction)):
    if testClass[i]==prediction[i]:
        x+=1
        
print (x/len(prediction))