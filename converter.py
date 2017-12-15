# Dependencies
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# This function rescales score from 0 to 100
def convert(score):
	X = score.reshape(-1,1)
	scaler = MinMaxScaler(feature_range=(0,100))
	rescaledScore = scaler.fit_transform(X)
	return rescaledScore