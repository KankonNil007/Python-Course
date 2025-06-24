# Exercise 04 - Encode, Decode Program

import random
import string

def encode():
    text = input("Enter Text to Encrypt: ")

    for char in ",.!?:;":
        text = text.replace(char, "")

    words = text.split()
    newWords = []

    for word in words:
        if (len(word) >= 3):
            word = word + word[0]
            word = word[1:len(word)]
            Char = string.ascii_letters
            ranChar1 = "".join(random.choices(Char, k=3))
            ranChar2 = "".join(random.choices(Char, k=3))
            word = ranChar1 + word + ranChar2
        else:
            word = word[::-1]

        newWords.append(word)

    NewText = " ".join(newWords)

    print(f"Encrypted Text: {NewText}")
    print("\n")
    choiceList()

def decode():
    text = input("Enter Text to Decrypt: ")

    for char in ",.!?:;":
        text = text.replace(char, "")

    words = text.split()
    newWords = []

    for word in words:
        if (len(word) >= 3):
            word = word[3:len(word) - 3]
            word = word[len(word) - 1] + word
            word = word[0:len(word) - 1]
        else:
            word = word[::-1]

        newWords.append(word)

    newText = " ".join(newWords)
    print(f"Decrypted Text: {newText}")
    print("\n")
    choiceList()

def screenView():
    print("1. Encoder")
    print("2. Decoder")
    print("3. Exit")
    print("\n")

def choiceList():
    inpChoice = int(input("Enter your Choice: "))

    if (inpChoice == 1):
        encode()
    elif (inpChoice == 2):
        decode()
    elif ( inpChoice == 3):
        print("Program Closed Successfully")
    else:
        print("Invalid Choice!!!!!")
        choiceList()

screenView()
choiceList()