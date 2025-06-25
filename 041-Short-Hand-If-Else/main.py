# Short Hand If Else Statements

a = 34
b = 69

# Standard If-Else
if (a > b):
    print("A")
elif (a == b):
    print("AB")
else:
    print("B")

# ShortHand If-Else
print("A") if a > b else print("AB") if a == b else print("B")

print(6) if b > a else "" # You have to put an else statement if there isn't one just keep it blank like above.

# Another Example

c = 5 if a > b else 0
print(c)