# Personal Expense Tracker

from datetime import datetime

balance = 5000

def addIncome():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%d-%m-%Y %H:%M:%S")

    inpAmnt = int(input("Enter Amount(In Numbers): "))
    inpNote = input("Enter your Note: ")

    with open("Completion-Projects/Personal-Expense-Tracker/transactions.txt", "a+") as file:
        file.seek(0)
        contents = file.read()
    
        if contents:
            file.write("\n")
        file.write(f"Income - {inpAmnt}$ - {inpNote} - {current_time}")

    global balance
    balance = balance + inpAmnt

    print("New Income Added!!")

    choiceList()

def addExpense():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%d-%m-%Y %H:%M:%S")

    inpAmnt = int(input("Enter Amount(In Numbers): "))
    inpNote = input("Enter your Note: ")

    global balance

    if (inpAmnt > balance):
        print("Not Enough Money!!")
        addExpense()

    balance = balance - inpAmnt

    with open("Completion-Projects/Personal-Expense-Tracker/transactions.txt", "a+") as file:
        file.seek(0)
        contents = file.read()
    
        if contents:
            file.write("\n")
        file.write(f"Expense - {inpAmnt}$ - {inpNote} - {current_time}")

    print("New Expense Added!!")

    choiceList()

def viewBalance():
    print(f"Your Balance is: {balance}$")
    choiceList()

def viewHistory():
    print("--------Transactons---------")
    print("Type - Amount - Note - Date_Time")
    with open("Completion-Projects/Personal-Expense-Tracker/transactions.txt", "r") as file:
        for line in file:
            print(line, end="")
    print("\n")
    choiceList()

def screenView():
    print("========== Expense Tracker ==========")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View History")
    print("5. Delete History")
    print("6. Exit")
    print("-------------------------------------")

def choiceList():
    inpChoice = int(input("Enter your Choice: "))

    if (inpChoice == 1):
        addIncome()
    elif (inpChoice == 2):
        addExpense()
    elif (inpChoice == 3):
        viewBalance()
    elif (inpChoice == 4):
        viewHistory()
    elif (inpChoice == 5):
        with open("Completion-Projects/Personal-Expense-Tracker/transactions.txt", "w") as file:
            file.write("")

        print("History Deleted!!")
        choiceList()
    elif (inpChoice == 6):
        print("Program Ended Successfully!!")
    else:
        print("Invalid Choice!!!")
        choiceList()

screenView()
choiceList()