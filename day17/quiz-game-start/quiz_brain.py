from cgi import test
from mimetypes import init
from operator import length_hint

class QuizBrain:

    def __init__(self, input):
        self.question_number = 0 
        self.question_list = input
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)
 
    def next_nexquestion(self):
        # test = self.question_list[self.question_number]
        # print(test)
        
        current_question = self.question_list[self.question_number]
        self.question_number += 1 
        user_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer_input, correct_answer):
        if user_answer_input == correct_answer:
            print ("you got it right!!")
        else:
            print ("the answer is wrong...")




 