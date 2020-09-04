library(cluster)
library(HSAUR)

set.seed(381)

data3 <- read.csv(file.choose(new = FALSE), header=TRUE, stringsAsFactors=TRUE)
data6 <- read.csv(file.choose(new = FALSE), header=TRUE, stringsAsFactors=TRUE)

#Prepare data for merge and merge into dataTotal
data3$id <- c(1:nrow(data3))
data6$id <- c(1:nrow(data6))
dataTotal <- merge(data6, data3, by = "id")
drops <- c("id")
data3 <- data3[ , !(names(data3) %in% drops)]
data6 <- data6[ , !(names(data6) %in% drops)]
dataTotal <- dataTotal[ , !(names(dataTotal) %in% drops)]

#sample Data
sampleSelector <- sample(nrow(data3),2800)
sampledData3 <- data3[sampleSelector, ]
sampledData6 <- data6[sampleSelector, ]
sampledDataTotal <- dataTotal[sampleSelector, ]

mydata <- sampledData3
wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
for (i in 2:52) wss[i] <- sum(kmeans(mydata,
                                     centers=i)$withinss)
plot(1:52, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares")

mydata <- sampledData6
wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))
for (i in 2:52) wss[i] <- sum(kmeans(mydata,
                                     centers=i)$withinss)
plot(1:52, wss, type="b", xlab="Number of Clusters",
     ylab="Within groups sum of squares")
