# Generators in Python

def newGenerator():
    for i in range(1, 4):
        yield i # Yield is the generator operator

gen = newGenerator()

print(next(gen)) # Prints the first value of the generator loop
print(next(gen)) # Prints the second value of the generator loop
print(next(gen)) # Prints the third value of the generator loop
print(next(gen)) # Gives an Error because there is no fourth value in that loop

# The main difference between generators and simple functions is that simple function stores all the values in the memory and gives when requested. But generators don't use memory. They give each value one by one when requested.