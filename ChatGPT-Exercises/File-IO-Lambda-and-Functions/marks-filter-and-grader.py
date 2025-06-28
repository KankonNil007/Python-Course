# 3. Marks Filter & Grader

# Goal: Use filter() and map() to select passing students and calculate grades.

# 🔧 Concepts:

# lambda, map, filter, reduce, local variables

inpList = input("Enter numbers separated by spaces: ")

inpList2 = list(map(int, inpList.split()))

passedStudents = list(filter(lambda x: x>=60 and x <= 100, inpList2))

def grades(x):
    if (x >= 80):
        return "A"
    elif (x < 80 and x >= 70):
        return "B"
    elif (x < 70 and x >= 60):
        return "C"
    
GradesList = list(map(grades, passedStudents))

from functools import reduce

averageMarks = reduce(lambda x,y: (x + y)/2, inpList2)

print("Here is the Details:")

print(f"Passed: {passedStudents}")
print(f"Grades: {GradesList}")
print(f"Average Marks: {averageMarks}")