# dir(), "__dict__" and help() Methods in Python(OOPs)

# dir() method

list1 = [1, 2, 3]
print(dir(list1)) # dir method prints out how many methods and attributes we can use in list1
print(list1.__add__)

tuple1 = (1, 2, 3)
print(dir(tuple1))

# "__dict__" attribute

class Person:
    def __init__(self, name, income):
        self.name = name
        self.income = income
        self.version = 1.4

a = Person("Kankon", "40000")
print(a.__dict__) # It tells you what variables and values are there in a class as dictionary format

# help() method 

class Person:
    def __init__(self, name, income):
        self.name = name
        self.income = income
        self.version = 1.4

a = Person("Kankon", "40000")
print(help(a)) # Help method tells what you can do with a class or variable with some instructions