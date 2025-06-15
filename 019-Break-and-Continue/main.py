# Break and Continue in Python

# Break Function in Loops

for i in range(1, 21):
    print("5 X",i ,"=", 5 * i)
    if (i == 10):
        break # break stops a loop in a certain value
print("Loop is broken successfully.")

# Continue Function in Loops

for i in range(5, 16):
    if (i == 10):
        print("We skip the 10")
        continue # Continue skips the value in the loop
    print("7 X", i,"=", 7 * i)
print("Value 10 is removed from the multiplication table\n\n")

# Do While Loops [from Previous Lesson]

i = 1
while True: # Infinte Loop
    print(i)
    i = i + 1
    if (i % 100 == 0):
        break