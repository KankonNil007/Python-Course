# Seek and Tell Functions in Python

# seek() Function

with open("051-Seek-and-Tell-Functions/myfile.txt", "r") as txt:
    print(type(txt))

    # Seek Function tells you from which point you should run the program. It works in bytes. 
    txt.seek(12)

    # Read the next 8 bytes and starts after 12th byte
    txtPart = txt.read(8)
    print(f"Text from 13th and 8 bytes: {txtPart}")


# tell() Function

with open("051-Seek-and-Tell-Functions/myfile.txt", "r") as txt:
    txt.seek(5) # Starts from 5th byte
    print(txt.read(15)) # prints 15 bytes from 5th byte

    # Tell Function tells us where we are at the current position in that file in bytes
    print(txt.tell()) # 20 because 15 + 5


# truncate() Function

with open("051-Seek-and-Tell-Functions/myfile2.txt" , "w") as txt: # Creates a new file

    txt.write("Hello World!") # Writes "Hello World!" inside that file

    # Truncate Method tells us how many bytes should we keep after adding something
    txt.truncate(8) # It will write only "Hello Wo" inside the file

with open("051-Seek-and-Tell-Functions/myfile2.txt" , "r") as txt:
    print(txt.read()) # Prints out the file