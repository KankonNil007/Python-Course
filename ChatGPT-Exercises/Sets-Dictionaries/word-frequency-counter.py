# Word Frequency Counter

# Topics used: dictionaries, f-strings, docstrings

# Task:
# Input a paragraph from the user and count the frequency of each word.

def count_word_frequency(text):
    """
    Takes a string input and returns a dictionary with word frequencies.
    Words are case-insensitive and punctuation is ignored.
    """
    # Remove punctuation (basic way)
    for char in "-.,!?":
        text = text.replace(char, "")
    
    text = text.lower()  # Make it case-insensitive
    words = text.split()

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Input paragraph
paragraph = input("Enter a paragraph:\n")

# Count frequency
result = count_word_frequency(paragraph)

# Print results
print("\n📊 Word Frequency:\n")
for word, count in result.items():
    print(f"{word:<15} ➤ {count} time(s)")
