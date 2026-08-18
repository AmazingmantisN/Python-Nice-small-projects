from constants import *
from tkinter import messagebox
import winsound

winsound.PlaySound(
    r"C:\Windows\Media\chimes.wav", winsound.SND_FILENAME | winsound.SND_ASYNC
)

class TimerManager:

  def __init__(self, window, canvas, text_id):
    self.window = window
    self.canvas = canvas
    self.text_id = text_id
    self.break_selected = SHORT_BREAK_MIN
    self.timer = None
    self.current_mode = "work"
    self.count = WORK_MIN


  def shortbreak_selected(self):
    self.break_selected = SHORT_BREAK_MIN

  def longbreak_selected(self):
    self.break_selected = LONG_BREAK_MIN

  def start_timer(self):
      if self.current_mode == "work":
        self.work_timer()
      elif self.current_mode == "break":
         self.break_timer()
    

  def work_timer(self):
    
    if self.timer:
        self.window.after_cancel(self.timer)
    self.current_mode = "work"
    self.count_down(WORK_MIN * 60)

  def break_timer(self):
    
    
      if self.timer:
            self.window.after_cancel(self.timer)
      self.current_mode = "break"
      self.count_down(self.break_selected * 60)
    
  
  def count_down(self, count):
     
    focus = count
    
    count_min = focus // 60
    count_sec = focus % 60

    self.canvas.itemconfig(
        self.text_id, text=f"{count_min:02d}:{count_sec:02d}"
    )
    
    if focus > 0:
       self.timer = self.window.after(1000,self.count_down, focus-1)
    else:
      winsound.MessageBeep(
                winsound.MB_ICONASTERISK
            )
      
      if self.current_mode == "work":
         messagebox.showinfo(
                    title="Work Done!",
                    message="Great job! Time for a break.",
                )
         self.current_mode = "break"
      elif self.current_mode == "break":
         messagebox.showinfo(
                    title="Break Finished!", message="Back to work!"
                )
         self.current_mode = "work"
        
  def reset_timer(self):
      
      if self.timer:
          self.window.after_cancel(self.timer)
          self.timer = None
      self.current_mode = "work"    
      self.canvas.itemconfig(self.text_id, text="00:00")
    
    