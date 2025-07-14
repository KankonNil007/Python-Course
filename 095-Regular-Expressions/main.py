# Regular Expressions in Python

import re

searchWord = "is"
paragraph = """
Wikiversity is a Wikimedia Foundation project devoted to learning resources, learning projects, and research for use in all levels, types, and styles of is education from pre-school to university, including professional Mikiversity training and informal learning. We invite teachers, students, and researchers to join us in creating open educational resources and collaborative Sikiversity  learning communities. To learn is more about Wikiversity, try a guided tour, learn about adding content, or start editing now.
"""

Word = re.search(searchWord, paragraph) # Finds the first result
print(Word)

# What if you want all eearched items

Word2 = "is"
word3 = re.finditer(Word2, paragraph) # iterable

for word in word3:
    print(word)

# You can do it for a sequence

word4 = r"[A-Z]+ikiversity"
word5 = re.finditer(word4, paragraph)

for word in word5:
    print(word)

# Email Checker

email = "kankonmondolpekka123@gmail.com"
patternEmail = r"\w+@+\w+.+\w"

matcher = re.match(patternEmail, email)
print(matcher)