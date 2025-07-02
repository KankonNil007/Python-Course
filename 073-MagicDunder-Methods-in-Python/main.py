# Magic/Dunder Methods in Python

# __len__ Method:

from emp import Employee    

a = Employee("Kankon")

print(a.name)
print(len(a))

# __str__ Method

from emp import Employee

b = Employee("Sagor")
print(b)
print(str(b))

# __repr__ Method

from emp import Employee

c = Employee("Dheeman")
print(repr(c))

# __call__ Method

from emp import Employee

d = Employee("Tribindo")
d()