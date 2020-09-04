require(caret)

#setting seed so that random behaviour is consisitent
set.seed(38)

#set the working directory to the directory that contains the files using setwd()
features <-  read.csv(file.choose(new = FALSE), header=TRUE, stringsAsFactors=TRUE)
labels <-  read.csv(file.choose(new = FALSE), header=TRUE, stringsAsFactors=TRUE)

practiceFeatures <- features[c(1:nrow(labels)),]
testFeatures <- features[-c(1:nrow(labels)),]

#For some reason it demands make.names
labelgood <- make.names(labels$S_labels)

#Create model without preprocessing
knnModel <- train(practiceFeatures, 
                  labelgood, 
                  method='knn', 
                  trControl=trainControl(method='cv', number = 10, classProbs=TRUE, savePredictions="final"),
                  tuneGrid=expand.grid(k=c(1:25)))

predict <- predict(knnModel, features)

#Create model using 5 principle components
knnModel <- train(practiceFeatures, 
                  labelgood, 
                  method='knn', 
                  preProcess = c("pca", "center"),
                  trControl=trainControl(method='cv', number = 10, classProbs=TRUE, savePredictions="final", preProcOptions = list(pcaComp = 5)),
                  tuneGrid=expand.grid(k=c(1:25)))

top5predict <- predict(top5knnModel, features)

underSample <- features[c(1:29,35,44,56,61,72,74,90,98,107,119,121,131,133,137,140,143,173),]
underLabels <- labels[c(1:29,35,44,56,61,72,74,90,98,107,119,121,131,133,137,140,143,173),]

underLabelsGood <- make.names(underLabels)

underknnModel <- train(underSample, 
                       underLabelsGood, 
                       method='knn', 
                       trControl=trainControl(method='cv', number = 10, classProbs=TRUE, savePredictions="final"),
                       tuneGrid=expand.grid(k=c(1:25)))

underpredict <- predict(underknnModel, features)

finalPredict <- predict(knnModel, testFeatures)
write.csv(finalPredict, "FinalPrediction.csv")
