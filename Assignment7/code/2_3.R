#Set working directory to directory of the datasets
setwd("/media/HDD-Thijs/Schooldocumenten/2017-2018/IntroDataScience/assignment7")

#read Data from csv
data3 <- read.csv("data3.csv")
data6 <- read.csv("data6.csv")

#sample Data
sampledData3 <- data3[sample(nrow(data3), 2800), ]
sampledData6 <- data6[sample(nrow(data6), 2800), ]

dist3 <- dist(sampledData3, method = "euclidean") # distance matrix
dist6 <- dist(sampledData6, method = "euclidean") # distance matrix

#create plots
singleData3 <- hclust(dist3, method="single")
plot(singleData3, labels=FALSE, hang = -1, main="Single linkage, sampled data3", xlab="Stars", ylab="Distance", sub="")

singleData6 <- hclust(dist6, method="single")
plot(singleData6, labels=FALSE, hang = -1, main="Single linkage, sampled data6", xlab="Stars", ylab="Distance", sub="")

singleData3 <- hclust(dist3, method="complete")
plot(singleData3, labels=FALSE, hang = -1, main="Complete linkage, sampled data3", xlab="Stars", ylab="Distance", sub="")

singleData6 <- hclust(dist6, method="complete")
plot(singleData6, labels=FALSE, hang = -1, main="Complete linkage, sampled data6", xlab="Stars", ylab="Distance", sub="")

singleData3 <- hclust(dist3, method="average")
plot(singleData3, labels=FALSE, hang = -1, main="Average linkage, sampled data3", xlab="Stars", ylab="Distance", sub="")

singleData6 <- hclust(dist6, method="average")
plot(singleData6, labels=FALSE, hang = -1, main="Average linkage, sampled data6", xlab="Stars", ylab="Distance", sub="")