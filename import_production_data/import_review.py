import pandas as pd
from sqlalchemy import create_engine
import random
import datetime
import warnings
from dotenv import load_dotenv
load_dotenv()

warnings.filterwarnings('ignore')

# Load mid.csv into a DataFrame
df_mid = pd.read_csv('mid.csv')

# Load comments.csv into a DataFrame
df_comments = pd.read_csv('comments.csv')

# Create a new pandas DataFrame with columns
# `uid`, `mid`, `review_date`, `rating`, `comment`
df = pd.DataFrame(columns=['mid', 'review_date', 'rating', 'comment'])

# Convert the mid column of df_mid to a list
values = df_mid['mid'].tolist()

# Load uid.csv into a DataFrame
df_uid = pd.read_csv('uid.csv')

# Convert the uid column of df_uid to a list
values_uid = df_uid['uid'].tolist()

# Dates for generating reviews
start_date_review = datetime.date(2020, 1, 1)
end_date_review = datetime.date(2023, 12, 31)

# Create a connection to the MySQL server
import os
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# create a connection to the MySQL server
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:3306/{db_name}')


def batch_to_sql(df, table_name, engine):
    try:
        # write the DataFrame to the 'Review' table in the database
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
    except Exception as e:
        # Print the movie name
        print(e)
    # Empty the DataFrame
    df = df.iloc[0:0]
    return df

for mid in values:
    # Generate a random review for each movie
    review_date = start_date_review + (end_date_review - start_date_review) * random.random()
    rating = random.randint(1, 5)

    # Sample a comment from comments.csv
    comment = random.choice(df_comments['comment'].tolist())

    df = df.append({
        'uid': random.choice(values_uid),
        'mid': mid, 
        'review_date': review_date,
        'rating': rating,
        'comment': comment
    }, ignore_index=True)

    # If the DataFrame has more than 1000 rows, write it to the database and clear it
    if len(df) > 1000:
        df = batch_to_sql(df, 'Review', engine)

# Write any remaining rows to the database
if len(df) > 0:
    df = batch_to_sql(df, 'Review', engine)
