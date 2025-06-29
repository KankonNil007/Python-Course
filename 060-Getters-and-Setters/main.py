# Getters and Setters in Python(OOPs)

class myClass1:
    def __init__(self, value):
        self.numb = value

    def show(self):
        print(f"The Value is {self.numb}")

    @property # Getter
    def multiplication(self):
        return 10 * self.numb
    
    @multiplication.setter # Setter
    def multiplication(self, newValue):
        self.numb = newValue / 10

obj1 = myClass1(10)
obj1.multiplication = 88
print(obj1.multiplication)
obj1.show()