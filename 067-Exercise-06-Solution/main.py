# Exercise 06 - Solution

class Library:
    def __init__(self):
        self.bookNum = 2
        self.bookList = ["The Horizon of Universe", "Importance of Perseverence"]

    def addBook2(self, bookName):
        self.bookList.append(bookName)
        self.bookNum = self.bookNum + 1

a = Library()

c = a.bookList

def showBookList():
    print("Book List:")

    if (len(c) > 0):
        for k, i in enumerate(c, start=1):
            print(f"{k}. {i}")
    else:
        print("No Books!!")

    choiceList()

def bookNum2():
    print(f"The Total Number of Books is: {a.bookNum}")
    choiceList()

def addBook():
    inpBook = input("Enter the Book Name: ")

    a.addBook2(inpBook)

    print("Book Added!!")
    choiceList()

def screenView():
    print("1. Show Book List")
    print("2. Show Total Number of Books")
    print("3. Add a book")
    print("4. Exit")

def choiceList():
    inpChoice = int(input("Enter Your Choice: "))

    if (inpChoice == 1):
        showBookList()
    elif (inpChoice == 2):
        bookNum2()
    elif (inpChoice == 3):
        addBook()
    elif (inpChoice == 4):
        print("Program Ended Successfully")
    else:
        print("Invalid Choice!!!!")
        choiceList()

screenView()
choiceList()