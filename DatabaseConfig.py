import os
import mysql.connector
import logging

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Connect to the database
def connect_to_database():
    try:
        db_connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        db_cursor = db_connection.cursor()
        return db_cursor, db_connection
    
    except Exception as e:
        logging.error(f'There was a problem connecting to the database {e}')