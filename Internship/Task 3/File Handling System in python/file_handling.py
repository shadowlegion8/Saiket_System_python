try:
    file_name = "sample.txt"

    # Step 1: Create and write data to file
    with open(file_name, 'w') as file:
        file.write("Python is easy to learn.\n")
        file.write("Python is powerful.\n")
        file.write("I love Python.\n")

    # Step 2: Read file
    with open(file_name, 'r') as file:
        content = file.read()

    print("Original Content:\n")
    print(content)

    # Step 3: Take input
    old_word = input("Enter word to replace: ")
    new_word = input("Enter new word: ")

    # Step 4: Replace words
    modified_content = content.replace(old_word, new_word)

    # Step 5: Write updated content
    with open(file_name, 'w') as file:
        file.write(modified_content)

    print("\nModified Content:\n")
    print(modified_content)

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected Error:", e)