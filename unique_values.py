# Dependencies
import pandas as pd
import re

# Read csv
df = pd.read_csv('./csv/main.csv')

# Function to get unique vales
def get_unique(li):

	unique_values = []

	# Get alphabet char only
	regex = re.compile('[^a-zA-Z &]')
	for i in range(0, len(li)):
		k = li[i].split(',')
		for j in range(0,len(k)):
			l = k[j].lstrip()
			l = regex.sub('',l)
			if l not in unique_values:
				unique_values.append(l)

	return unique_values

uniq_genre = get_unique(df['Genre'])
uniq_mood = get_unique(df['Mood'])
uniq_tempo = get_unique(df['Tempo'])

# Saves uniqe value into df
unique_genre_df = pd.DataFrame({'Genre': uniq_genre})
unique_mood_df = pd.DataFrame({'Genre': uniq_mood})
unique_tempo_df = pd.DataFrame({'Genre': uniq_tempo})

# Turn df into csv
unique_genre_df.to_csv('./csv/uniq_genre.csv')
unique_mood_df.to_csv('./csv/uniq_mood.csv')
unique_tempo_df.to_csv('./csv/uniq_tempo.csv')