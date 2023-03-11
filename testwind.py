from tkinter import *
import time
main = Tk()

def newWindow2():
    main2 = Toplevel(main)
    def closeit():
        entry.grid()
    
    def closen():
        main2.destroy()
        main2.quit()
        
        
    
    entry = Entry(main2)
    entry.grid(row=0, column=0, pady=5)
    entry.grid_remove()
    
    button2 = Button(main2, text='Exit', command=closeit)
    button2.grid(row=1, column=0, pady=5, padx=5)
    button3 = Button(main2, text='Close', command=closen)
    button3.grid(row=1, column=1, pady=5, padx=5)
    
    
    main2.mainloop()

def newWindow(event):
    print('What are you')
    newWindow2()
    print('Mo wa')
    
button = Button(main, text='Open')
button.grid(row=0, column=0, pady=5, padx=5)
button.bind('<Button-1>', newWindow)
main.mainloop()