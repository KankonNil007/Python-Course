# Classes and Objects in Python(OOPs)

# Defining a class
class Person:
    name = "Kankon"
    occupation = "Student"
    netWorth = 100

# Calling a class
a = Person()
print(a.name, a.occupation, a.netWorth)

# Change their value
a.name = "Madara Uchiha"
a.netWorth = 99999

print(f"{a.name} has {a.netWorth} dollars")


# self parameter in classes

class aboutMe:
    name = "Kankon"
    age = "19"
    def info(self):
        print(f"{self.name} is {self.age} years old.")

b = aboutMe()

b.info()

# Create Multiple Objects using a single Class

class fruit: # a class
    name = "Mango"
    price = 25
    def info(self):
        print(f"The Price of a {self.name} is: {self.price}$")

a = fruit() # a object
b = fruit() # a object
c = fruit() # a object

a.name = "Apple"
a.price = 15

b.name = "Banana"
b.price = 10

a.info() 
b.info()
c.info() # Stays at the default values as it is not changed