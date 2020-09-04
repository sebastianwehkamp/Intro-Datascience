# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 12:01:22 2017

@author: Sebastian
"""

import pandas as pd

#Read the provided CSV file lastFM.tsv 
lastFM = pd.read_csv('lastFM.tsv', sep='\t')
#Assign proper names to columns
lastFM.columns = ['User', 'Timestamp', 'MBIDBand', 'Band', 'MBIDSong', 'Song']
#Drop MBID columns since they are not needed
lastFM = lastFM[['User', 'Timestamp', 'Band', 'Song']]

#Read the other tsv file
profiles = pd.read_csv('userid-profile.tsv', sep='\t')
profiles.columns = ['User', 'Gender', 'Age', 'Country', 'Registered']

#Merge them
merged = pd.merge(lastFM, profiles, how='right', on='User')

#Export to CSV
merged.to_csv('merged.csv')
