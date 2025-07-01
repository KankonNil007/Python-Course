# Instance Variables and Class Variables in Python(OOPs)

class Employee:
    companyName = "Apple" # Class Variable
    noOfEmployees = 0

    def __init__(self, name):
        self.name = name # Instance Variable
        self.amount = 0.02 # Instance Variable
        Employee.noOfEmployees += 1

    def showDetails(self):
        print(f"{self.name} works in {Employee.noOfEmployees} sized {self.companyName} and his amount is {self.amount}")

Employee.companyName = "Microsoft" # Class Variables can be changed directly for all

emp1 = Employee("Kankon")
emp1.amount = 0.6
emp1.companyName = "Google" # Class Variables can be changed inside an instance
emp1.showDetails()
emp2 = Employee("Sagor")
emp2.showDetails()