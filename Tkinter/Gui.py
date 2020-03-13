from tkinter import *

window = Tk()           #creates an empty window

def km_to_miles():
    miles = float(e1_value.get())* 1.6
    t1.insert(END, miles)


#widgets
b1 = Button(window,text="Execute", command=km_to_miles)           #generates button
b1.grid(row=0,column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)              #area to enter a value
e1.grid(row=0,column=1)

t1 = Text(window, height=1, width=20)           #output text area
t1.grid(row=0,column=2)

window.mainloop()       #keeps window open
