from tkinter import *

window = Tk()
window.title("Miles to kilometer convertor")
window.minsize(width=500, height=500)




#main miles input box

input = Entry(width=30)
input.insert(END, string="Enter miles here")
miles = 0
kilometer = 0


#answer label
label2 = Label(text='0')
label2.place(x=160,y=80)

def get_miles(event=None):

    try:
        miles = float(input.get())
        kilometer = miles * 1.6
        label2.config(text=f"{kilometer:.2f} kms",font=("Arial", 40), fg='red')
    except ValueError:
        label2.config(text="Enter a number", font=("Arial", 40), fg='red')
    



input.place(x=100, y=10)
input.bind("<Return>", get_miles)

#Label for Miles

label = Label(text="This is old text")
label.config(text="Miles")
label.place(x=300, y=10)

#Label for is equal to

label1 = Label(text='This is old text')
label1.config(text='Is equal to=  ', font=("Arial", 25))
label1.place(x=150, y = 40)

#Answer



# label2 = Label(text='This is old text')
# label2.config(text=kilometer)
# label2.place(x=200,y=50)






window.mainloop()