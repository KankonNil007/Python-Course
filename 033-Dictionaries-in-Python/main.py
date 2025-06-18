# Dictionaries in Python

dict1 = {
    "Kankon": "Human Being",
    "Table": "Object",
    "Goat": "Animal"
}

print(dict1)

# We can access every value

print(dict1["Table"])
print(dict1["Kankon"])

# We can use multiple data types

dict2 = {
    23: "Kankon",
    45: 6.7,
    65: True
}

print(dict2[45])
print(dict2[65])

# There are 2 ways of printing a value of a key of a dictionary

dict3 = {
    "name": "Kankon",
    "age": 20,
    "eligible": True
}

print(dict3["name"]) # This shows an error if the requested key is not there
print(dict3.get("name")) # This displays "None" if the requested key is not there


# Accessing Multiple Keys, Values or Both

dict3 = {
    "name": "Kankon",
    "age": 20,
    "eligible": True
}

print(dict3.keys()) # Printing the keys
print(dict3.values()) # Printing the values
print(dict3.items()) # Printing the keys and values

# Through a loop

for i in dict3.keys():
    print(f"The value of the key {i} is {dict3[i]}")

# Through a loop[items() method]

for keys, values in dict3.items():
    print(f"{keys} = {values}")