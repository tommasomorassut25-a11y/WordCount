import tkinter as tk
from tkinter import filedialog

# =========================================================================================
# GUI FUNCTIONS
# =========================================================================================

# Function to open the file dialog and insert the path into the entry box
def browse_file():
    file_path = filedialog.askopenfilename(title="Select a .txt file", filetypes=[("Text files", "*.txt")])
    if file_path:  # If the user selected a file (and didn't click "Cancel")
        document_entry.delete(0, tk.END)  # Clear the text box
        document_entry.insert(0, file_path) # Insert the file path

# Bridge function: Reads the text box and safely starts the analysis
def start_analysis():
    current_path = document_entry.get()
    
    if current_path: 
        lbl_report.config(text="") # Clear old results
        analyze_text(current_path) # Call the analysis function

# =========================================================================================
# TEXT ANALYSIS FUNCTIONS
# =========================================================================================

def analyze_text(file_path):
    word_dictionary = {}
    total_letters = 0
    total_characters = 0
    total_punctuation = 0
    total_spaces = 0
    total_words = 0
    longest_word = ""
    shortest_word = ""
    most_frequent_word = ""

    punctuation_marks = ".,;:!?"

    # Added try/except block to avoid crashes if the file doesn't exist
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        lbl_report.config(text="Error: File not found. Check the path.")
        return

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

    if words:  
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
    
    # Print the report
    print_report(total_letters, total_spaces, total_punctuation, total_characters, total_words, longest_word, shortest_word, most_frequent_word)


def print_report(total_letters, total_spaces, total_punctuation, total_characters, total_words, longest_word, shortest_word, most_frequent_word):
    # Print to the console
    print(f"Total letters: {total_letters}")
    print(f"Total spaces: {total_spaces}")
    print(f"Total punctuation marks: {total_punctuation}")
    print(f"Total characters: {total_characters}")
    print(f"Total words: {total_words}")
    print(f"Longest word: {longest_word}")
    print(f"Shortest word: {shortest_word}")
    print(f"Most frequent word: {most_frequent_word}")

    # Write to the GUI
    report_text = (
        f"Total letters: {total_letters}\n"
        f"Total spaces: {total_spaces}\n"
        f"Total punctuation marks: {total_punctuation}\n"
        f"Total characters: {total_characters}\n"
        f"Total words: {total_words}\n"
        f"Longest word: {longest_word}\n"
        f"Shortest word: {shortest_word}\n"
        f"Most frequent word: {most_frequent_word}"
    )
    lbl_report.config(text=report_text)


# =========================================================================================
# PROGRAM START AND WINDOW CONSTRUCTION
# =========================================================================================
if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("Text Analyzer")
    root.geometry("450x350") # Sets a minimum size for the window

    frame = tk.Frame(root)
    frame.grid(padx=15, pady=15)

    document_label = tk.Label(frame, text="Select or enter the path of the .txt document:")
    document_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 5))
    
    document_entry = tk.Entry(frame, width=45)
    document_entry.grid(row=1, column=0, sticky="w")

    button_browse = tk.Button(frame, text="Browse", command=browse_file)
    button_browse.grid(row=1, column=1, padx=5)

    button_analyze = tk.Button(frame, text="Analyze", command=start_analysis, bg="lightblue")
    button_analyze.grid(row=2, column=0, columnspan=2, pady=15)

    lbl_report = tk.Label(frame, text="", justify="left", font=("Helvetica", 10))
    lbl_report.grid(row=3, column=0, columnspan=2, sticky="w")

    root.mainloop()