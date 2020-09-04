library(Rtsne)

train <- read.csv(file.choose(new = FALSE), header=TRUE, stringsAsFactors=TRUE)

#Setting fixed seed
set.seed(42)

Labels<-train$S_labels
train$S_labels<-as.factor(train$S_labels)
## for plotting
colors = rainbow(length(unique(train$S_labels)))
names(colors) = unique(train$S_labels)

tsne <- Rtsne(train[,-1], dims = 2, perplexity=30, verbose=TRUE, max_iter = 500)

## Plotting
plot(tsne$Y, t='n', main="tsne")
text(tsne$Y, labels=train$S_labels, col=colors[train$S_labels])
