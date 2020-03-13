from tkinter import *

window = Tk()

def convertion():
    grams = float(e1_value.get()) * 1000
    pound = float(e1_value.get()) * 2.20462
    ounce = float(e1_value.get()) * 35.274
    t_gram.delete(1.0,END)
    t_gram.insert(END, grams)
    t_pound.delete(1.0,END)
    t_pound.insert(END, pound)
    t_ounce.delete(1.0,END)
    t_ounce.insert(END, ounce)

b_convert = Button(window,text="Convert", command=convertion)
b_convert.grid(row=0,column=3)


e2=Label(window,text="Kg")
e2.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0,column=2)

t_gram = Text(window, height=1, width=20)
t_gram.grid(row=1,column=1)

t_pound = Text(window, height=1, width=20)
t_pound.grid(row=1,column=2)

t_ounce = Text(window, height=1, width=20)
t_ounce.grid(row=1,column=3)



window.mainloop() 