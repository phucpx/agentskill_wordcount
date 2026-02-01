import sys
import os

def count_words(file_path):
    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        print(f"Total words: {len(words)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_words.py <file_path>")
    else:
        count_words(sys.argv[1])

