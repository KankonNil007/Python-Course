from questions import questions

print("========== Quiz Time ==========")

quesNum = 0
score = 0

for n, ques in enumerate(questions, start=1):
    quesNum = quesNum + 1
    print(f"Question {n}: {ques["question"]}")
    print(f"A. {ques["options"][0]}")
    print(f"B. {ques["options"][1]}")
    print(f"C. {ques["options"][2]}")
    print(f"D. {ques["options"][3]}")
    print("\n")
    inpAns = input("Enter your Answer: ")
    inpAns = inpAns.capitalize()
    if (inpAns == ques["answer"] or inpAns == ques["ans_alt"]):
        print("Correct!!")
        score = score + 1
    else:
        print("Incorrect!!")

    print("\n")
    print(f"Score: {score}/{quesNum}")
    print("-------------------------------")

print(f"Overall Score: {score}/{quesNum}")