# Nested If Else Conditionals 

num = 99

if(num < 0):
    print("The Number is Negative")
elif(num > 0):
    if(num > 0 and num <= 10):
        print("The Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("The Number is between 11-20")
    elif(num > 20 and num <= 30):
        print("The Number is between 21-30")
    else:
        print("The Number is Bigger than 30")
else:
    print("The Number is Zero.")