import pandas as pd
# import gzip
# import shutil
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
# import subprocess
import mysql.connector

# # HELPERS:
# def is_brew_installed():
#     try:
#         subprocess.check_output(['brew', '-v'])
#         return True
#     except Exception:
#         return False

# def install_brew():
#     command = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
#     os.system(command)

def getMid():
    query = "SELECT mid from Movie"
    cursor = mydb.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        # Write to csv
        df = pd.DataFrame(result, columns=['mid'])
        df.to_csv('mid.csv', index=False)
        print("Data exported to 'mid.csv' successfully.")
    except mysql.connector.Error as error:
        print('There was an error in fetching users:')
        print(error)


########## MAIN ##########

load_dotenv()

    # Read database credentials from environment variables
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Create a connection to the MySQL server
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:3306/{db_name}')

mydb = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

# if not is_brew_installed():
#     print("Homebrew not found. Installing...")
#     install_brew()
#     print("Homebrew installed successfully.")
# else:
#     print("Homebrew is already installed.")


# Download and extract the TSV file
url = 'https://datasets.imdbws.com/title.basics.tsv.gz'
gz_file_path = 'title.basics.tsv.gz'
tsv_file_path = 'title.basics.tsv'

# try:
#     print("Installing wget using Homebrew...")
#     subprocess.run(['brew', 'install', 'wget'])
#     print("wget installed successfully.")
# except Exception as e:
#     print(f"Error occurred while installing wget: {e}")

# try:
#     print("Downloading the TSV file...")
#     subprocess.run(['wget', '-O', gz_file_path, url])
#     print("TSV file downloaded successfully.")

#     print("Unpacking the GZ file...")
#     with gzip.open(gz_file_path, 'rb') as f_in:
#         with open(tsv_file_path, 'wb') as f_out:
#             shutil.copyfileobj(f_in, f_out)
#     print("GZ file unpacked successfully.")
# except Exception as e:
#     print(f"Error occurred: {e}")

try:
    # Read the TSV file into a pandas DataFrame
    df = pd.read_csv(tsv_file_path, sep='\t', low_memory=False)

    # Filter for rows where titleType is 'movie'
    df = df[df['titleType'] == 'movie']

    # Strip the 'tt' prefix from the 'tconst' values and convert to integers
    df['tconst'] = df['tconst'].str.replace('tt', '').astype(int)

    # Split the 'genres' string on commas and only keep the first genre
    df['genres'] = df['genres'].str.split(',').str[0]

    # Rename the DataFrame columns to match the SQL table
    df = df[['primaryTitle', 'genres', 'startYear', 'runtimeMinutes']]
    df = df.rename(columns={'primaryTitle': 'title', 'genres': 'genre', 'startYear': 'release_year', 'runtimeMinutes': 'duration'})

    # Replace the '\\N' values in duration with 100
    df = df.replace('\\N', pd.NA).dropna()
    df = df.dropna(subset=['title'])




    try:
        # Write the DataFrame to the 'Movie' table in the database
        df.to_sql('Movie', con=engine, if_exists='append', index=False)
        print("Data inserted into the 'Movie' table successfully.")

    except Exception as e:
        print(e)

except Exception as e:
    print("Error processing the TSV file:", e)




# Export mid data to mid.csv
try:
    # Query to fetch all 'mid' from the 'Movie' table
    query = "SELECT mid FROM Movie"

    # Execute the query and store the result in a DataFrame
    getMid()
except Exception as e:
    print(f"Error occurred: {e}")