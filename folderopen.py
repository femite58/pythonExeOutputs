from tkinter import *
from tkinter import filedialog
import os
main = Tk()
def print_path():
    f = filedialog.askopenfilenames(parent=main, initialdir=str(os.getcwd()), title='Choose files')
    s = list(f)
    print(s)
    return f
b1 = Button(main, text='Print path', command=print_path)
b1.pack()

main.mainloop()