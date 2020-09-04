library("FactoMineR")
library("factoextra")

merged <- read.csv(file.choose(new = FALSE), header=TRUE, stringsAsFactors=TRUE)

#Run PCA
res.pca <- PCA(merged, graph = FALSE)

#Plot based on labels
fviz_pca_ind(res.pca, col.ind=merged$S_labels)
