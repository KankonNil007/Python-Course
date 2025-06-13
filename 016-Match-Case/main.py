# Match Case using Python

num = int(input("Enter your Number :"))

match num:
    case 0:
        print("The number is Zero")
    case 10:
        print("The Number is 10")
    case _ if num > 10:
        print(num, "is greater than 10")
    case _:
        print("The number is ", num)