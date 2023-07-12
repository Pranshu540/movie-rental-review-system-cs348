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

# Create a new pandas DataFrame with columns
# `uid`, `mid`, `rent_date`, `due_date`, `is_active`
df = pd.DataFrame(columns=['mid', 'rent_date', 'due_date', 'is_active'])

# Convert the mid column of df_mid to a list
values = df_mid['mid'].tolist()

# Load uid.csv into a DataFrame
df_uid = pd.read_csv('uid.csv')

# Convert the uid column of df_uid to a list
values_uid = df_uid['uid'].tolist()

# Dates for generating rentals
start_date_active = datetime.date(2023, 7, 4)
end_date_active = datetime.date(2023, 7, 9)

start_date_inactive = datetime.date(2020, 1, 1)
end_date_inactive = datetime.date(2023, 6, 30)

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
        # write the DataFrame to the 'Movie' table in the database
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
    except Exception as e:
        # Print the movie name
        print(e)
    # Empty the DataFrame
    df = df.iloc[0:0]
    return df

for mid in values:
    users = set()
    # Generate active rentals
    rent_date = start_date_active + (end_date_active - start_date_active) * random.random()
    due_date = rent_date + datetime.timedelta(days=7)  # assuming due date is 7 days after rent date


    user = random.choice(values_uid)
    while user in users:
        user = random.choice(values_uid)
    users.add(user)

    df = df.append({
        'uid': user,
        'mid': mid, 
        'rent_date': rent_date,
        'due_date': due_date,
        'is_active': 1
    }, ignore_index=True)

    # Generate random number of inactive rentals
    num_rentals = random.randint(1, 10)
    
    for _ in range(num_rentals):
        rent_date = start_date_inactive + (end_date_inactive - start_date_inactive) * random.random()
        due_date = rent_date + datetime.timedelta(days=7)  # assuming due date is 7 days after rent date
        user = random.choice(values_uid)
        while user in users:
            user = random.choice(values_uid)
        users.add(user)

        df = df.append({
            'uid': user,
            'mid': mid, 
            'rent_date': rent_date,
            'due_date': due_date,
            'is_active': 0
        }, ignore_index=True)

    # If the DataFrame has more than 1000 rows, write it to the database and clear it
    if len(df) > 1000:
        df = batch_to_sql(df, 'Rental', engine)

# Write any remaining rows to the database
if len(df) > 0:
    df = batch_to_sql(df, 'Rental', engine)
