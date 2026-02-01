---
name: word-count
description: Count the number of words in a text file. Use this skill when the user wants to analyze or count words in a document or text file.
compatibility: Requires Python 3 installed.
---
# Word Count Skill

## When to use
Use this skill when the user wants to count words in a text file.

## Steps
1. Ensure the file path exists.
2. Run the script:
   scripts/count_words.py <file_path>
3. Return the word count result to the user.

## Example
Input:
scripts/count_words.py sample.txt

Output:
Total words: 125
