# Inheritance in Python(OOPs)

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id =id
        
    def showDetails(self):
        print(f"ID {self.id} is {self.name}")

class Programmer(Employee): #Inheritance
    def showLang(self):
        print("The Lanuage is Python")


a1 = Employee("Kankon Nil", 445)
a2 = Programmer("Sumon Nil", 446)

a1.showDetails()
a2.showDetails()
a2.showLang()