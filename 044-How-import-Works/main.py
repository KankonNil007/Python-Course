# How import Works in Python

# Directly importing a module
import math

math1 = math.floor(4.763462)
math2 = math.sqrt(10)

print(math1, math2)

# You can also import certain functions from a module
from math import sqrt, pi

math3 = sqrt(64)
math4 = pi

print(math3, math4)

# You can also import everything from a module though it is not recommended
# from math import *


# The as keyword
# This enables modules to be called whatever defined in the as keyword also available for module functions

import math as meth

print(meth.sqrt(9))

from math import sqrt as st, pi as pie

print(st(45) * pie)


# The dir function in a module
# Prints out all the functions and variables in a module

import math

print(dir(math))


# You can also import a whole another file

from kankon import welcome, kankon5

welcome()
print(kankon5)