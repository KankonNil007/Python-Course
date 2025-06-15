# Days of the Week by Match case

# Ask the user to enter a number (1-7) and print the day of the week.

"""

Input: 1 → Output: Monday  
Input: 7 → Output: Sunday  
Input: 8 → Output: Invalid day

"""

# Let's Start:

daysNum = int(input("Input Days Number: "))

match daysNum:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Number")