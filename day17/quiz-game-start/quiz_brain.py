from question_model import Question
from data import question_data

print(question_data)
print ("\n\n")
print(question_data[0]) 

# question_bank = [Question] 
# for x in question_data:

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

