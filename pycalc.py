from tkinter import *
import math

#main app settings
app= Tk()
app.title("Pycalc")
app.configure(bg="steelblue")
app.resizable(0,0)

### FUNCTIONS ###
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
    
#addition call
def add():
    global stored
    global operation
    stored = screen.get()
    operation = '+'
    screen.delete(0,END)

#subtraction call
def sub():
    global stored
    global operation
    stored = screen.get()
    operation = '-'
    screen.delete(0,END)

#multiplication call
def mult():
    global stored
    global operation
    stored = screen.get()
    operation = '*'
    screen.delete(0,END)

#division call
def div():
    global stored
    global operation
    stored = screen.get()
    operation = '/'
    screen.delete(0,END)

#square number call
def squared():
    x=screen.get()
    check = float(x) % 1
    if(check == 0):
        x= int(x)*int(x)
    else:
        x= float(x)*float(x)
    screen.delete(0,END)
    screen.insert(END,x)

#square root call
def rooted():
    x=screen.get()
    x= float(x) ** .5
    screen.delete(0,END)
    screen.insert(END,x)

#exponent call
def exponents():
    global stored
    global operation
    stored = screen.get()
    operation = 'exp'
    screen.delete(0,END)

#pi value insert
def insert_pi():
    screen.insert(END, math.pi)

#equal call, uses stored global and the operation global to produce result
def equal():
    current= screen.get()
    check= float(stored) % 1
    ## if check = 0, it is an integer
    if(check == 0):
        if operation == '+':
            result = int(current) + int(stored)
        if operation == '-':
            result = int(stored) - int(current)
        if operation == "*":
            result = int(current) * int(stored)
        if operation == "/":
            if int(current) == 0:
                result = "ERROR: DIVIDE BY ZERO"
            else:
                result = int(stored) / int(current)
        if operation == "exp":
            result = int(stored) ** int(current)
            
    ## if check strays too far from 0, its a float
    if(check >= .0000001 or check <= .0000001):
        if operation == '+':
            result = float(current) + float(stored)
        if operation == '-':
            result = float(stored) - float(current)
        if operation == "*":
            result = float(current) * float(stored)
        if operation == "/":
            if float(current) == 0:
                result = "ERROR: DIVIDE BY ZERO"
            else:
                result = float(stored) / float(current)
        if operation == "exp":
            result = float(stored) ** float(current)
            
    screen.delete(0,END)
    screen.insert(END,result)

#additional_function to resize window and add function buttons for trig functions, exponents(powers and roots), and scientific notation conversion to sig figs
def additional_function():
    square= Button(app, padx=5, pady=10, text="x^2",command=squared).grid(row=2,column=4,sticky=N,padx=5,pady=5)
    square_root= Button(app, padx=3,pady=10,text="sq.rt.", command=rooted).grid(row=2,column=5,sticky=N,padx=5,pady=5)
    exponent= Button(app, padx=5, pady=10, text="exp.",command=exponents).grid(row=3,column=4,sticky=N,padx=5,pady=5)
    pi_val= Button(app, padx=10, pady=10, text="pi",command=insert_pi).grid(row=3,column=5,sticky=N,padx=5,pady=5)
    sine= Button(app, padx=8, pady=10, text="sin",command=button_click).grid(row=4,column=4,sticky=N,padx=5,pady=5)
    arcsine= Button(app, padx=5, pady=10, text="asin",command=button_click).grid(row=4,column=5,sticky=N,padx=5,pady=5)
    cosine= Button(app, padx=8, pady=10, text="cos",command=button_click).grid(row=5,column=4,sticky=N,padx=5,pady=5)
    arccosine= Button(app, padx=5, pady=10, text="acos",command=button_click).grid(row=5,column=5,sticky=N,padx=5,pady=5)
    tangent= Button(app, padx=8, pady=10, text="tan",command=button_click).grid(row=6,column=4,sticky=N,padx=5,pady=5)
    arctangent= Button(app, padx=5, pady=10, text="atan",command=button_click).grid(row=6,column=5,sticky=N,padx=5,pady=5)
    scinote= Button(app, padx=6, pady=10, text="Scientific Not.",command=button_click).grid(row=7,column=4,columnspan=2,sticky=N,padx=5,pady=5)

### BUTTONS ###
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
decimal= Button(app,padx=10,pady=10,text=".",command=lambda: button_click('.'))

#operation buttons
addition= Button(app,padx=10,pady=10,text="+",command=add)
subtraction= Button(app,padx=10,pady=10,text="-",command=sub)
multiplication= Button(app,padx=10,pady=10,text="*",command=mult)
division= Button(app,padx=10,pady=10,text="/",command=div)
equal= Button(app,padx=38,pady=10,text="=",command=equal)

#functional buttons
clear= Button(app,padx=34,pady=10,text="CLR",command=clear_click)
delete= Button(app, padx=6,pady=10,text="DEL",command=del_click)
function_tab= Button(app, padx=25, pady=10, text="ADDITIONAL FUNCTIONS >>>",command=additional_function)

### LAYOUT ###
#title for calculator app
#(row 1)
title= Label(app, text="Pycalc",width=6, fg="yellow", bg="steelblue", font="fixedsys 28")
title.grid(row=0,column=0,columnspan=4,sticky=N)

#display box for input/ouput
#(row 2)
entry = ""
screen= Entry(app, width=40,background="white",text=entry)
screen.grid(row=1,column=0,columnspan=4,sticky=E,padx=5)

#button grid layout
#(row 3)
nine.grid(row=2,column=0,sticky=N,padx=5,pady=5)
eight.grid(row=2,column=1,sticky=N,padx=5,pady=5)
seven.grid(row=2,column=2,sticky=N,padx=5,pady=5)
addition.grid(row=2,column=3,sticky=N,padx=5,pady=5)
#(row 4)
six.grid(row=3,column=0,sticky=N,padx=5,pady=5)
five.grid(row=3,column=1,sticky=N,padx=5,pady=5)
four.grid(row=3,column=2,sticky=N,padx=5,pady=5)
subtraction.grid(row=3,column=3,sticky=N,padx=5,pady=5)
#(row 5)
three.grid(row=4,column=0,sticky=N,padx=5,pady=5)
two.grid(row=4,column=1,sticky=N,padx=5,pady=5)
one.grid(row=4,column=2,sticky=N,padx=5,pady=5)
multiplication.grid(row=4,column=3,sticky=N,padx=5,pady=5)
#(row 6)
delete.grid(row=5,column=0,sticky=N,padx=5,pady=5)
zero.grid(row=5,column=1,sticky=N,padx=5,pady=5)
decimal.grid(row=5,column=2,sticky=N,padx=5,pady=5)
division.grid(row=5,column=3,sticky=N,padx=5,pady=5)
#(row 7)
clear.grid(row=6,column=0,columnspan=2,sticky=N,padx=5,pady=5)
equal.grid(row=6,column=2,columnspan=2,sticky=N,padx=14,pady=5)
#(row 8)
function_tab.grid(row=7,column=0,columnspan=4,sticky=N,padx=10,pady=5)



def main():
    global stored
    global operation
    app.mainloop()
