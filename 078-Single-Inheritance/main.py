# Single Inheritance in Python(OOPs)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def makeSound(self):
        print("Sound made by the Animal")

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def makeSound(self):
        print("Bark!!!")

class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def makeSound(self):
        print("Meow!!!")

a = Animal("Tom", "Mulder")
a.makeSound()

b = Dog("Tom", "Mulder")
b.makeSound()

c = Cat("Erry", "Persian")
c.makeSound()