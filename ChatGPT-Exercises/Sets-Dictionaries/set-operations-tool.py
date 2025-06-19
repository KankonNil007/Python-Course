# Set Operations Tool

# Topics used: sets

# Create a program to perform:
# Union
# Intersection
# Difference
# Between two sets taken as user input.

inp1 = input("Enter first Set(Separed by commas): ")
inp2 = input("Enter second Set(Separed by commas): ")

list1 = inp1.split(",")
list2 = inp2.split(",")

set1 = set(list1)
set2 = set(list2)

print("\n")

def union():
    set3 = set1.union(set2)
    print(f"Union: {set3}")
    print("\n")

    ChoiceList()

def intersection():
    set3 = set1.intersection(set2)
    print(f"Intersection: {set3}")
    print("\n")

    ChoiceList()

def difference():
    set3 = set1.difference(set2)
    print(f"Difference (A - B): {set3}")
    print("\n")

    ChoiceList()

def setOperation():
    print("1. Union")
    print("2. Intersection")
    print("3. Difference")
    print("4. Exit")

def ChoiceList():
    inpChoice = int(input("Enter Choice: "))

    if (inpChoice == 1):
        union()
    elif (inpChoice == 2):
        intersection()
    elif (inpChoice == 3):
        difference()
    elif (inpChoice == 4):
        print("Program Closed Successfully.")
    else:
        print("Invalid Choice!!!!!")
        print("\n")
        ChoiceList()

setOperation()
ChoiceList()