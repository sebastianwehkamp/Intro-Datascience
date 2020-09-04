install.packages(c("openssl","httr", "jsonlite", "lubridate"))
library("httr")
library(jsonlite)
library(lubridate)
imdbCSV <- read.csv(file.choose(new = FALSE))

resultFrame <- data.frame( Title=character(),
                  ReleaseDate=as.Date(character()),
                  Popularity=double(), 
                  Budget=double(), 
                  Revenue=double(),
                  Genre=character(),
                  ImdbRating=double(),
                  ImdbVotes=integer(),
                  Director=character(),
                  Country=character()
                  ) 

for (i in 1:length(imdbCSV$Title)) {
  #check if the name doesn't contain special characters
  if (grepl('[^[:alnum:]]', imdbCSV$Title[i])) {
    title <- imdbCSV$Title[i]
    
    #releaseDate
    if (imdbCSV$ReleaseDate[i] != "'NaT'") {
      #it is a properdate
      releaseDate <- as.Date(imdbCSV$ReleaseDate[i], "'%d/%m/%Y'")
    } else {
      releaseDate <- NA
    }
    
    popularity <- imdbCSV$Popularity[i]
    
    if (imdbCSV$Budget[i] != 0) {
      budget <- imdbCSV$Budget[i]
    } else {
      budget <- NA
    }
    
    if (imdbCSV$Revenue[i] != 0) {
      revenue <- imdbCSV$Revenue[i]
    } else {
      revenue <- NA
    }
    
    url <- paste0("http://www.omdbapi.com/?apikey=863c5282&t=", gsub(' ', "%20", imdbCSV$Title[i]))
    if (!is.na(releaseDate)) {
      url <- paste0(url,"&y=",format(releaseDate, "%Y"))
    }
    
    #retrieve the movie
    rawData <- GET(url = url)
    if (rawData$status_code == 200) {
      movieData <- fromJSON(rawToChar(rawData$content))
      if (movieData$Response == "True") {
        #the movie exists    
        print(paste0("It Exists: ",i))
        print(movieData$Title)
        resultFrame <- rbind(resultFrame, data.frame( Title=title,
                                                      ReleaseDate=releaseDate,
                                                      Popularity=popularity, 
                                                      Budget=budget, 
                                                      Revenue=revenue,
                                                      Genre=movieData$Genre,
                                                      ImdbRating=movieData$imdbRating,
                                                      ImdbVotes=movieData$imdbVotes,
                                                      Director=movieData$Director,
                                                      Country=movieData$Country
                                                      )
        )
      }
    }
  }
}