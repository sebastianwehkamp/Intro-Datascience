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

#Create model using previously created BIC and VVV as model
BIC = mclustBIC(sampledData3, G=1:17)
modDefault = Mclust(sampledData3, x=BIC, modelName = "VVV")
plot(modDefault, what = "classification")

#Apply dimensionility reduction and create scatter plot
modDR = MclustDR(modDefault)
plot(modDR)


# add a column in myData CLUST with the cluster.
sampledData3$CLUST <- modDefault$classification

# now to write it out:
write.csv(sampledData3[,c("CLUST","V1","V2","V3")], # reorder columns to put CLUST first
          file="out.csv",                  # output filename
          row.names=FALSE,                 # don't save the row numbers
          quote=FALSE)    



