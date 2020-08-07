from tkinter import *
entry=""
#main app settings
app= Tk()
app.title("Pycalc")
app.configure(bg="steelblue")
app.resizable(0,0)

#title for calculator app
title= Label(app, text="Pycalc",width=6, fg="yellow", bg="steelblue", font="fixedsys 28")
title.grid(row=0,column=0,columnspan=4,sticky=N)

#display box for input/ouput
screen= Entry(app, width=40,background="white",text=entry)
screen.grid(row=1,column=0,columnspan=4,sticky=E,padx=5)

#button_click for line entry
def button_click(number):
    screen.insert(END, number)

#clear_click to clear screen
def clear_click():
    screen.delete(0,END)

#del_click to delete the char in last index of entry
def del_click():
    current= screen.get()
    screen.delete(len(current)-1, len(current))

#number buttons
nine= Button(app,padx=10,pady=10,text="9", command=lambda: button_click(9))
eight= Button(app,padx=10,pady=10,text="8", command=lambda: button_click(8))
seven= Button(app,padx=10,pady=10,text="7",command=lambda: button_click(7))
six= Button(app,padx=10,pady=10,text="6",command=lambda: button_click(6))
five= Button(app,padx=10,pady=10,text="5",command=lambda: button_click(5))
four= Button(app,padx=10,pady=10,text="4",command=lambda: button_click(4))
three= Button(app,padx=10,pady=10,text="3",command=lambda: button_click(3))
two= Button(app,padx=10,pady=10,text="2",command=lambda: button_click(2))
one= Button(app,padx=10,pady=10,text="1",command=lambda: button_click(1))
zero= Button(app,padx=10,pady=10,text="0",command=lambda: button_click(0))

#operation buttons
addition= Button(app,padx=10,pady=10,text="+",command=button_click)
subtraction= Button(app,padx=10,pady=10,text="-",command=button_click)
multiplication= Button(app,padx=10,pady=10,text="*",command=button_click)
division= Button(app,padx=10,pady=10,text="/",command=button_click)
equal= Button(app,padx=38,pady=10,text="=",command=button_click)

#functional buttons
clear= Button(app,padx=34,pady=10,text="CLR",command=clear_click)
delete= Button(app, padx=6,pady=10,text="DEL",command=del_click)

#button grid layout
nine.grid(row=2,column=0,sticky=N,padx=5,pady=5)
eight.grid(row=2,column=1,sticky=N,padx=5,pady=5)
seven.grid(row=2,column=2,sticky=N,padx=5,pady=5)
addition.grid(row=2,column=3,sticky=N,padx=5,pady=5)

six.grid(row=3,column=0,sticky=N,padx=5,pady=5)
five.grid(row=3,column=1,sticky=N,padx=5,pady=5)
four.grid(row=3,column=2,sticky=N,padx=5,pady=5)
subtraction.grid(row=3,column=3,sticky=N,padx=5,pady=5)

three.grid(row=4,column=0,sticky=N,padx=5,pady=5)
two.grid(row=4,column=1,sticky=N,padx=5,pady=5)
one.grid(row=4,column=2,sticky=N,padx=5,pady=5)
multiplication.grid(row=4,column=3,sticky=N,padx=5,pady=5)

delete.grid(row=5,column=0,sticky=N,padx=5,pady=5)
zero.grid(row=5,column=1,sticky=N,padx=5,pady=5)
division.grid(row=5,column=3,sticky=N,padx=5,pady=5)

clear.grid(row=6,column=0,columnspan=2,sticky=N,padx=5,pady=5)
equal.grid(row=6,column=2,columnspan=2,sticky=N,padx=5,pady=5)
