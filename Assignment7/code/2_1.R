data3 <- read.csv(file.choose(new = FALSE), header=TRUE, stringsAsFactors=TRUE)

sample <- data3[sample(nrow(data3), 28000, replace=FALSE),]

plot(sample)
