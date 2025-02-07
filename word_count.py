def count_word_occurrences(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print(f"Content of the file: {content}")  # Debugging statement

        content = content.lower()
        import string
        for char in string.punctuation:
            content = content.replace(char, " ")
        words = content.split()
        print(f"Words list: {words}")  # Debugging statement

        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

        sorted_word_counts = dict(sorted(word_counts.items()))
        print("Word counts in alphabetical order:")
        for word, count in sorted_word_counts.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: The specified file does not exist. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    file_path = 'example.txt'  # Adjust file name/path if needed
    count_word_occurrences(file_path)
