import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()

# read the TSV file into a pandas DataFrame
df = pd.read_csv('./title.basics.half.tsv', delimiter='\t')

# filter for rows where titleType is 'movie'
df = df[df['titleType'] == 'movie']

# strip the 'tt' prefix from the 'tconst' values and convert to integers
df['tconst'] = df['tconst'].replace('tt', '', regex=True).astype(int)

# split the 'genres' string on commas and only keep the first genre
df['genres'] = df['genres'].str.split(',').str[0]

# rename the DataFrame columns to match the SQL table
df = df[['primaryTitle', 'genres', 'startYear', 'runtimeMinutes']]

# replace the '\\N' values in duration with 100
df = df.replace('\\N', pd.NA).dropna()
df = df.dropna(subset=['primaryTitle'])



df = df.rename(columns={
    'primaryTitle': 'title',
    'genres': 'genre',
    'startYear': 'release_year',
    'runtimeMinutes': 'duration'
})

import os
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# create a connection to the MySQL server
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:3306/{db_name}')

try:
    # write the DataFrame to the 'Movie' table in the database
    df.to_sql('Movie', con=engine, if_exists='append', index=False)

except Exception as e:
    # Print the movie name
    print(e)

