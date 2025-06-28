# Lambda Calculator

# Goal: Take a list of operations (+, -, *, /) and apply them on pairs of numbers using lambda.

# 🔧 Concepts:

# lambda, map(), global ops = {'+': lambda x,y: x+y, ...}

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Infinity"
}

data = [(3, 4, '+'), (10, 5, '-'), (6, 2, '*'), (9, 0, '/')]

results = list(map(lambda tup: ops[tup[2]](tup[0], tup[1]), data))
print(results)  # Output: [7, 5, 12, 'Infinity']