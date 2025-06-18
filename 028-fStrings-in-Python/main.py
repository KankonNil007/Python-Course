# f Strings in Python

# Format Method in Strings

letter = "My name is {} and I am from {}"
country = "Bangladesh"
name = "Kankon"

print(letter.format(name, country))

# f-Strings instead of Format Method

letter = f"My name is {name} and I am from {country}"
print(letter)

# Format Method in Numbers

txt = "For only {price:.2f} dollars!" # .2f means upto 2 decimal points
print(txt.format(price = 49.09999))

# f-Strings in Numbers

price = 99.599999
txt2 = f"The Shirt is only {price:.2f} dollars!"
print(txt2)

# Strings - Calculation handling

calculation = f"{23 * 40}"
print(calculation)

# Raw f-Strings Retaining Method

letter = f"My name is {{name}} and I am from {{country}}"
country = "Bangladesh"
name = "Kankon"

print(letter)