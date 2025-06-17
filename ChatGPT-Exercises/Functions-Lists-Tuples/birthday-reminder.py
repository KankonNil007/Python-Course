# Birthday Reminder

# Topics: Tuples, Lists, Functions

# What it does:
# Store and display names with birthdays.

birthdays = []

def addBirthday():
    tempList = []
    inpName = input("Enter Name: ")
    tempList.append(inpName)
    inpBDay = input("Enter Birthday: ")
    tempList.append(inpBDay)
    tempTuple = tuple(tempList)
    birthdays.append(tempTuple)
    print("Birthday Added!\n")

    choiceList()


def showBirthdayList():
    print("Birthday List:", birthdays)
    print("\n")

    choiceList()

def screenView():
    print("1. Add Birthday")
    print("2. Show Birthday List")
    print("3. Exit")

def choiceList():
    inpChoice = int(input("Enter Choice: "))

    if (inpChoice == 1):
        addBirthday()
    elif (inpChoice == 2):
        showBirthdayList()
    elif (inpChoice == 3):
        print("Program Ended Successfully")
    else:
        print("Invalid Choice!!!")
        choiceList()

screenView()
choiceList()