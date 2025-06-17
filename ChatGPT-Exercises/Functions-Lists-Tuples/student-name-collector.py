# Student Name Collector - Python

# Topics: Functions, Lists

# What it does:
# Takes names from user and stores them.

studentName = []

def addStudent():
    stdName = input("Enter Student Name: ")
    studentName.append(stdName)
    print("Student Added")

    choiceList()

def showList():
    print("Student List:", studentName)

    choiceList()

def showScreen():
    print("1. Add Student")
    print("2. Show List")
    print("3. Exit")

def choiceList():
    inpChoice = int(input("Enter Choice: "))

    if (inpChoice == 1):
        addStudent()
    elif (inpChoice == 2):
        showList()
    elif (inpChoice == 3):
        print("Program Ended Successfully!!")
    else:
        print("Invalid Choice!!!!")
        choiceList()

showScreen()
choiceList()