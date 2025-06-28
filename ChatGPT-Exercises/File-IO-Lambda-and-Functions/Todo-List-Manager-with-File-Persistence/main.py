# Todo List Manager with File Persistence
    
# Goal: Create a console app that adds, removes, and lists tasks from a file (todo.txt).

# 🔧 Concepts:

# readline(), truncate(), seek(), file.writelines(), global list of tasks. 

txtFile = open("ChatGPT-Exercises/File-IO-Lambda-and-Functions/Todo-List-Manager-with-File-Persistence/todo.txt", "r")

def viewList():
    txtFile2 = open("ChatGPT-Exercises/File-IO-Lambda-and-Functions/Todo-List-Manager-with-File-Persistence/todo.txt", "r")
    i = 0
    while True:
        i = i + 1
        line = txtFile2.readline()
        if not line:
            break
        print(f"{i}. {line}")

    choiceList()

def addTask():
    inpTask = input("Enter Task: ")

    txtFile2 = open("ChatGPT-Exercises/File-IO-Lambda-and-Functions/Todo-List-Manager-with-File-Persistence/todo.txt", "a")

    txtFile2.write(f"{inpTask}\n")
    txtFile2.close()

    print("Task Added!!\n")

    choiceList()

def removeTask():
    inptask = input("Enter Task to Remove: ")

    txtFile2 = open("ChatGPT-Exercises/File-IO-Lambda-and-Functions/Todo-List-Manager-with-File-Persistence/todo.txt", "r")

    lines = txtFile2.readlines()

    lines_to_keep = []
    line_to_remove = inptask
    for line in lines:
        if line.strip('\n') != line_to_remove:
            lines_to_keep.append(line)

    with open("ChatGPT-Exercises/File-IO-Lambda-and-Functions/Todo-List-Manager-with-File-Persistence/todo.txt", "w") as f:
        f.writelines(lines_to_keep)

    print("Task Removed!\n")

    choiceList()

def screenView():
    print("1. View List")
    print("2. Add Tasks")
    print("3. Remove Tasks")
    print("4. Exit")
    print("\n")

def choiceList():
    inpChoice = int(input("Enter Your Choice: "))

    if (inpChoice == 1):
        viewList()
    elif(inpChoice == 2):
        addTask()
    elif (inpChoice == 3):
        removeTask()
    elif (inpChoice == 4):
        print("Program Ended Successfully!")
    else:
        print("Invalid Choice!!!")
        choiceList()

screenView()
choiceList()