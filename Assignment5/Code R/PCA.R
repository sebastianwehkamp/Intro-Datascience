library("FactoMineR")
library("factoextra")

features <- read.csv(file.choose(new = FALSE), header=TRUE, stringsAsFactors=TRUE)

#Run PCA
res.pca <- PCA(features, graph = FALSE)

#Store eigen values
eigenvalues <- res.pca$eig

#Create a nice plot
fviz_screeplot(res.pca, ncp=10)

# Coordinates of variables
head(res.pca$var$contrib)

#Create a plot showing the sum of contributions of the first five components.
fviz_contrib(res.pca, choice = "var", axes = 1:5, top = 10)
