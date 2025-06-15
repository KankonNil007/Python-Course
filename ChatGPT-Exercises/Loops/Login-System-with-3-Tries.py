# Login System with 3 Tries with Loops

# Ask the user for username and password. Only allow 3 attempts using while. Exit early if login is correct.

Username = "Kankon007"
Password = "Pekkav00"

for i in range(1,4):
    inputUser = input("Enter UserName: ")
    inputPass = input("Enter Password: ")

    if (inputUser == Username and inputPass == Password):
        print("Welcome", Username)
        break
    else:
        print("Invalid Username or Password")
else:
    print("Too many attempts. Access denied")
