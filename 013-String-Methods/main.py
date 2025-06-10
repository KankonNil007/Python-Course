# String Methods In Python

name = "Kankon"

print(len(name)) # Shows the length of the String

print(name.upper()) # Turns our String Uppercase
print(name.lower()) # Turns our String Lowercase

"""
When we want to remove unnecessary symbols from our String, we use Rstrip method
"""

name2 = "Kankon007!!!!!!!!"

print(name2.rstrip("!"))

# REplace Method

print(name2.replace("Kankon", "Lord"))

# Split Method: turns string to list

name3 = "Kankon Lord King Emperor Duke"

print(name3.split(" "))

# Capitalize Method : turns first word to Capital

desc = "welcome to python course"

print(desc.capitalize())

# Center Method : Centers any string using spaces

desc2 = "Welcome to the console"

print(desc2)
print(desc2.center(60)) # Length of String + Space = 60

# Count Method : counts a spcific string is a Variable

desc4 = "Welcome to Kankon's World. Kankon is the boss here."

print(desc4.count("Kankon"))

# Endswith Method : Checks if the string ends with something specific

name4 = "Kankon777"

print(name4.endswith("777")) # Returns true or false

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

# Find method : Returns the index number of the string and returns -1 if not found

str3 = "My name is Kankon. But, he is an honest man"

print(str3.find("is"))
print(str3.find("Nil"))

# Index Method : Similiar to Find method just only returns an exception when not found

str3 = "My name is Kankon. But, he is an honest man"

print(str3.index("is"))
# print(str3.index("Nil")) # Throws an error

# Alnum and Alpha Method : Checks if the string is alphaNeumeric (a-z A-Z 0-9) and Alpha (a-z A-Z)

str4 = "HeisverySmart"
str5 = "HeisverySmart99"

print(str4.isalnum())
print(str4.isalpha())
print(str5.isalpha())
print(str5.isalnum())

# Lower Method : checks the string if all the characters are in lower case

str6 = "hello world"
print(str6.islower())

# Printable Method : checks the string if all the characters are printable

str7 = "Hello Guys\n"
print(str7.isprintable())

# Space Method : checks the string and returns true if all the characters contains space

str8 = " "
str9 = "HelloWorld"

print(str8.isspace())
print(str9.isspace())

# Title Method : checks the string and returns true if the first character contains capital letter

str9 = "Hello World"

print(str9.istitle())

# Startswith Method : checks the string and returns true if the first character starts with ....

str10 = "Python is a programming language"

print(str10.startswith("Python"))

# Swapcase Method : Turns every Alphabet to the opposite case state to what it was.

str11 = "Python is a Interpreted Language"

print(str11.swapcase())

# Title Method : Turns every First Alphabet of a word to Capital letter.

str11 = "Python is a Interpreted Language"

print(str11.title())