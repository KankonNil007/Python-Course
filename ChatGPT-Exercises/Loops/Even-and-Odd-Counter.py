# Even and Odd Number Counter Using Loops 

"""

Take 5 numbers from the user. Count how many are even and how many are odd. Skip negative numbers using continue.

""" 

evenNum = 0
oddNum = 0

for i in range(1,6):
    num = int(input(f"Enter number {i}: "))

    if ( num < 0):
        continue
    
    if (num % 2 == 0):
        evenNum = evenNum + 1
    elif (num % 2 != 0):
        oddNum = oddNum + 1

print("Even:", evenNum)
print("Odd:", oddNum)
print("Negative numbers were skipped.")   