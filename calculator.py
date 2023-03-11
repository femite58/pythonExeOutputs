import tkinter
from tkinter import *
top = tkinter.Tk()
top.title(string='Calculator')
top.geometry("400x400")
expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
equation = StringVar()

e = tkinter.Entry(top, width=47, justify='left', textvariable=equation)
e.place(x=50, y=50)
button7 = tkinter.Button(text= '7', height=2, width=10, command=lambda:press(7))
button7.place(x=20,y=100)
button8 = tkinter.Button(text= '8', height=2, width=10, command=lambda:press(8))
button8.place(x=110,y=100)
button9 = tkinter.Button(text='9', height=2, width=10, command=lambda:press(9))
button9.place(x=200, y=100)
buttonX = tkinter.Button(text='X', height=2, width=10, command=lambda:press('*'))
buttonX.place(x=290, y=100)
button4 = tkinter.Button(text='4', height=2, width=10, command=lambda:press(4))
button4.place(x=20, y=150)
button5 = tkinter.Button(text='5', height=2, width=10, command=lambda:press(5))
button5.place(x=110, y=150)
button6 = tkinter.Button(text='6', height=2, width=10, command=lambda:press(6))
button6.place(x=200, y=150)
buttonmin = tkinter.Button(text='-', height=2, width=10, command=lambda:press('-'))
buttonmin.place(x=290, y=150)
button1 = tkinter.Button(text='1', height=2, width=10, command=lambda:press(1))
button1.place(x=20, y=200)
button2 = tkinter.Button(text='2', height=2, width=10, command=lambda:press(2))
button2.place(x=110, y=200)
button3 = tkinter.Button(text='3', height=2, width=10, command=lambda:press(3))
button3.place(x=200, y=200)
buttonplus = tkinter.Button(text='+', height=2, width=10, command=lambda:press('+'))
buttonplus.place(x=290, y=200)
plusorminus = tkinter.Button(text='+/-', height=2, width=10)
plusorminus.place(x=20, y=250)
button0 = tkinter.Button(text='0', height=2, width=10, command=lambda:press(0))
button0.place(x=110, y=250)
buttonpoint = tkinter.Button(text='.', height=2, width=10, command=lambda:press('.'))
buttonpoint.place(x=200, y=250)
equalto = tkinter.Button(text='=', height=2, width=10, command=equalpress)
equalto.place(x=290, y=250)


 
top.mainloop()
