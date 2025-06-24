# Guess the Number – Cheat Detector

# Concepts: for-else, try-except, raise

# 📝 Task:

# Let the user guess a number in 5 tries.

# If they guess it right, break.

# If all attempts fail, show "Better luck next time!" using else with for.

# If user enters anything that’s not a number, catch it with try-except.

# If user enters a number outside 1–100, raise a ValueError.

numToBeGuessed = 13

for i in range(1, 6):
    try:
        guessNumb = int(input("Guess the Number: "))

        if (guessNumb == numToBeGuessed):
            print("Well, You have Guessed the Number.")
            break
        else:
            print("Wrong Number. Try Again!!")
    except ValueError:
        print("Not a Number!!!")

else:
    print("Better Luck Next Time!")