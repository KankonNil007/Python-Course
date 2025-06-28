# File Comparison Tool

# Goal: Compare two .txt files line-by-line and print the differences.

# 🔧 Concepts:

# readline(), seek(), global/local variable usage

def mainFunc():
    with open("ChatGPT-Exercises/File-IO-Lambda-and-Functions/File-Comparison-Tool/txtfile1.txt", "r") as txt1:
        lines1 = txt1.readlines()

        newList1 = []

        for item in lines1:
            if isinstance(item, str):
                newList1.append(item.replace("\n", ""))
            else:
                newList1.append(item)


    with open("ChatGPT-Exercises/File-IO-Lambda-and-Functions/File-Comparison-Tool/txtfile2.txt", "r") as txt2:
        lines2 = txt2.readlines()

        newList2 = []

        for item in lines2:
            if isinstance(item, str):
                newList2.append(item.replace("\n", ""))
            else:
                newList2.append(item)

    for i, (newList1, newList2) in enumerate(zip(newList1, newList2), start=1):
        if newList1.strip() != newList2.strip():
            print(f"Line {i} is different:")
            print(f"File1: {newList1.strip()}")
            print(f"File2: {newList2.strip()}")



inpChoice = int(input("Enter 1 to begin the Comparison: "))

if (inpChoice == 1):
    mainFunc()
else:
    print("Invalid Choice!!")
