from question_model import question
from data import question_data
from quiz_brain import Quizbrain



question_bank = []

for i in question_data:
  question_bank.append(question(i["text"], i["answer"]))


quiz = Quizbrain(question_bank)

while quiz.still_left():
  quiz.nxt_question()
  quiz.answer_checker()