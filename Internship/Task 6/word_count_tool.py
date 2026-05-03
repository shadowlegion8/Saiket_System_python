# ==========================================
# Internship Task 6 : Word Count Tool

# Import Counter for word frequency counting
from collections import Counter

# Display heading
print("===== Word Count Tool =====")

# Take text file name from user
file_name = input("Enter Text File Name (example: sample.txt): ")

try:
    # Open file in read mode
    with open(file_name, "r", encoding="utf-8") as file:
        # Read complete file content
        text = file.read()

    # Count total characters
    characters = len(text)

    # Split text into lines and count lines
    lines = text.splitlines()
    line_count = len(lines)

    # Convert text to lowercase and split into words
    words = text.lower().split()

    # Count total words
    word_count = len(words)

    # Count frequency of each word
    frequency = Counter(words)

    # Display results
    print("\n===== Analysis Result =====")
    print("Total Lines      :", line_count)
    print("Total Words      :", word_count)
    print("Total Characters :", characters)

    # Display most common words
    print("\n===== Top 10 Most Common Words =====")
    for word, count in frequency.most_common(10):
        print(f"{word} : {count}")

# If file does not exist
except FileNotFoundError:
    print("File not found! Please check file name.")

# Handle any other errors
except Exception as e:
    print("Error:", e)