# os Module in Python

import os

# Creates a folder in that path named data
if (not os.path.exists("046-os-Module-in-Python/data")): # For not showing any error if the path already exists
    os.mkdir("046-os-Module-in-Python/data")

# Making 100 directory using loop and os module
for i in range(1, 101):
    os.mkdir(f"046-os-Module-in-Python/data/Day{i}")

# Renameing the folders using loop and os module

for i in range(1, 101):
    os.rename(f"046-os-Module-in-Python/data/Day{i}", f"046-os-Module-in-Python/data/Tutorial {i}")


# Listing the files and folders inside a folder

folders = os.listdir("046-os-Module-in-Python/data")
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"046-os-Module-in-Python/data/{folder}"))

# How to print the directory that you are working

print(os.getcwd())

# You can also change it 

# os.chdir("Your desired path")


# To create nested directories

os.makedirs('folder1/folder2/folder3')

# Remove a folder or directory
# These don't work if the folders contain files.

os.rmdir('my_folder')  # Removes empty folder

# Remove nested directories
os.removedirs('folder1/folder2/folder3')

# Check if File or Directory

print(os.path.isfile('test.txt'))       # True if it's a file
print(os.path.isdir('my_folder'))       # True if it's a directory

# Get File Path Info

file_path = 'example.txt'

print(os.path.abspath(file_path))           # Full path
print(os.path.basename(file_path))          # 'example.txt'
print(os.path.dirname(file_path))           # Directory path
print(os.path.splitext(file_path))          # ('example', '.txt')

# Execute System Commands

os.system('dir')    # Windows - list directory