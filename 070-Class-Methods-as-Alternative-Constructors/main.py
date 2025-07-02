# Class Methods as Alternative Constructors - Python(OOPs)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        name , salary = string.split("-")
        return cls(name, int(salary))

a = Employee("Kankon", 12000)
print(a.name)
print(a.salary)

string2 = "Sagor-22000" # Suppose, you have to convert this and commit to the Employee class

a2 = Employee.fromStr(string2)
print(a2.name)
print(a2.salary)
