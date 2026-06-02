class Quizbrain:
  def __init__(self, q_list):
    self.qnumber = 0
    self.q_list = q_list
    self.answer = ""
    self.user_answer = ""
    self.correct = 0
   
  def still_left(self):
    if self.qnumber < len(self.q_list):
       return True
    else:
       return False
   
    
  def nxt_question(self):
      current_question = self.q_list[self.qnumber]
      self.qnumber += 1
      self.answer = current_question.answer
      self.user_answer = input(f"Q.no: {self.qnumber}, {current_question.text} (true/false): ")
      
  def answer_checker(self):
     if self.user_answer.lower() == self.answer.lower():
        print("You got it right!")
        print(f"The correct answer is: {self.answer}")
        self.correct += 1
        print(f"Score: {self.correct}/{self.qnumber}")
        
     elif self.user_answer.lower() != self.answer.lower():
        print("You got it wrong!")
        print(f"The correct answer is: {self.answer}")
        print(f"Score: {self.correct}/{self.qnumber}")
        
     
  
      
    
    