from cgitb import text
from re import A
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# print(question_data)
# print ("\n\n")
# print(question_data[0]) 

# question_bank = [Question] 
# for x in question_data:

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)
# print(question_bank[2].text)
# print(question_bank[1].answer)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_nexquestion()

print("You've completed the test")
print(f"Your score is {quiz.score}/{quiz.question_number}")
