import pandas as pd

url='https://en.wikipedia.org/wiki/List_of_Spanish_football_champions'
dataframe = pd.read_html(url, header=0)[2]

dataframe['Winner'] = dataframe['Winner'].map(lambda x: x.rstrip('*'))
dataframe['Winner'] = dataframe['Winner'].map(lambda x: x.rstrip('†'))
dataframe['Winner'] = dataframe['Winner'].map(lambda x: x.rstrip('‡'))
dataframe['Winner'] = dataframe['Winner'].str.replace('\d+', '')
dataframe['Winner'] =  dataframe['Winner'].apply(lambda x: x.replace('(','').replace(')',''))

dataframe['Runner-up'] = dataframe['Runner-up'].str.replace('\d+', '')
dataframe['Runner-up'] =  dataframe['Runner-up'].apply(lambda x: x.replace('(','').replace(')',''))

dataframe.to_csv('La Liga Champions.csv')

