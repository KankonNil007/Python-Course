# For Loops in Python

name = "Kankon"

for i in name:
    print(i, end=", ")
    if (i == "K"):
        print("The letter 'K' in my name")

print("\n\n")

# Nested For Loops

colors = ["Red", "Blue", "Green", "Yellow"]

for color in colors:
    print(color)
    for i in color:
        print(i)

print("\n\n")

# Range Numbers in For Loops

for k in range(5):
    print(k + 1)

for i in range(1, 11):
    print(i)

for k in range(1, 20, 3):
    print(k)