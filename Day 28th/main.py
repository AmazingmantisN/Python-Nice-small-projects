from tkinter import *
from PIL import Image, ImageTk
from timer import TimerManager
# ---------------------------- CONSTANTS ------------------------------- #
from constants import *
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(bg="#CF4173")

# Load original image using PIL
bg_path = r"C:\Programming\Python Udemy course\Day 28th\Pomodorobgpic.png"
bg_original = Image.open(bg_path)
bg_pic = ImageTk.PhotoImage(bg_original)

# Background label setup
background_label = Label(window, image=bg_pic, bg="#CF4173")
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# Canvas setup
canvas = Canvas(width=300, height=300, bg="#CF4173", highlightthickness=0)
canvas.create_image(150, 150, image=bg_pic)
counter_Text =  canvas.create_text(
        150, 120, text="00:00", font=("Bauhaus95", 35, "bold"), fill="#0B0305"
    )

timer_mgr = TimerManager(window, canvas, counter_Text)

#Timer Label
canvas.create_text(
    150,50, text="Timer", font=(FONT_NAME, 18), fill="#F5EEF0"
)

#tickmark
text = "✓"
canvas.create_text(
    150,190, text=text, font=("BernardMTCondensed", 20, "bold"), fill="#023A19"
)
#Buttons
start_button = Button(
    window,
    text="Start",
    width=7,  # Fixed width forces both buttons to match size
    font=(FONT_NAME, 12, "bold"),
    fg="#F7F5DD",
    bg="#5D3140",
    activebackground="#3D202A",
    activeforeground="#F7F5DD",
    bd=0,
    relief="flat",
    pady=0,
    cursor="hand2",
    command=lambda: timer_mgr.start_timer()
)
start_button.place(x=30, y=210)

stop_button = Button(
    window,
    text="Reset",
    width=7,  # Fixed width matches Start button exactly
    font=(FONT_NAME, 12, "bold"),
    fg="#F7F5DD",
    bg="#5D3140",
    activebackground="#3D202A",
    activeforeground="#F7F5DD",
    bd=0,
    relief="flat",
    pady=0,
    cursor="hand2",
    command=lambda: timer_mgr.reset_timer()
    
)
stop_button.place(x=210, y=210)



#Break selector buttons
short_break_btn = Button(
    window,
    text="Short Break",
    font=(FONT_NAME, 8, "bold"),
    fg="#F7F5DD",
    bg="#5D3140",
    activebackground="#3D202A",
    activeforeground="#F7F5DD",
    bd=0,
    relief="flat",
    cursor="hand2",
    command=timer_mgr.shortbreak_selected
)
short_break_btn.place(x=215, y=35)

long_break_btn = Button(
    window,
    text="Long Break",
    font=(FONT_NAME, 8, "bold"),
    fg="#F7F5DD",
    bg="#5D3140",
    activebackground="#3D202A",
    activeforeground="#F7F5DD",
    bd=0,
    relief="flat",
    cursor="hand2",
    command=timer_mgr.longbreak_selected
)
long_break_btn.place(x=220, y=10)



canvas.pack()


# Background resizing function
# def resize_background(event):
#     if event.width > 1 and event.height > 1:
#         resized = bg_original.resize(
#             (event.width, event.height), Image.Resampling.LANCZOS
#         )
#         new_pic = ImageTk.PhotoImage(resized)
#         background_label.config(image=new_pic)
#         background_label.image = new_pic




window.mainloop()