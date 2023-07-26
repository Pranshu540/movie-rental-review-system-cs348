import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

load_dotenv()  # load variables from .env file


class Config(object):
    MYSQL_DATABASE_USER = os.getenv("DB_USER")
    MYSQL_DATABASE_PASSWORD = os.getenv("DB_PASSWORD")
    MYSQL_DATABASE_DB = os.getenv("DB_NAME")
    MYSQL_DATABASE_HOST = os.getenv("DB_HOST")

