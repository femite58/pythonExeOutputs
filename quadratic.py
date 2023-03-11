from tkinter import *
from tkinter import ttk
import math
body = Tk()
body.title('Quadratic Calculator')
def calculate():
    a = float(eval(avar.get()))
    b = float(eval(bvar.get()))
    c = float(eval(cvar.get()))
    firstanswer = (-b+math.sqrt((b**2)-4*(a*c)))/(2*a)
    secondanswer = (-b-math.sqrt((b**2)-4*(a*c)))/(2*a)
    resultlabel.config(text='x = '+str(firstanswer)+' or '+str(secondanswer))
    
labela = Label(body, text='Value of a:')
labela.grid(row=0, column=0, pady=5)

avar = StringVar()
a_entry = ttk.Entry(body, textvariable=avar)
a_entry.grid(row=0, column=1, pady=5, padx=5)
a_entry.focus()

labelb = Label(body, text='Value of b:')
labelb.grid(row=1, column=0)

bvar = StringVar()
b_entry = ttk.Entry(body, textvariable=bvar)
b_entry.grid(row=1, column=1, padx=5)

labelc = Label(body, text='Value of c:')
labelc.grid(row=2, column=0, pady=5)

cvar = StringVar()
c_entry = ttk.Entry(body, textvariable=cvar)
c_entry.grid(row=2, column=1, pady=5, padx=5)

resultlabel = Label(body)
resultlabel.grid(row=3, column=0, columnspan=2, padx=5)

calculatebutton = ttk.Button(body, text='Calculate', command=calculate)
calculatebutton.grid(row=4, column=0, columnspan=2, pady=5)

body.mainloop()