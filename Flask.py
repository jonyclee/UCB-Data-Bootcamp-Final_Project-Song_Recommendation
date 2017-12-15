# Dependencies
from flask import Flask, render_template, request
import pandas as pd
import random
import predictor as pre

# Set up Flask
app = Flask(__name__)

# Main page that leads to the form to fill out
@app.route("/")
def index():

	# Read the csv
	df = pd.read_csv('./csv/main.csv')

	rand_songs = []

	# Function to get random songs
	def get_songs():
		index = random.randint(0,len(df)-1)
		temp_data = df.iloc[index]
		if temp_data['Title'] not in rand_songs:
			rand_songs.append(temp_data['Title'])
		else:
			get_songs()

	for i in range(0,20):
		get_songs()

	return render_template("index.html",song_1=rand_songs[0],song_2=rand_songs[1],song_3=rand_songs[2],song_4=rand_songs[3]
		,song_5=rand_songs[4],song_6=rand_songs[5],song_7=rand_songs[6],song_8=rand_songs[7],song_9=rand_songs[8],song_10=rand_songs[9]
		,song_11=rand_songs[10],song_12=rand_songs[11],song_13=rand_songs[12],song_14=rand_songs[13],song_15=rand_songs[14],song_16=rand_songs[15]
		,song_17=rand_songs[16],song_18=rand_songs[17],song_19=rand_songs[18],song_20=rand_songs[19])

# Page for Recommended Song
@app.route("/predict", methods=["POST"])
def predict():

	# Get the genre from the form
    genre = request.form.get('genre')

    # Get the user score and songs from the form
    song_scores = []
    songs_title = []

    for i in range(1,21):
    	song = 'SONG_' + str(i)
    	name = 'song_' + str(i)
    	score = request.form.get(str(song))
    	song_scores.append(score)
    	title = request.form.get(name)
    	songs_title.append(title)

    print(len(songs_title))
    print(len(song_scores))

    song_rec, lyric_rec, artist_rec = pre.ml(songs_title, song_scores, genre)

    return render_template("predict.html", genre=genre, title=song_rec, lyric=lyric_rec, artist=artist_rec)

if __name__ == '__main__':
    app.run(debug=True)