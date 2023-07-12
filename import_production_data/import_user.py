import pandas as pd
from sqlalchemy import create_engine
import random
import string
import warnings
import mysql.connector

import os
from dotenv import load_dotenv
load_dotenv()
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)



warnings.filterwarnings('ignore')

usernames = set()

# List of adjectives and nouns
adjectives = ['happy', 'brave', 'clever', 'daring', 'honest', 'kind', 'lively', 'calm', 'bold', 'gentle', 'funny', 'wild',
              'silly', 'vibrant', 'caring', 'curious', 'eager', 'fiery', 'jolly', 'noble', 'quirky', 'sassy', 'spunky',
              'talented', 'witty', 'zealous', 'cheerful', 'creative', 'determined', 'fearless', 'gracious', 'humorous',
              'intelligent', 'optimistic', 'passionate', 'patient', 'radiant', 'sincere', 'thoughtful', 'charming',
              'dashing', 'energetic', 'fierce', 'grateful', 'harmonious', 'inspiring', 'joyful', 'lovely', 'magnificent',
              'nurturing', 'outgoing', 'playful', 'resilient', 'sensible', 'talented', 'vivacious', 'whimsical', 'youthful',
              'zesty', 'adventurous', 'bold', 'confident', 'dynamic', 'enthusiastic', 'friendly', 'graceful', 'humble',
              'inventive', 'joyous', 'loving', 'mellow', 'nifty', 'optimistic', 'peaceful', 'radiant', 'sincere', 'tender',
              'upbeat', 'vibrant', 'witty', 'yummy', 'zany']

nouns = ['dog', 'cat', 'bird', 'lion', 'tiger', 'elephant', 'monkey', 'giraffe', 'kangaroo', 'panda', 'koala', 'zebra',
         'dolphin', 'whale', 'shark', 'octopus', 'butterfly', 'bee', 'snail', 'turtle', 'frog', 'squirrel', 'bear',
         'rabbit', 'horse', 'cow', 'sheep', 'goat', 'pig', 'chicken', 'duck', 'ostrich', 'parrot', 'peacock', 'owl',
         'penguin', 'crocodile', 'alligator', 'snake', 'lizard', 'jaguar', 'leopard', 'rhinoceros', 'hippopotamus',
         'zebu', 'gazelle', 'donkey', 'camel', 'buffalo', 'deer', 'moose', 'antelope', 'gorilla', 'orangutan',
         'chimpanzee', 'walrus', 'seal', 'sloth', 'beaver', 'rat', 'mouse', 'hamster', 'guinea pig', 'gerbil', 'rabbit',
         'hedgehog', 'ferret', 'skunk', 'armadillo', 'badger', 'fox', 'wolf', 'coyote', 'lynx', 'bobcat', 'weasel',
         'otter', 'raccoon', 'bat']

# Create a new pandas DataFrame with columns
# `username`, `password`, `wallet`
df = pd.DataFrame(columns=['username', 'password', 'wallet'])

# Generate users
for _ in range(10000):
    # Generate a random username in "reddit style"
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = f"{adjective.capitalize()}{noun.capitalize()}{random.randint(100, 999)}"

    while username in usernames:
        username = f"{adjective.capitalize()}{noun.capitalize()}{random.randint(100, 999)}"

    usernames.add(username)
    # Generate a random password of length 8
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    # Set the initial wallet balance to a random value between 1.00 and 200.00
    wallet = round(random.uniform(1.00, 200.00), 2)

    df = df.append({
        'username': username,
        'password': password,
        'wallet': wallet
    }, ignore_index=True)

    # If the DataFrame has more than 1000 rows, write it to the database and clear it
    if len(df) >= 1000:
        # create a connection to the MySQL server
        engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:3306/{db_name}')

        try:
            # Write the DataFrame to the 'User' table in the database
            df.to_sql('User', con=engine, if_exists='append', index=False)
        except Exception as e:
            print(e)
        # Empty the DataFrame
        df = pd.DataFrame(columns=['username', 'password', 'wallet'])

# Write any remaining rows to the database
if not df.empty:
    # Create a connection to the MySQL server
    engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:3306/{db_name}')
    try:
        # Write the DataFrame to the 'User' table in the database
        df.to_sql('User', con=engine, if_exists='append', index=False)
    except Exception as e:
        print(e)


def getUid():
    query = "SELECT uid from User"
    cursor = mydb.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        # Write to csv
        df = pd.DataFrame(result, columns=['uid'])
        df.to_csv('uid.csv', index=False)
        print("Data exported to 'uid.csv' successfully.")
    except mysql.connector.Error as error:
        print('There was an error in fetching users:')
        print(error)


getUid()
