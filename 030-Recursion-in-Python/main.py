# Recursion in Python

# Recursion means calling a function inside that specific function - Sounds Interesting!

# Let's take an example with factorial

def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num - 1)
    
print("The Factorial of 5 is", factorial(5))

# Fibonacci Numbers Example

def fibonacci(n):
    # Handle edge cases 🛑
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the series with first two numbers 🌟
    fib_series = [0, 1]
    
    # Generate next numbers in the series 🔄
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    
    return fib_series

# Test it out 🚀
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
print(fibonacci(2))  # Output: [0, 1]
print(fibonacci(0))  # Output: []