from cgi import test
from mimetypes import init
from operator import length_hint

class QuizBrain:

    def __init__(self, input):
        self.question_number = 0 
        self.question_list = input
    
<<<<<<< HEAD
    def still_has_questions(self):
        if self.question_number <= 12:
            return True
        else:
            return False

=======
    def still_has_question(self):
        return self.question_number < len(self.question_list)
 
>>>>>>> 50a1af2d422ebf6a8ea19ff970fcd1899aff3440
    def next_nexquestion(self):
        # test = self.question_list[self.question_number]
        # print(test)
        
        current_question = self.question_list[self.question_number]
        self.question_number += 1 
        input(f"Q.{self.question_number} : {current_question.text} (True/False)?: ")


 