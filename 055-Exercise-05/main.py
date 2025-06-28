# Snake Water Gun Game - Exercise 05

print("Snake Water Gun Game")

inpChoice = input("Select Your Move: ")
inpChoice = inpChoice.capitalize()


import random

randomChoice = random.randint(1, 3)
computerMove = ""

if (randomChoice == 1):
    computerMove = "Snake"
elif (randomChoice == 2):
    computerMove = "Water"
elif (randomChoice == 3):
    computerMove = "Gun"

print(f"Computer Move: {computerMove}")

if (computerMove == inpChoice):
    print("Result: Match Tied!!")
elif (inpChoice == "Snake" and computerMove == "Water"):
    print("Result: You Win!")
elif (inpChoice == "Snake" and computerMove == "Gun"):
    print("Result: You Lose!")
elif (inpChoice == "Water" and computerMove == "Snake"):
    print("Result: You Lose!")
elif (inpChoice == "Water" and computerMove == "Gun"):
    print("Result: You Win!")
elif (inpChoice == "Gun" and computerMove == "Snake"):
    print("Result: You Win!")
elif (inpChoice == "Gun" and computerMove == "Water"):
    print("Result: You Lose!")
else:
    print("Invalid Move!!!!!")