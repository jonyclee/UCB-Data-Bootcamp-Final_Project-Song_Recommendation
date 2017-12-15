# Dependencies
import pandas as pd
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

# Read the csv
df = pd.read_csv('main.csv')

df = df.drop('Unnamed: 0',1)

# Create engine to connecting to songs_main
engine = create_engine("sqlite:///songs_main.sqlite")

# Creating a connection
conn = engine.connect()

# Declaring base
Base = declarative_base()

# Declare class called songs and table called main
class songs(Base):
	__tablename__="./csv/main"

	id = Column(Integer, primary_key=True)
	Artist = Column(String)
	Compound_Score = Column(Float)
	Genre = Column(String)
	Lyric = Column(String)
	Mood = Column(String)
	New_Score = Column(Float)
	Tempo = Column(String)
	Title = Column(String)
	Top_Word = Column(String)

# Use create all to create main table
Base.metadata.create_all(engine)

# Turns df into dictionary
song_data = df.to_dict(orient="record")

# Use sqlalchemy to reflect table
metadata = MetaData(bind=engine)
metadata.reflect()

# Save reference to main table
table = Table("main",metadata,autoload=True)

# Remove previous data in table to ensure clean table
conn.execute(table.delete())

# Insert data into table
conn.execute(table.insert(),song_data)