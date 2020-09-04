require(mclust)

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

#Create BIC plot and statistics
BIC = mclustBIC(sampledData3, G=1:50)
plot(BIC)
summary(BIC)

#Create model using previously created BIC and VVV as model
modDefault = Mclust(sampledData3, x=BIC, modelName = "VVV")
summary(modDefault, parameters = TRUE)
plot(modDefault, what = "classification")

#Create model using random initialization
randPairs <- randomPairs(sampledData3)
str(randPairs)
modRand <- Mclust(sampledData3, initialization = list(hcPairs = randPairs), G=1:50)
plot(modDefault, what="BIC")
