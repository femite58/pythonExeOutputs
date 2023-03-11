import os
import subprocess
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

main = Tk()
main.title("Files Renamer")

def execute(event):
    path = os.getcwd()

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.exe' in file:
                files.append(os.path.join(r, file))
    files2 = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.exe' in file:
                files2.append(os.path.join(r, file))
                
    character = str(entry.get())
    n = 0
    r = 0
    j = 0
    k = 0
    for file in files:
        if os.path.basename(file)[0] == 'v':
            file_str_dir = os.path.dirname(file)
            file_str_exist = os.path.basename(file).lstrip(character)
            exist_filedir = os.path.join(file_str_dir, file_str_exist)
            if exist_filedir in files:
                dir2 = os.path.dirname(file)
                os.chdir(dir2)
                ren_file = str(os.path.basename(file)).lstrip(character)
                os.remove(str(os.path.join(dir2, ren_file)))
                subprocess.call('attrib -h -s '+'"{}"'.format(file), shell=True, startupinfo=si)
                os.rename(file, str(os.path.join(dir2, ren_file)))
                n+=1    
            else:
                pass
        else:
            continue 
    subprocess.call('dir /a /s '+character+'*.exe /b >hiddenexedir.txt', shell=True, startupinfo=si)
    hiddenexedir = open('hiddenexedir.txt', 'r')
    hiddenexedir_list = str(hiddenexedir.read()).replace('\r', '').strip('\n').split('\n')
    hiddenexedir.close()
    os.remove('hiddenexedir.txt')
    for exe_file in hiddenexedir_list:
        if exe_file == '':
            continue
        exe_file_dir = os.path.dirname(exe_file)
        strip_exe_file = os.path.basename(exe_file).lstrip(character)
        ren_exe_file = os.path.join(exe_file_dir, strip_exe_file)
        if os.path.exists(ren_exe_file):
            while 1:
                if os.path.isdir(ren_exe_file):
                    subprocess.call('rd /s /q "'+ren_exe_file+'"', shell=True, startupinfo=si)
                    break
                else:
                    break
        ico_exe_file = os.path.basename(exe_file)[:len(os.path.basename(exe_file))-4]+os.path.basename(exe_file)[-4:].replace('.exe', '.ico')
        exist_ico_file = os.path.join(exe_file_dir, ico_exe_file)
        if os.path.exists(exist_ico_file):
            if os.path.getsize(exist_ico_file) == 0:
                try:    
                    os.remove(exist_ico_file)
                except:
                    continue
                subprocess.call('attrib -h -s "'+exe_file+'"', shell=True, startupinfo=si)
                os.rename(exe_file, ren_exe_file)
                r+=1
    
    subprocess.call('dir /a /s '+character+'*.ico /b >icodir.txt', shell=True, startupinfo=si)
    icodir = open('icodir.txt', 'r')
    icodir_list = str(icodir.read()).replace('\r', '').strip('\n').split('\n')
    icodir.close()
    os.remove('icodir.txt')
    for ico_file in icodir_list:
        if ico_file == '':
            continue 
        if os.path.getsize(ico_file) == 0:
            os.remove(ico_file)
            j+=1
    
    subprocess.call('dir /a:sh /s '+character+'*.exe /b >hiddenexefiles.txt', shell=True, startupinfo=si)
    hiddenexefiles = open('hiddenexefiles.txt', 'r')
    hiddenexefiles_list = str(hiddenexefiles.read()).replace('\r', '').strip('\n').split('\n')
    hiddenexefiles.close()
    os.remove('hiddenexefiles.txt')
    for exe_file in hiddenexefiles_list:
        if exe_file == '':
            continue
        exe_file_dir = os.path.dirname(exe_file)
        strip_exe_file = os.path.basename(exe_file).lstrip(character)
        ren_exe_file = os.path.join(exe_file_dir, strip_exe_file)
        if os.path.exists(ren_exe_file):
            while 1:
                if os.path.isdir(ren_exe_file):
                    subprocess.call('rd /s /q "'+ren_exe_file+'"', shell=True, startupinfo=si)
                    break
                else:
                    break
        subprocess.call('attrib -h -s "'+exe_file+'"', shell=True, startupinfo=si)
        os.rename(exe_file, ren_exe_file)
        k+=1
    
    totalfiles = n+r+j+k
    messagebox.showinfo("", "%s files are treated and renamed successfully!"%(totalfiles))
    main.quit()
 
frame = Frame(main)
frame.pack()

label = Label(frame, text="Enter the character to remove:")
label.pack(side="left", padx=5)
entry = ttk.Entry(frame)
entry.pack(side="right", padx=10)
entry.focus()
entry.bind('<Return>', execute)

button = ttk.Button(main, text="Ok", width=10)
button.pack(pady=10)
button.bind('<Return>', execute)
button.bind('<Button-1>', execute)

main.mainloop()