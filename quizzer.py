
!file-question_model.py*!

class question:
    def __init__(self,qtext,qans):
        self.text=qtext
        self.ans=qans


q=question(12,'true')
print(q.text)

main.py


from question_model import question
from data import question_data
from quiz_brain import quizbrain

question_bank=[]
for Question in question_data:
    q_text=Question["text"]
    q_ans=Question["answer"]
    new_q=question(q_text,q_ans)
    question_bank.append(new_q)
quiz=quizbrain(question_bank)


while quiz.still_has_question():
    quiz.nextquestion()

print("you have completed the quiz")
print(f"your final score is {quiz.score}/{quiz.question_number}")




quiz_brain.py

class quizbrain:
    def __init__(self,q_list):
        self.question_number=0
        self.score=0
        self.question_list=q_list

    def still_has_question(self):
        if self.question_number<len(self.question_list):

            return True
        else:
            return False

    def nextquestion(self):
        current_question= self.question_list[self.question_number]
        self.question_number+=1
        user_answer = input(f"Q.{self.question_number}:{current_question.text}(True/False):")
        self.check_answer(user_answer,current_question.ans)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("wrong answer")
        print(f"the correct answer is {correct_answer}")
        print(f"Your current score is {self.score}")

data.py
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to "
             "eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

