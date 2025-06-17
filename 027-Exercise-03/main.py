# Exercise 03 - Kaun Banega Crorepati

print("Here are your Questions:")

dict1 = { 
        "question": "What is the capital of India?",

        "options": ["A: Mumbai", "B: Delhi", "C: Kolkata", "D: Chennai"],

        "correct": "B" }

dict2 = {         
        "question": "Which planet is known as the Red Planet?",

        "options": ["A: Jupiter", "B: Venus", "C: Mars", "D: Mercury"],

        "correct": "C" }

dict3 = {         
        "question": "Who wrote the Indian National Anthem?",

        "options": ["A: Mahatma Gandhi", "B: Rabindranath Tagore", "C: Jawaharlal Nehru", "D: Subhas Chandra Bose"],

        "correct": "B" }

def function3():
    print(dict3["question"])
    for i in dict3["options"]:
        print(i)
    ans1 = input("Your Answer(A, B, C, D): ")
    if (ans1 == dict3["correct"]):
        print("Your Answer is Correct.\nYou have won the Game")
        print("Your winnings are $1000")
    else:
        print("Your Answer is Wrong. Game Over")

def function2():
    print(dict2["question"])
    for i in dict2["options"]:
        print(i)
    ans1 = input("Your Answer(A, B, C, D): ")
    if (ans1 == dict2["correct"]):
        print("Your Answer is Correct.\nHere is the next Question:")
        function3()
    else:
        print("Your Answer is Wrong. Game Over")

def function1():
    print(dict1["question"])
    for i in dict1["options"]:
        print(i)
    ans1 = input("Your Answer(A, B, C, D): ")
    if (ans1 == dict1["correct"]):
        print("Your Answer is Correct.\nHere is the next Question:")
        function2()
    else:
        print("Your Answer is Wrong. Game Over")

function1()