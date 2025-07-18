# Quiz App (MCQ Game)

### 🖥 UI (Command Line):
```
========== Quiz Time ==========
Question 1: What is the capital of France?
A. Berlin
B. Madrid
C. Paris
D. Rome

Enter your answer: c
Correct!

Score: 1/1
-------------------------------
```

### 🧠 Features:

- Store questions and answers (dict or list of dicts)
- Ask questions one by one
- Keep score
- Give feedback: Correct/Wrong

### 💡 Hints:

- Use a list of dictionaries to store quiz data:
```
{"question": "What is 2+2?", "options": ["1", "2", "4", "8"], "answer": "4"}
```
- Loop through questions using for
- Use .lower() to compare answers
- Show final score at the end