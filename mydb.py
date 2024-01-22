import mysql.connector

import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

# (1)
env_filename = '.env'
dotenv_path = join(dirname(__file__), env_filename)
load_dotenv(dotenv_path)

# (2)
# load_dotenv(find_dotenv())

dataBase = mysql.connector.connect(
    host = os.environ.get('DB_HOST'),
    user = os.environ.get('DB_USER'),
    passwd = os.environ.get('DB_PASSWORD'),
)

dataBase_name = os.environ.get('DB_NAME')

cursorObject = dataBase.cursor()

if dataBase_name:
    # try-except in Python (https://stackoverflow.com/a/6817677)
    try:
        cursorObject.execute(f'CREATE DATABASE IF NOT EXISTS {dataBase_name}')
        print('Database was successfully created!')
    except KeyboardInterrupt:
        print('Database creation was cancelled due to Keyboard interrupt')
    except Exception as e:
        print('Something went wrong while attempting to create a database, try again')
        print(f'potential error: {e}')
else:
    print('[x] Database name is not provided')
