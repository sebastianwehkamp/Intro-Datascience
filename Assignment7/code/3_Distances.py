import csv
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import random
from sklearn.preprocessing import MinMaxScaler


scaler = MinMaxScaler(feature_range=(-1, 1))
reader = csv.reader(open("data6.csv", "r"), delimiter=",")
next(reader, None)
lines = [line for line in reader]
randomLines = random.sample(lines, 2800)
x = list(randomLines)
result = np.array(x).astype("float")
scaler.fit_transform(result)

sampleMetrics=[]
distances = []

for i in range(2, 52):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit_predict(result)
    distances.append(kmeans.inertia_)
    print("k: " +str(i)+"   cost: "+str(kmeans.inertia_))
    

fignum=1
fig = plt.figure(fignum, figsize=(10, 9))
plt.plot(range(2, 52), distances, 'rx-')
plt.xlabel('k')
plt.ylabel('Centroid Distances')
plt.title('The Elbow Method showing the optimal k')

fig.show()