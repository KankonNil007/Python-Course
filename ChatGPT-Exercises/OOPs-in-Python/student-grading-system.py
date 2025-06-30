# Student Grading System

# Topics: Class, Object, Constructor, Getters/Setters

# 📝 Task:
# Create a Student class that:

# Takes name, roll, and marks as inputs.

# Uses a getter to show grade (A, B, C, F) based on marks.

# Uses a setter to update marks safely (0–100 only).

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    @property
    def showGrade(self):
        if (self.marks >= 80 and self.marks <= 100):
            return "A"
        elif (self.marks >= 70 and self.marks < 80):
            return "B"
        elif (self.marks >= 60 and self.marks < 70):
            return "C"
        elif (self.marks >= 0 and self.marks < 60):
            return "F"
        else:
            return "Invalid Grade Number!"
        
    @showGrade.setter
    def showGrade(self, newMarks):
        self.marks = newMarks

inpName = input("Enter Your Name: ")
inpRoll = int(input("Enter Your Roll: "))
inpMarks = int(input("Enter Your Marks: "))

a = Student(inpName, inpRoll, inpMarks)

print(f"Your Grade is: {a.showGrade}")

def updateMarks():
    inpUpMarks = int(input("Enter Updated Marks: "))

    a.showGrade = inpUpMarks

    print(f"Your Updated Grade: {a.showGrade}")

inpChoice = int(input("Enter 1 to Edit your marks or 2 to Exit: "))

if (inpChoice == 1):
    updateMarks()
elif (inpChoice == 2):
    print("Program Ended Successfully")
else:
    print("Invalid Input")