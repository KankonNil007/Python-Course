# Snake Water Gun - Solution

import random

user = int(input("Select 0 for Snake, 1 for Water and 2 for Gun: "))
comp = random.randint(0, 2)

def check(user, comp):
    if (user == comp):
        return 0
    elif (user == 0 and comp == 2):
        return -1
    elif (user == 1 and comp == 0):
        return -1
    elif (user == 2 and comp == 1):
        return -1
    else:
        return 1
    
result = check(user, comp)

print(f"You chose: {user}\nComputer chose: {comp}")

if (result == 0):
    print("It's a draw")
elif (result == 1):
    print("You Win!")
else:
    print("You Lose!")