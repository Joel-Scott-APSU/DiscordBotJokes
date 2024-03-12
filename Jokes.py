import re
from DatabaseConfig import connect_to_database
import os

db_cursor, db_connection = connect_to_database()

def read_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()  # Read the entire file into a string
            
            # Use regular expression to match the patterns for jokes and punchlines
            filename = os.path.basename(filename)
            if filename == '300RandomJokes.txt':
                joke_punchline_pairs = re.findall(r'\d+\. (.+?[?.!]) (.+)', text)
                table_name = 'alljokes'
            elif filename == 'DarkHumorJokes.txt':
                joke_punchline_pairs = re.findall(r'\d+\.\s*(.+)', text)
                table_name = 'darkhumor'
            else:
                print("Unknown filename. Data will not be inserted.")
                return
            
            # Iterate over each joke-punchline pair
            for joke, punchline in joke_punchline_pairs:
                # Check if the joke-punchline pair already exists in the database
                db_cursor.execute(f"SELECT * FROM {table_name} WHERE joke = %s AND punchline = %s", (joke, punchline))
                if not db_cursor.fetchall():
                    # If the pair doesn't exist, insert it into the database
                    db_cursor.execute(f"INSERT INTO {table_name} (joke, punchline) VALUES (%s, %s)", (joke, punchline))
                    db_connection.commit()
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"There was an error adding files to the database: {e}")

def read_jokes(table):
    db_cursor = db_connection.cursor()

    db_cursor.execute(f"SELECT * FROM {table} ORDER BY RAND() LIMIT 1")
    joke = db_cursor.fetchone()
    
    db_cursor.close()
    db_connection.close()

    return joke