# MultiLevel Inheritance in Python(OOPs)

class Person:
    def __init__(self, name, prof):
        self.name = name
        self.prof = prof

    def showDetails(self):
        print(f"Name: {self.name}")
        print(f"Profession: {self.prof}")

class Employee(Person):
    def __init__(self, name, type):
        Person.__init__(self, name, prof="Employee")
        self.type = type

    def showDetails(self):
        Person.showDetails(self)
        print(f"Job: {self.type}")

class Programmer(Employee):
    def __init__(self, name, lang):
        Employee.__init__(self, name, type="Programmer")
        self.lang = lang

    def showDetails(self):
        Employee.showDetails(self)
        print(f"Programming Language: {self.lang}")

a = Programmer("Kankon", "Python")
a.showDetails()