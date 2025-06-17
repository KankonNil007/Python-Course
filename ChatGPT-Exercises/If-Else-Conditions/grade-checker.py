# Grade Checker using If-Else Statements

print("GRADE CHECKER(USA VARIANT)")

gradeNum = int(input("Enter your Number Percentage(without %): "))

if (gradeNum >= 90 and gradeNum <= 100):
    print("You have got A+. Exellent!")
elif (gradeNum >= 80 and gradeNum < 90):
    print("You have got A. Very Good!")
elif (gradeNum >= 70 and gradeNum < 80):
    print("You have got B. Good Job!")
elif (gradeNum >= 60 and gradeNum < 70):
    print("You have got C. Needs Improvement!")
elif (gradeNum >= 0 and gradeNum < 60):
    print("You have got F. Better Luck Next Time!")
elif (gradeNum < 0 and gradeNum >= -100):
    print("You got Negative Numbers!!!!! HAHAHAHAHA")
elif (gradeNum > 100 or gradeNum < -100):
    print("Not a Valid Grade Number")
else:
    print("Not a Number")