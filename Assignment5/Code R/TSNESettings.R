library(Rtsne)

train <- read.csv(file.choose(new = FALSE), header=TRUE, stringsAsFactors=TRUE)

#Setting fixed seed
set.seed(42)

Labels<-train$S_labels
train$S_labels<-as.factor(train$S_labels)
## for plotting
colors = rainbow(length(unique(train$S_labels)))
names(colors) = unique(train$S_labels)

#Execute TSNE with one of the below settings

## Plotting
plot(tsne$Y, t='n', main="tsne")
text(tsne$Y, labels=train$S_labels, col=colors[train$S_labels])

####Settings####
#No PCA
tsne <- Rtsne(train[,-1], pca=FALSE, perplexity=30, verbose=TRUE, max_iter = 500)

#TSNE Scaling Center settings
tsne <- Rtsne(train[,-1], dims=2, perplexity=30, verbose=TRUE, max_iter = 500, pca_center = TRUE, pca_scale=FALSE)
tsne <- Rtsne(train[,-1], dims=2, perplexity=30, verbose=TRUE, max_iter = 500, pca_center = FALSE, pca_scale=FALSE)
tsne <- Rtsne(train[,-1], dims=2, perplexity=30, verbose=TRUE, max_iter = 500, pca_center = FALSE, pca_scale=TRUE)
tsne <- Rtsne(train[,-1], dims=2, perplexity=30, verbose=TRUE, max_iter = 500, pca_center = TRUE, pca_scale=TRUE)
