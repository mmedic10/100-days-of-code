from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"],i["answer"]))

quiz = QuizzBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")