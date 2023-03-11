import requests
from bs4 import BeautifulSoup
import html5lib
import tkinter, time
from tkinter import ttk, messagebox
from tkinter import *

root = Tk()

archive_url = 'http://localhost:8888/sender/'
def get_file_links():
    r = requests.get(archive_url)
    soup = BeautifulSoup(r.content, 'html5lib')
    links = soup.findAll('a')
    file_links = [archive_url + link['href'] for link in links]
    return file_links 
def download_file_series(file_links):
    n=1
    for link in file_links: 
        file_name = link.split('/')[-1] 
        l1.config(text='Donwloading file: %s'%file_name)
        r = requests.get(link, stream=True)
        with open(file_name, 'wb') as f: 
            for chunk in r.iter_content(chunk_size = 1024*1024):
                if chunk:
                    f.write(chunk)
        
        while n<len(file_links)+1:
            progress_var.set(n)
            n+=1
            time.sleep(1)
            root.update_idletasks()
            break 
    l1.config(text='')
    messagebox.showinfo('Successful Download', 'All files are successfully downloaded!')
    return 
def start():
    file_links = check()
    download_file_series(file_links)
def check():
    check_links = [item.get() for item in check_buttons.values()]
    check_link_list = []
    for check_link in check_links:
        if check_link:
            check_link_list.append(check_link)
    return check_link_list
def selectall():
    max_vlinks = get_file_links()
    i=0
    for item in check_buttons.values():
        item.set(max_vlinks[i])
        i+=1
def deselectall():
    for item in check_buttons.values():
        item.set('')        

max_vlinks = get_file_links()
check_buttons = {item:StringVar() for item in max_vlinks}
check_frame = Frame(root)
check_frame.grid(row=0, column=0)
r=0
for item in max_vlinks:
    C = ttk.Checkbutton(check_frame, text=str(item.split('/')[-1]), variable=check_buttons[item], onvalue=str(item), offvalue='')
    C.grid(row=r, column=0, sticky=W)
    r+=1
l1 = Label(root, text='')
l1.grid(row=r, column=0)
r+=1
progress_var = IntVar()

pb = ttk.Progressbar(root, orient="horizontal", length=200, maximum=len(check()), mode="determinate", var=progress_var)
pb.grid(row=r, column=0)
r+=1
pb["value"] = 0
b1 = Button(root, text='Download', command=start)
b1.grid(row=r, column=0)
r+=1
bcheckall = Button(root, text='Select all', command=selectall)
bcheckall.grid(row=r, column=0)
buncheckall = Button(root, text='Deselect all', width=10, command=deselectall)
buncheckall.grid(row=r, column=1, pady=5, sticky=E)
root.mainloop()

