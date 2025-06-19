# For Loop with Else in Python

for i in range(1,6):
    print(i)
else:
    print("Loop has Ended")

# Else statement is printed if the loop in excecuted successfully. If the loop breaks at some point, it will not go through Else statement. Also, it doesn't work for endless loops. 

for i in range(1,6):
    print(i)
    if (i == 4):
        break
else:
    print("Loop has Ended")

# You can also try with while loop

i = 1
while (i < 7):
    print(f"This is number {i}")
    i = i + 1
    if (i == 6):
        break
else:
    print("Loop Ended Successfully")