import csv
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import random
from matplotlib import pyplot as plt

reader = csv.reader(open("data6.csv", "r"), delimiter=",")
next(reader, None)
lines = [line for line in reader]
randomLines = random.sample(lines, 4000)
x = list(randomLines)
result = np.array(x).astype("float")

sampleMetrics=[]

for i in range(2, 52):
    kmeans = KMeans(n_clusters=i)
    cluster_labels=kmeans.fit_predict(result)
    sampleMetrics.append((silhouette_score(result, cluster_labels, metric='euclidean')))

bestScore=max(sampleMetrics)
bestCluster=sampleMetrics.index(bestScore)
print("Best Sihlouete Score: "+str(bestScore))
print("Best Number of clusters: "+str(bestCluster+2))

fignum=1
fig = plt.figure(fignum, figsize=(10, 9))
plt.plot(range(2, 52), sampleMetrics, 'rx-')
plt.xlabel('k')
plt.ylabel('Silhouette Score')

fig.show()