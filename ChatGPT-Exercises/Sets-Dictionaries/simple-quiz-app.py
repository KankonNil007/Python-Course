# Simple Quiz App

# Topics used: dictionaries, f-strings

# Task:
# Create a dictionary of questions and answers. Ask each question to the user and keep score.

quiz = {
    "What is the capital of France?": "Paris",
    "2 + 2 = ?": "4",
    "Currency of USA?": "Dollar",
    "Capital of India?": "New Delhi"
}
Score = 0

for key, values in quiz.items():
    print(key)
    tempAns = input("Enter Answer: ")
    tempAns = tempAns.capitalize()
    if (values == tempAns):
        Score = Score + 1
        print(f"Your Answer is correct.\nYour Score is: {Score}")
    else:
        print(f"Game Over.Your Overall score: {Score}")
        break
