# To-Do List Manager

def addTask():
    inpTask = input("Enter the Task: ")

    with open('Completion-Projects/To-Do-List-Manager/tasks.txt', 'a') as file:
        file.write(f"\n{inpTask}")

    print("Task Added!!")
    choiceList()

def markTask():
    with open('Completion-Projects/To-Do-List-Manager/tasks.txt', 'r') as file:
        for n, line in enumerate(file, start=1):
            print(f"{n}. {line.strip()}")

    inpChoice = int(input("Enter the Task Number: "))

    with open("Completion-Projects/To-Do-List-Manager/tasks.txt", "r") as file:
        lines = file.readlines()

    if (inpChoice < 1 or inpChoice > len(lines)):
        print("Line is out of Range")
        choiceList()
    
    if (lines[inpChoice - 1].endswith(" - Completed\n")):
        print("Task is Already Completed")
        choiceList()
    
    lines[inpChoice - 1] = lines[inpChoice - 1].rstrip("\n") + " - Completed\n"

    with open("Completion-Projects/To-Do-List-Manager/tasks.txt", "w") as file:
        file.writelines(lines)

    print("Task Marked as Completed!!!")
    choiceList()

def viewTasks():
    with open('Completion-Projects/To-Do-List-Manager/tasks.txt', 'r') as file:
        for n, line in enumerate(file, start=1):
            print(f"{n}. {line.strip()}")

    choiceList()

def deleteTask():
    with open('Completion-Projects/To-Do-List-Manager/tasks.txt', 'r') as file:
        for n, line in enumerate(file, start=1):
            print(f"{n}. {line.strip()}")

    inpChoice = int(input("Enter the Task Number: "))

    with open("Completion-Projects/To-Do-List-Manager/tasks.txt", "r") as file:
        lines = file.readlines()

    if (inpChoice < 1 or inpChoice > len(lines)):
        print("Line is out of Range")
        choiceList()
    
    lines.pop(inpChoice - 1)

    with open("Completion-Projects/To-Do-List-Manager/tasks.txt", "w") as file:
        file.writelines(lines)

    print("Task Deleted!!!")
    choiceList()
    

def screenView():
    print("========== To-Do List ==========")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Tasks")
    print("4. Delete Task")
    print("5. Exit")
    print("-------------------------------------")

def choiceList():
    inpChoice = int(input("Enter your Choice: "))

    if (inpChoice == 1):
        addTask()
    elif (inpChoice == 2):
        markTask()
    elif (inpChoice == 3):
        viewTasks()
    elif (inpChoice == 4):
        deleteTask()
    elif (inpChoice == 5):
        print("Program Ended Successfully!!")
    else:
        print("Invalid Choice!!!")
        choiceList()

screenView()
choiceList()