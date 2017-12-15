# Dependencies
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_absolute_error

# Function to perform predict users scores based on input
def ml(songs, scores, genre):
	# Read the csv
	df = pd.read_csv('./csv/main.csv')

	# Get dummy variables and store into a df
	features_df = pd.get_dummies(df, columns=['Genre', 'Mood', 'Tempo'])

	# Combine the songs and scores into a df
	user_score_df = pd.DataFrame({'Title': songs, 'User_score': scores})

	# Merge the features_df and user_score_df
	combine_df = pd.merge(features_df,user_score_df,on='Title',how='left')

	# Save scores and remove all unused variables
	del combine_df['Top_Word']
	del combine_df['Artist']
	del combine_df['Lyric']
	del combine_df['Title']
	del combine_df['Compound_Score']
	del combine_df['Unnamed: 0']

	# Drop all rows with missing values and save it to new df
	training_df = combine_df.dropna(0,how='any')

	# Save training scores and remove it from df
	training_scores = training_df['User_score']
	del training_df['User_score']

	# Turn df into matrices
	X = training_df.as_matrix()
	y = training_scores.as_matrix()

	# Split data into training and testing sets
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

	# Create model
	model = ensemble.GradientBoostingRegressor(
	    n_estimators=200,
	    learning_rate=0.1,
	    max_depth=1,
	    min_samples_leaf=1,
	    max_features=0.1,
	    loss='lad',
	    random_state=0
	)

	# Fit data into the model
	model.fit(X_train,y_train)

	# Remove user scores table
	del combine_df['User_score']

	# Predicts the scores of songs
	predictions = []
	for i in range(0,len(combine_df)):
	    temp = combine_df.iloc[i].as_matrix()
	    temp_matrix = np.asmatrix(temp)
	    temp_matrix.reshape(-1,1)
	    predicted = model.predict(temp_matrix)
	    predictions.append(predicted)

	# Store the predicted scores into a df
	features_df['Predicted_Scores'] = predictions

	# Filters the songs to fit user genre
	user_genre = "Genre_['" + genre + "']"

	recommendation_df = features_df.loc[features_df[user_genre]==1]

	rec_sorted_df = recommendation_df.sort('Predicted_Scores',ascending=False)


	for i in range(0,len(rec_sorted_df)):
		results = rec_sorted_df.iloc[i]
		if results['Title'] not in songs:
			continue

	return (results['Title'], results['Lyric'], results['Artist'])