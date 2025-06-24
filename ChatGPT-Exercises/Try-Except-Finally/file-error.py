# File Reader with Error Handling
    
# Concepts: try-except-finally

# 📝 Task:

# Ask user to input a filename.

# Try to open and read the file.

# If the file doesn't exist, catch the FileNotFoundError.

# Use finally to print: "Execution Completed".

filename = input("Enter filename (with extension): ")

try:
    file = open(filename, "r")
    content = file.read()
    print("\n📄 File Contents:\n", content)
except FileNotFoundError:
    print("❌ File not found. Please check the filename.")
except Exception as e:
    print("❌ An unexpected error occurred:", e)
finally:
    print("📁 File operation complete.")
