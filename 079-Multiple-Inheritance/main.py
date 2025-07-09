# Multiple Inheritance in Python(OOPs)

class Employee:
    def __init__(self, name):
        self.name = name

    def showName(self):
        print(f"The name is {self.name}")

class Gamer:
    def __init__(self, games):
        self.games = games

    def showGames(self):
        print(f"The Games are {self.games}")

class Person(Employee, Gamer): # M I
    def __init__(self, name, games):
        self.name = name
        self.games = games

a = Person("Kankon", "Clash of Clans")
print(a.name)
print(a.games)
a.showGames()
a.showName()