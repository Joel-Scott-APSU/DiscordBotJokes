import re
from DatabaseConfig import connect_to_database

db_cursor, db_connection = connect_to_database()

def read_text_file(filename):
    try:
        print(filename)
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()  # Read the entire file into a string
            # Use regular expression to match the patterns for jokes and punchlines
            
            if filename == '300RandomJokes.txt':
                joke_punchline_pairs = re.findall(r'\d+\.\s*(.+?[?.!])\s*(.+)', text)
                table_name = 'alljokes'
                            # Iterate over each joke-punchline pair
                for joke, punchline in joke_punchline_pairs:
                    # Check if the joke-punchline pair already exists in the database
                    db_cursor.execute(f"SELECT * FROM {table_name} WHERE joke = %s AND punchline = %s", (joke, punchline))
                    if not db_cursor.fetchall():
                        # If the pair doesn't exist, insert it into the database
                        db_cursor.execute(f"INSERT INTO {table_name} (joke, punchline) VALUES (%s, %s)", (joke, punchline))
                        db_connection.commit()

            elif filename == 'DarkHumorJokes.txt':
                joke_punchline_pairs = re.findall(r'\d+\.\s*(.+)', text)
                table_name = 'darkhumor'
                
                for joke in joke_punchline_pairs:
                    db_cursor.execute(f"SELECT * FROM {table_name} WHERE JOKE = %s", (joke,))

                    if not db_cursor.fetchall():
                        db_cursor.execute(f'INSERT INTO {table_name} (joke) VALUES (%s)', (joke,))
                        db_connection.commit()

            else:
                print("Unknown filename. Data will not be inserted.")
                return
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"There was an error adding files to the database: {e}")

def read_random_jokes(table):
    db_cursor = db_connection.cursor()

    db_cursor.execute(f"SELECT joke, punchline FROM {table} ORDER BY RAND() LIMIT 1")
    joke_tuple = db_cursor.fetchone()

    joke = ' '.join([value.strip("'") for value in joke_tuple])

    return joke

def read_dark_jokes(table):
    db_cursor = db_connection.cursor()

    db_cursor.execute(f'SELECT joke FROM {table} ORDER BY RAND() LIMIT 1')
    new_joke = db_cursor.fetchone()

    joke = ' '.join([value.strip("'") for value in new_joke])

    return joke