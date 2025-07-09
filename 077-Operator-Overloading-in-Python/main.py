# Operator Overloading in Python(OOPs)

class Vector():
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self, newVec):
        return f"The Summation of Vectors: {Vector(self.i + newVec.i, self.j + newVec.j, self.k + newVec.k)}"
    
    def __sub__(self, newVec):
        return f"The Substraction of Vectors(A - B): {Vector(self.i - newVec.i, self.j - newVec.j, self.k - newVec.k)}"
    
a1 = Vector(3, 6, 2)
print(a1)
a2 = Vector(2, 5, 8)
print(a2)

# Adding two Vectors - Operator "+" will overload the class and print the "__add__" method
print(a1 + a2)
print(type(a1 + a2))

# Substracting Two Vectors
print(a1 - a2)