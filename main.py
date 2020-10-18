from tkinter import *  
import math
  
def clicked():
	one = txt1.get()
	two = txt2.get()
	act = txt3.get()
	if act == "+":
		answer = Label(window, text=(int(one)+int(two)))
		answer.grid(column=0, row=3)
	elif act == "-":
		answer = Label(window, text=(int(one)-int(two)))
		answer.grid(column=0, row=3)
	elif act == "*":
		answer = Label(window, text=(int(one)*int(two)))
		answer.grid(column=0, row=3)
	elif act == "/":
		answer = Label(window, text=(int(one)/int(two)))
		answer.grid(column=0, row=3)
	else:
		answer = Label(window, text=("We can't do that"))
		answer.grid(column=0, row=3)

window = Tk()  
window.title("Calculator")  
window.geometry('400x250')
txt1 = Entry(window, width=10)  
txt1.grid(column=0, row=0)
txt2 = Entry(window, width=10)  
txt2.grid(column=0, row=1)
txt3 = Entry(window, width=5)
txt3.grid(column=1, row=1)
btn = Button(window, text="Answer", command=clicked)  
btn.grid(column=0, row=2) 
lbl = Label(window, text=("Input 2 variables and what are\nyou going to do (+, -, *, /)"), font=("Arial Bold", 10))
lbl.grid(column=2, row=0)
window.mainloop()
