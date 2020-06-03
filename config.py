import os
import psycopg2
from sqlalchemy import create_engine
#from sqlalchemy import create_engine
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
create_engine("postgres+psycopg2://postgres:bianca1980@localhost:5432/fyyur")
SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:bianca1980@localhost:5432/fyyur'
