from mimetypes import init

class QuizBrain:

    def __init__(self, input):
        self.question_number = 0 
        self.question_list = input
    
    def still_has_questions(self):
        if self.question_number <= 12:
            return True
        else:
            return False

    def next_nexquestion(self):
        # test = self.question_list[self.question_number]
        # print(test)
        
        current_question = self.question_list[self.question_number]
        self.question_number =+ 1 
        input(f"Q.{self.question_number} : {current_question.text} (True/False)?: ")
 