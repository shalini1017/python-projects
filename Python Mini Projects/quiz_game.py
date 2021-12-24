
print("Welcome to the quiz game")

ques_answer_dict = {"what does USA stand for?": "United States of America", "what is the latest iphone version?": "13"}

questions = list(ques_answer_dict)


print("You will earn 1 point for each correct answer and get 0 for wrong ones\n")
print("Answer the following questions\n")

points = 0

for question in questions:
    print(question)
    user_answer = input("Answer: ")
    if user_answer == ques_answer_dict[question]:
        points = points + 1


print(f"you have got {points} points")
