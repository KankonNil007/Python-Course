# Bank Account Manager

# Topics: Private Variables, Getters/Setters, Property Decorators

# 📝 Task:
# Create a BankAccount class where:

# __balance is a private variable.

# Balance can only be viewed using a @property getter.

# It has deposit(amount) and withdraw(amount) methods with rules:

# Cannot withdraw more than balance

# Deposit/withdraw only if amount > 0

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def depoFunds(self, amnt):
        if (amnt > 0):
            self.__balance = self.__balance + amnt
            return f"Deposit Successful!!\nNew Balance {self.__balance}"
        else:
            return "Invalid Funds!!"

    def withFunds(self, amnt):
        if (amnt > 0 and amnt < self.__balance):
            self.__balance = self.__balance - amnt
            return f"Withdraw Successful!!\nNew Balance {self.__balance}"
        else:
            return "Invalid Funds"

inpName = input("Enter Your Name: ")
inpBalance = int(input("Enter Initial Balance: "))

a = BankAccount(inpName, inpBalance)

def deposit():
    inptAmnt = int(input("Enter Deposit Amount: "))

    print(a.depoFunds(inptAmnt))

    choiceList()

def withdraw():
    inptAmnt = int(input("Enter Withdraw Amount: "))

    print(a.withFunds(inptAmnt))

    choiceList()

def show():
    print(f"Your Balance: {a._BankAccount__balance}")

    choiceList()

def nextView():
    print("1. Deposit Funds")
    print("2. Withdraw Funds")
    print("3. Show Balance")
    print("4. Exit")

def choiceList():
    inpChoice = int(input("Enter Your Choice: "))

    if (inpChoice == 1):
        deposit()
    elif (inpChoice == 2):
        withdraw()
    elif (inpChoice == 3):
        show()
    elif (inpChoice == 4):
        print("Program Ended Successfully")    
    else:
        print("Invalid Choice!!!!")
        choiceList()

nextView()
choiceList()