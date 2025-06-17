# Even or Odd Number Checker using If-Else Conditions

print("EVEN - ODD CHECKER")

num = int(input("Enter you Number: "))

if (num % 2 == 0):
    print(num, "is a EVEN Number")
elif (num % 2 != 0):
    print(num, "is a ODD Number")
else:
    print("Invalid Number")