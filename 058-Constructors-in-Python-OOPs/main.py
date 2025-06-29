# Constructors in Python(OOPs)

class Person:
    def __init__(self, name, occupation): # Constructor
        print("This will be defaultly displayed when a class is called") # 2 times
        self.name = name
        self.occ = occupation

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Kankon", "Student")
b = Person("Harry", "Developer")

a.info()
b.info()