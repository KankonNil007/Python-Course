# is vs "==" (In Python)

a = 4
b = "4"

print(a is b) # Exact location of object in memory, Returns false
print(a == b) # value, Returns false

c = [4, 6, 10]
d = [4, 6, 10]

print(c is d) # List are changeable so it doesn't keep at the same memory
print(c == d)

e = 5
f = 5

print(e is f)
print(e == f)