# Rock Paper Scissors using If-Else Conditions

print("Rock Paper Scissors Game")

userInput = input("Choose (Rock, Paper, Scissors): ")

computerInput = "Scissors"

if (userInput == "Rock" or userInput == "rock"):
    print("You Won")
elif (userInput == "Paper" or userInput == "paper"):
    print("You Lost")
elif (userInput == "Scissors" or userInput == "scissors"):
    print("Tie")
else:
    print("Input a valid Move")
