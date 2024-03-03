import logging
import re

def read_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()  # Read the entire file into a string
            
            # Use regular expression to match the patterns for jokes and punchlines
            joke_punchline_pairs = re.findall(r'(.+?)[?.!] (.+)', text)
            
            # Separate the jokes and punchlines into two lists
            jokes, punchlines = zip(*joke_punchline_pairs)
            
            # Join the jokes and punchlines using newline characters
            jokes_with_newlines = '\n'.join(jokes)
            punchlines_with_newlines = '\n'.join(punchlines)
            
            print("Jokes:")
            print(jokes_with_newlines)
            print("\nPunchlines:")
            print(punchlines_with_newlines)
            
    except FileNotFoundError:
        print("File not found.")

def main():

    filename = "Jokes.txt"
    read_text_file(filename)

if __name__ == "__main__":
    main()