# Exception Handling in Python

a = input("Enter a Number: ")
print(f"The Multiplication Table of {a} is:")

try:
    for i in range(1, 11):
        print(f"{a} X {i} = {int(a) * i}")
except:
    print("Invalid Input!!!!")

print("Program Ended Successfully")

# There are many types errors: ValueError, IndexError

try:
    b = int(input("Enter an integer: "))
    b2 = [4, 5, 6]
    print(b2[b])
except ValueError: # Gives error if input is not what it needs
    print("Number is not an Integer!")
except IndexError: # gives error if index of a list is passed its limit
    print("List Indexing Error")


# Error: NameError

try:
  x = 5
  del x
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")