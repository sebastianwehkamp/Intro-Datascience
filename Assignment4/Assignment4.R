library(arules)
library(data.table)

#Read TSV
data <- read.csv(file.choose(new = FALSE), header=FALSE, stringsAsFactors=TRUE, sep="\t")
names(data) <- c('user', 'timestamp', 'mbid1', 'artist', 'mbid2', 'song')

#Drop mbid columns
keeps <- c('user', 'artist')
data <- data[keeps]

#Trans it
trans <- as(data, "transactions")

#Collapse dataframe
merged <- dcast(setDT(data), user ~ rowid(user), value.var = c('artist'), fill = '')

#Run apriori
rules <- apriori(trans, 
                 parameter = list(minlen=2, supp = 0.005, conf = 0.005),
                 appearance = list(lhs = c("artist=Ludwig Van Beethoven"), default = "rhs")
                 )
inspect(rules)

