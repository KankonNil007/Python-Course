# Finally Keyword in Python

try:
    list1 = [2, 4, 5, 7, 9]
    inpNum = int(input("Enter an Index: "))
    print(list1[inpNum])
except:
    print("Some Error Occured!!!")
finally: # Prints always whether error occurs or not
    print("I am always executed.")

# Why should we use "Finally"

def func1():
    try:
        list1 = [2, 4, 5, 7, 9]
        inpNum = int(input("Enter an Index: "))
        print(list1[inpNum])
        return 1
    except:
        print("Some Error Occured!!!")
        return 0
    finally: # Prints always whether error occurs or not
        print("I am always executed.")
    print("I am always executed") # Can't execute

x = func1()
print(x)