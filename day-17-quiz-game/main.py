from question_model import Question
# from data import question_data
from data2 import question_data
from quiz_brain import QuizBrain

question_bank = []

for dict in question_data:
    #using data.py file
    # question_text = dict["text"]
    # question_answer = dict["answer"]
    # using data2.py file
    question_text = dict["question"]
    question_answer = dict["correct_answer"]
    question_object = Question(question_text, question_answer)
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score: {quiz.score}/{quiz.question_number}")