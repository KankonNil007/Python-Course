# Grade Checker by Using Match Case

grade = input("Enter your grade (A-F):")

match grade:
    case "A":
        print("Excellent!")
    case "B":
        print("Very Good!")
    case "C":
        print("Good")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Failed")
    case _:
        print("Invalid Grade")
