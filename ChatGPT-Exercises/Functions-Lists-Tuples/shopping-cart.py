# Shopping Cart Basic - Python

# Topics: Lists, Functions

# What it does:
# Let the user add items to a cart and view the cart.

Cart = []

def addItem():
    addIt = input("Enter Item: ")
    Cart.append(addIt)
    print("Item Added!\n\n")

    choiceList()

def viewCart():
    print("Your Cart:", Cart)
    print("\n")

    choiceList()

def screenView():
    print("1. Add Item")
    print("2. View Cart")
    print("3. Exit")



def choiceList():
    inpChoice = int(input("Enter Choice: "))

    if (inpChoice == 1):
        addItem()
    elif (inpChoice == 2):
        viewCart()
    elif (inpChoice == 3):
        print("Program Ended Successfully")
    else:
        print("Invalid Choice!!!")
        choiceList()

screenView()
choiceList()