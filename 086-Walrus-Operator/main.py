# Walrus Operator in Python

a = 5
print(a := 6) # Walrus operator(:=) enables us to define a value to a variable within an expression.

# Walrus operator in a While Loop

nums = [3, 5, 7, 8, 9, 4]

while ((n := len(nums)) > 0):
    print(nums.pop())


# Another Example

# # Regular Example without Walrus
# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#           break
#     foods.append(food)

#Example with Walrus
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)