# Static Method in Python(OOPs)

class Kankon:
    def __init__(self, num):
        self.num = num

    def display(self, num2):
        self.num = self.num + num2

    @staticmethod # 
    # Static method can be called without creating an instance of the class
    # It is used when you want to perform a function that does not require access to any Method or property of the class.
    def add(num3, num4):
        return num3 + num4
    
a = Kankon(10)
print(a.num)  # Output: 10
a.display(5)
print(a.num)  # Output: 15

print(Kankon.add(5, 20))  # Output: 25
# You can also call the static method without creating an instance of the class