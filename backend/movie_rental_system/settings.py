import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


class Config(object):
    MYSQL_USER = os.getenv("DB_USER")
    MYSQL_PASSWORD = os.getenv("DB_PASSWORD")
    MYSQL_DB = os.getenv("DB_NAME")
    MYSQL_HOST = os.getenv("DB_HOST")
