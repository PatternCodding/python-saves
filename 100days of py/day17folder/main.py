from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(Q_text = question_text, Q_answer = question_answer)
    question_bank.append(new_question)
    
# print(question_bank)
quiz = QuizBrain(question_bank)
# quiz.next_question()

# to keep looping throught the entire questiins
while quiz.still_has_question():
    quiz.next_question()
    
# printing out the total score of the student after completing the entire questions

print("Your've completed the Quiz ")
print(f"Your final score was: {quiz.score}/{len(question_bank)} ")
# or
# print(f"Your final score was: {quiz.score}/{quiz.question_number} ")


'''{ASSIGNMENT}'''
'''
FROM
{https://opentdb.com/}
we can play around with there API. copy the questions and format it all.
generate your api. then try runnun the program
'''
