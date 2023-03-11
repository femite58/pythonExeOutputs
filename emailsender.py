import smtplib 
import tkinter
from tkinter import *
from tkinter import messagebox
main = Tk()
main.title("Email Sender")

def login(event):
    global smtpObj
    sender = str(s_email_e.get())
    receivers = [str(r_email_e.get())]
    message = str(msg.get("1.0", END))
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login(sender, s_pass_e.get())
    smtpObj.sendmail(sender, receivers, message)
    messagebox.showinfo("", "Successfully sent email")
    smtpObj.quit()

def quit_(event):
    main.quit()

sender_info = LabelFrame(main, text="Sender's Login Details")
sender_info.grid(row=0, column=0, pady=5, padx=10, sticky=W)

s_email_l = Label(sender_info, text="Email:")
s_email_l.grid(row=0, column=0, sticky=W, padx=5, pady=5)

s_email_e = Entry(sender_info)
s_email_e.grid(row=0, column=1, sticky=E, padx=5, pady=5)

s_pass_l = Label(sender_info, text="Password:")
s_pass_l.grid(row=1, column=0, sticky=W, padx=5, pady=5)

s_pass_e = Entry(sender_info, show="*")
s_pass_e.grid(row=1, column=1, sticky=E, pady=5, padx=5)

receiver_info = LabelFrame(main, text="Receiver's Email Address", width=207, height=50)
receiver_info.grid(row=1, column=0, padx=10, pady=5, sticky=W)
receiver_info.grid_propagate(False)


r_email_l = Label(receiver_info, text="Email:")
r_email_l.grid(row=0, column=0, pady=5, padx=5)

r_email_e = Entry(receiver_info)
r_email_e.grid(row=0, column=1, pady=5, padx=5)


msg = Text(main, height=6, width=25)
msg.grid(row=2, column=0, sticky=W, pady=5, padx=10) 

command = Frame(main, height=40, width=207)
command.grid(row=3, column=0, pady=5, padx=10, sticky=E)
command.grid_propagate(1)

quit = Button(command, text="Exit", width=10)
quit.grid(row=0, column=2, pady=5, padx=5, sticky=E)
quit.bind('<Button-1>', quit_)
quit.bind('<Return>', quit_)

send = Button(command, text="Send", width=10)
send.grid(row=0, column=1, pady=5, padx=5, sticky=E )
send.bind('<Return>', login)
send.bind('<Button-1>', login)

main.mainloop()