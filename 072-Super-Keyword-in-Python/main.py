# super Keyword in Python(OOPs)

class Parent:
    def parentMethod(self):
        print("You are inside Parent Class")

class Child(Parent):
    def childMethod(self):
        print("Hello Guys")
        super().parentMethod()

    def anoMeth(self):
        print("You are inside Child Class")
        super().parentMethod()

a = Child()

a.childMethod()
a.anoMeth()


# Another Example of super Keyword

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

a = Employee("Kankon Nil", 2343)
b = Programmer("Sagor Das", 4343, "Python")

print(b.name)
print(b.id)
print(b.lang)