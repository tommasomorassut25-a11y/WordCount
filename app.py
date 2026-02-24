# Create a Python program that analyzes the content of a text file
# and produces a detailed report.

# The program:
# - Asks the user for the path of a .txt file
# - Reads the file content
# - Analyzes the text
# - Prints a detailed report

file_path = input("Enter the path of the .txt document: ")

word_dictionary = {}

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

total_letters = 0
total_characters = 0
total_punctuation = 0
total_spaces = 0
total_words = 0
longest_word = ""
shortest_word = ""
most_frequent_word = ""

punctuation_marks = ".,;:!?"

# Count characters
for char in content:
    if char in punctuation_marks:
        total_punctuation += 1
    elif char == " ":
        total_spaces += 1
    else:
        total_letters += 1

total_characters = len(content)

# Split text into words
words = content.split()

if words:  # Avoid errors if file is empty
    shortest_word = words[0]

total_words = len(words)

# Find longest and shortest word
for word in words:
    clean_word = word.strip(punctuation_marks)

    if len(clean_word) > len(longest_word):
        longest_word = clean_word

    if len(clean_word) < len(shortest_word) and clean_word != "":
        shortest_word = clean_word

# Count word frequency
for word in words:
    clean_word = word.strip(punctuation_marks).lower()

    if clean_word in word_dictionary:
        word_dictionary[clean_word] += 1
    else:
        word_dictionary[clean_word] = 1

# Find most frequent word
max_value = 0

for key, value in word_dictionary.items():
    if value > max_value:
        most_frequent_word = key
        max_value = value

# Print report
print(f"Total letters: {total_letters}")
print(f"Total spaces: {total_spaces}")
print(f"Total punctuation marks: {total_punctuation}")
print(f"Total characters: {total_characters}")
print(f"Total words: {total_words}")
print(f"Longest word: {longest_word}")
print(f"Shortest word: {shortest_word}")
print(f"Most frequent word: {most_frequent_word}")