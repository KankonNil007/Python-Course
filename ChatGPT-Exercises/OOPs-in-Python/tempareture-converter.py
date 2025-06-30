# Temperature Converter

# Topics: @staticmethod, @classmethod

# 📝 Task:
# Create a TemperatureConverter class with:

# @staticmethod for celsius_to_fahrenheit(c) and fahrenheit_to_celsius(f)

# @classmethod that takes a temperature and unit and returns converted value with unit

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return round((c * 9/5) + 32, 2)

    @staticmethod
    def fahrenheit_to_celsius(f):
        return round((f - 32) * 5/9, 2)

    @classmethod
    def convert(cls, value, unit):
        if unit.upper() == "C":
            return f"Converted: {cls.celsius_to_fahrenheit(value)} F"
        elif unit.upper() == "F":
            return f"Converted: {cls.fahrenheit_to_celsius(value)} C"
        else:
            return "Unknown unit."

# --- User Interaction ---
value = float(input("Enter temperature value: "))
unit = input("Enter unit (C/F): ")

print(TemperatureConverter.convert(value, unit))
