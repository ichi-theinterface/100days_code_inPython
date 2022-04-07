from cgitb import text
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
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)
# print(question_bank[2].text)
# print(question_bank[1].answer)

quiz = QuizBrain(question_bank)
quiz.next_nexquestion()
