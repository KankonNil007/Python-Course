# File IO in Python

# Read mode in file.IO: 'r' which is default
txtfile = open("049-File-IO-in-Python/kankon.txt", "r")
# print(txtfile)

txtread = txtfile.read()
print(txtread)
txtfile.close()

# Write mode : Creates a new file if the file doesn't exist, this will overwrite the file.

txtfile2 = open("049-File-IO-in-Python/kankon2.txt", "w")
txtfile2.write("Hello Guys!!")
txtfile2.close()

# Append Mode:  Creates a new file if the file doesn't exist, This will add certain value once the program is run. 

txtfile3 = open("049-File-IO-in-Python/kankon3.txt", "a")
txtfile3.write("Hello Guys\n") # I have run the program 5 times that means this text is written there 5 times
txtfile3.close()

# You Have to close the mode once it is used or else it will not work


# With Statement any mode ("r", "w", "a"). No Close Statement

with open("049-File-IO-in-Python/kankon.txt", "a") as txtfile4:
    txtfile4.write("\nI am inside with Statement!")