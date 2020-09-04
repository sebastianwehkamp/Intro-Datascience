import pandas as pd
import urllib
import json
import csv
from dateutil.parser import parse


#Needed to check if date is valid
def is_date(string):
    try: 
        parse(string)
        return True
    except ValueError:
        return False

reader=pd.read_csv('movievalue.csv', encoding='latin1').dropna(subset=['Title'], how='all')
i=0

with open('new.csv', 'w', newline='') as new:
    writer=csv.writer(new)
    writer.writerow(('Title', 'ReleaseDate', 'Popularity', 'Budget', 'Revenue', 'Director', 'Genre', 'IMDBRating', 'IMDBVotes', 'BoxOfice', 'Production'))
    
    for title in reader.Title:
        
        link = "http://www.omdbapi.com/?apikey=863c5282&t=" + title.replace(" ", "+")
    
        if is_date(reader.ReleaseDate[i]):
            link += "&y=" + str(parse(reader.ReleaseDate[i]).year)
        
        try:
          with urllib.request.urlopen(link, timeout=10) as response:
              data=response.read().decode()
              result=json.loads(data)
              writer.writerow((reader.Title[i], reader.ReleaseDate[i], reader.Popularity[i], reader.Budget[i], reader.Revenue[i], result['Director'], result['Genre'], result['imdbRating'], result['imdbVotes'], result['BoxOffice'], result['Production']))
              i+=1
        except Exception:
            i+=1
        if i==10000:
            break
