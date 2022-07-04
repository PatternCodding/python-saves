from hashlib import new


class Question:
    
    def __init__(self, Q_text, Q_answer):
        self.text = Q_text
        self.answer = Q_answer
        
# new_q = Question("anytext", "False")
# print(new_q.text)
