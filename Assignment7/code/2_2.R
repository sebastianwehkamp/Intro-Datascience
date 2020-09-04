library("clustertend")
data3 <- read.csv(file.choose(new = FALSE), header=TRUE, stringsAsFactors=TRUE)
data6 <- read.csv(file.choose(new = FALSE), header=TRUE, stringsAsFactors=TRUE)

sample <- data3[sample(nrow(data6), 2800, replace=FALSE),]

hop <- hopkins(sample, 10, header=T)
