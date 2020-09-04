import pandas as pd

#Read the provided CSV file lastFM.tsv 
labels = pd.read_csv('labelsFlowCapAnalysis2017.csv')

features = pd.read_csv('featuresFlowCapAnalysis2017.csv', header=0)

#Merge them
merged = labels.join(features, how='outer')

#Export to CSV
del merged.index.name
merged.to_csv('merged.csv')