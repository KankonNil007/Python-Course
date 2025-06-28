# Word Frequency Counter (File IO + Functions)

# Goal: Read a .txt file, count how often each word appears, and write the results to a new file.

# 🔧 Concepts:

# read(), split(), map(), lambda, file.write()


txtfile = open("ChatGPT-Exercises/File-IO-Lambda-and-Functions/Word-Frequency-Counter/newtext.txt", "r")

textInside = txtfile.read()

char1 = ",.?!'%#@"

for i in char1:
    textInside = textInside.replace(i, "")

textInside = textInside.lower()

textInside = textInside.split()

frequency = {}

for word in textInside:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("Word Frequency List:")

for word, count in frequency.items():
    print(f"{word} = {count} time(s)")