# Class Methods in Python(OOPs)

class Employee:
    company = "Apple" # Class Variable

    def __init__(self, name):
        self.name = name

    def showDetails(self):
        print(f"I am {self.name} and I work in {self.company}")

    @classmethod # If you wanna change the class variable use classmethod
    def changeComp(cls, newComp):
        cls.company = newComp

a = Employee("Kankon")
a.showDetails()
a.changeComp("Google")
a.showDetails()
print(Employee.company)


