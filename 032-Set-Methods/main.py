# Set Methods in Python

# Union between Sets: A U B

set1 = {2, 4, 6, 7}
set2 = {5, 7, 9}

print("The Union Set:", set1.union(set2)) # This doesn't update set1
print(set1)

# If you want to update it to what changed so far
# We use update method to update it
# For example, we changed set1 to union set2. So, set1 should become the union of the two sets

set1.update(set2)
print(set1)

# Intersection between Sets: A ∩ B

set3 = {2, 4, 6, 7}
set4 = {5, 7, 9}

print("The Intersection Set:", set3.intersection(set4)) # This doesn't update set3
print(set3)

# If you want to update it to what changed so far
# We use intersection_update method to update it
# For example, we changed set3 to intersection set4. So, set3 should become the union of the two sets

set3.intersection_update(set4)
print(set3)


# Symmetric Difference: (A U B) - (A ∩ B)
# All the values that are not in common

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.difference(cities2)
print("Symmetric Difference:",cities3)

# Symmetric Difference Update Method

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities.symmetric_difference_update(cities2)
print("Symmetric Difference Update:",cities)


# Difference: A - B or B - A

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.difference(cities2) # A - B
cities4 = cities2.difference(cities) # B - A
print("Difference A:",cities3)
print("Difference B:",cities4)

# Difference Update Method

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities.difference(cities2) # A - B
cities2.difference(cities) # B - A
print("Difference A Update:",cities)
print("Difference B Update:",cities2)


# Disjoint Set
# When A set's values are not equal to another set's any other value, it is called a disjoint set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = {"Berlin", "Delhi"}
cities4 = {"Seoul", "Kabul"}

print(cities.isdisjoint(cities2)) # False
print(cities3.isdisjoint(cities4)) # True


# Super Set
# When a set have all the values of another set, it is called super set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid"}

cities3 = {"Berlin", "Delhi"}
cities4 = {"Seoul", "Kabul"}

print(cities.issuperset(cities2)) # True
print(cities3.issuperset(cities4)) # False


# Sub Set
# When a set have some or only just one values of another set, it is called sub set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid"}

print(cities.issubset(cities2)) # False
print(cities2.issubset(cities)) # True


# Adding a value to a set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")

print(cities)

# Removing a value from a set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Madrid") # Raises an error if the value is not in the set
cities.discard("Delhi") # Doesn't raise an error if the value is not in the set

print(cities)

# Randomly Removing a value from a set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print("The Item which I poped is:", item)


# Deleting an Entire Set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities

# print(cities) # Throws an error as the set is deleted


# Clearing all the values of a set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()

print(cities) # Prints an empty set unlike del method which shows an error

# Checking a set if a value is there

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")