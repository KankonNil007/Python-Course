# Read, Readlines Method and Other Methods in Python

# Readline Method: Prints line by line of a file

txtfile = open("050-Read-Readlines-and-Other-Methods/myfile.txt", "r")

while True:
    line = txtfile.readline()
    if not line:
        break
    print(line)

# File Handling using loop and readline method

txtfile2 = open("050-Read-Readlines-and-Other-Methods/myfile2.txt", "r")

i = 0
while True:
    i = i + 1
    line = txtfile2.readline()
    if not line:
        break
    s1 = int(line.split(",")[0])
    s2 = int(line.split(",")[1])
    s3 = int(line.split(",")[2])
    print(f"Marks of Student {i} of Maths is: {s1}")
    print(f"Marks of Student {i} of Science is: {s2}")
    print(f"Marks of Student {i} of ICT is: {s3}")


# Writeline method: Writes or overwrites multiple lines in a file

txtfile3 = open("050-Read-Readlines-and-Other-Methods\myfile3.txt", "w")

lines = ['Hello Guys\n', 'This is Kankon\n', 'It is morning']
txtfile3.writelines(lines)
txtfile3.close()