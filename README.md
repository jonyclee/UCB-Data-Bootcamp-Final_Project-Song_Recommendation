# Songs Recommender

### Description
***
The goal of this project was to create a song recommendation system. To achieve this, first we have obtain a list of songs along with some basic information regarding each song such as genre, mood, and tempo. After obtaining a basic dataset, we created a Flask that would obtain user input. Next, we applied the user input into a machine learning algorithem that would generate a song recommendation based on user input.

### API
***
##### Billboard
We used billboard to obtain the top 100 songs for 4 years.
##### PyLyric
We used pyLyric to obtain the lyrics
##### pygn
We used pygn to obtain some basic information such as genre, mood, and tempo about each song.
* Note: pygn file was obtained Ching-Wei Chen [Github](https://github.com/cweichen/pygn)

### Machine Learning
***
We used GradientBoostingRegressor to predict potential scores of each song in order to recommend a song to the user. The features of GradientBoostingRegressor were chosen to maximize r2 score while minimizing MSE.

### Flask
***
We deployed a Flask to obtain user information and run our machine learning model.

### Contributor
***
Jonathan Lee [GitHub](https://github.com/jonyclee) <br />
Johnny Li [GitHub](https://github.com/johnnyli93)

##### Technologies Used:
***
* Python notebook
* Python packages:
	- billboard
	- pandas
	- PyLyric
	- pgyn
	- numpy
	- vaderSentiment.vaderSentiment
	- re
	- string
	- operator
	- stop_words
	- Flask
	- random
	- sklearn
	- sqlalchemy
* html (bootstrap)