from tkinter import *
from tkinter import messagebox, ttk, filedialog
import requests, html5lib, os, subprocess, http.server, socketserver, socket, time, sys
from bs4 import BeautifulSoup 
from PIL import Image, ImageTk

os.chdir(os.getcwd())

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW   

def resource_path1(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

main = Tk()
main.title('Tether')
main.geometry('400x400')
main.wm_resizable(width=False, height=False)
main.iconbitmap(resource_path1('tether logo.ico'))
          
def setPass():
    bodyframe.grid_remove()
    main2 = Frame(main, width=380, height=240)
    main2.grid(row=1, column=0)
    main2.grid_propagate(0)    
    def confirm(event):
        if len(str(newpasse_var.get())) < 8 :
            errorl.grid()
            errorl.config(text='Enter a valid password of at least 8 characters long', fg='red')
        else:        
            if str(newpasse_var.get()) == str(confirmpe_var.get()):
                subprocess.call('netsh wlan set hostednetwork key="'+str(confirmpe_var.get())+'" >nul', shell=True, startupinfo=si)
                main2.grid_remove()
                bodyframe.grid()
                sel(event)
                return
            else:
                errorl.grid()
                errorl.config(text='Passwords mismatched!!!', fg='red')
        
    label_instruct = Label(main2, text='Your Wireless Network is insecure \nCreate New Password to secure your Network', width=50)        
    label_instruct.grid(row=0, column=0)
    label_instruct.grid_propagate(0)
    new_pass = Frame(main2, width=300, height=150)
    new_pass.grid(row=1, column=0, pady=5, padx=5)
    new_pass.grid_propagate(0)
    
    newpasse_var = StringVar()
    confirmpe_var = StringVar()
    
    newpassl = Label(new_pass, text="New Password:")
    newpassl.grid(row=0, column=0, pady=5, sticky=W)
    newpasse = ttk.Entry(new_pass, show='*', textvariable=newpasse_var)
    newpasse.grid(row=0, column=1, pady=5, padx=5, sticky=E)
    
    confirmpl = Label(new_pass, text="Confirm Password:")
    confirmpl.grid(row=1, column=0, pady=5, sticky=W)
    confirmpe = ttk.Entry(new_pass, show='*', textvariable=confirmpe_var)
    confirmpe.grid(row=1, column=1, pady=5, padx=5, sticky=E)
    
    errorl = Label(new_pass)
    errorl.grid(row=2, column=0, pady=5, sticky=W)
    errorl.grid_remove()
    
    buttonpad = Label(new_pass, width=15)
    buttonpad.grid(row=3, column=0, sticky=W)
    buttonpad.grid_propagate(0)
    button = ttk.Button(new_pass, text='Create Password')
    button.grid(row=3, column=1, pady=5, sticky=E)
    button.bind('<Button-1>', confirm)
    
    
def print_path():
    f = filedialog.askdirectory(parent=main, initialdir=str(os.getcwd()), title='Choose folder to be shared')
    return f
def print_path_download():
    df = filedialog.askdirectory(parent=main, initialdir=str(os.getcwd()), title='Choose Download folder')
    return df
def sel(event):
    if var.get()=="Send":
        global real_ip                
        subprocess.call('ping '+socket.gethostname()+' -4 >ip.txt', shell=True, startupinfo=si)
        ip = open('ip.txt', 'r')
        ip_str = str(ip.read()).replace('\r', '').strip('\n').split('\n')[0]
        ip_str_start = ip_str.find('[')+1
        real_ip = ip_str[ip_str_start:].replace('] with 32 bytes of data:', '')
        ip.close()
        os.remove('ip.txt')
        
        while 1:
            if os.path.exists('sender'):
                os.remove('sender')
                break
            else:
                break 
        while 1:
            if os.path.exists('index.html'):
                os.remove('index.html')
                break
            else:
                break
        options.grid_remove()
        sender_path = str(print_path())
        while 1:
            if sender_path == '':
                messagebox.showerror('Error', 'You must choose a folder')
                sender_path = str(print_path())
            else:
                os.symlink(sender_path, 'sender')
                break
           
                        
        label.config(text='')
        label1.config(text='Tell the receiver to type your IP: '+real_ip+' when required')
                        
        html_file = open("index.html", "wb")
        os.chdir('sender')

        for r, d, f in os.walk(os.getcwd()):
            for file in f:
                if '.' in file:
                    if ',' in file:
                        os.rename(os.path.join(r, file),os.path.join(r, file).replace(',',' '))
                    elif '%' in file:
                        os.rename(os.path.join(r, file),os.path.join(r,file).replace('%',''))
                    else:
                        continue 
                else:
                    continue
        files = []

        for r, d, f in os.walk(os.getcwd()):
            for file in f:
                if '.' in file:
                    files.append(os.path.join(r, file))
                else:
                    continue
            
        filesname = []
        for r, d, f in os.walk(os.getcwd()):
            for file in f:
                if '.' in file:
                    filesname.append(os.path.basename(os.path.join(r, file)))
                else:
                    continue
        
        filesize = {}
        for r, d, f in os.walk(os.getcwd()):
            for file in f:
                if '.' in file:
                    filesize.update([(os.path.join(r, file),os.path.getsize(os.path.join(r, file)))])

        os.chdir('..')
        javascript = '''var files, text, fLen, i, files2, cwd, cwdl;
        files = '''+str(filesname)+''';
        fLen = files.length;
        files2 = '''+str(files)+''';
        cwd = "'''+os.getcwd()+'''";
        cwdl = cwd.length;
        text = '';
        for (i = 0; i < fLen; i++) {
            text += '<a href="'+files2[i].substr(cwdl+4)+'">'+files[i]+'</a><br>';
        }
        text += '<br>';


        document.getElementById("files").innerHTML = text;'''

        javascript2 = str(filesize)
        html = '''<!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>

        <h2>Welcome To Tether</h2>
        <p>Right click on the files below and click "Download link" to download your desired file</p>



        <p id="files"></p>


        <script>'''+javascript+'''

        </script>
        <script>'''+javascript2+'''
        </script>
        </body>
        </html>''' 
        
        html_file.write(html.encode('utf-8'))
        html_file.close()
        subprocess.call('attrib +h +s index.html', shell=True, startupinfo=si)
                
        subprocess.call('start "" "'+resource_path1('httpserver.exe')+'"', shell=True, startupinfo=si)
        welcomeframe.grid_remove()
        button.config(state='disabled')
        button.unbind('<Button-1>')
        receive_label_instruct.grid()
        receive_button.grid()
        changesharefolder.grid()
        
            
    else:
        while 1:
            try:
                http = subprocess.check_output('tasklist |findstr httpserver.exe', shell=True, startupinfo=si)
                subprocess.call('taskkill /im httpserver.exe /f >nul', shell=True, startupinfo=si)
                break
            except:
                break
        while 1:
            if os.path.exists('index.html'):
                os.remove('index.html')
                break 
            else:
                break
        while 1:
            if os.path.exists('sender'):
                os.remove('sender')
                break
            else:
                break
        
        subprocess.call('ping '+socket.gethostname()+' -4 >ip.txt', shell=True, startupinfo=si)
        ip = open('ip.txt', 'r')
        ip_str = str(ip.read()).replace('\r', '').strip('\n').split('\n')[0]
        ip_str_start = ip_str.find('[')+1
        real_ip = ip_str[ip_str_start:].replace('] with 32 bytes of data:', '')
        ip.close()
        os.remove('ip.txt')
        
        if real_ip == '127.0.0.1':
            messagebox.showerror('Network not found', 'Connect to the Sender\'s Wireless Network first')
            return 
        else:        
            welcomeframe.grid_remove()
            options.grid_remove()
            label.config(text='Click the "Send" button, if you want to send at the same time')
            label1.config(text="Ask your sender to reveal his/her \nIP address to you. Then type it when required")
            show_ip_frame()
            ip_label.config(text='Sender\'s IP address')
            button.grid_remove()
            send_button.grid()

def quit_(event):
    confirmexit = messagebox.askyesno('Exit Confirmation', 'Are you sure you want to exit?')
    if confirmexit:
        main.quit()
    else:
        return

def send_initiate():
    sender_path = str(print_path())
    while 1:
        if sender_path == '':
            messagebox.showerror('Error', 'You must choose a folder')
            sender_path = str(print_path())
        else:
            os.symlink(sender_path, 'sender')
            break

    html_file = open("index.html", "wb")
    os.chdir('sender')

    for r, d, f in os.walk(os.getcwd()):
        for file in f:
            if '.' in file:
                if ',' in file:
                    os.rename(os.path.join(r, file),os.path.join(r, file).replace(',',' '))
                elif '%' in file:
                    os.rename(os.path.join(r, file),os.path.join(r, file).replace('%',''))
                else:
                    continue 
            else:
                continue
    
    files = []

    for r, d, f in os.walk(os.getcwd()):
        for file in f:
            if '.' in file:
                files.append(os.path.join(r, file))
            else:
                continue
     
    filesname = []
    for r, d, f in os.walk(os.getcwd()):
        for file in f:
            if '.' in file:
                filesname.append(os.path.basename(os.path.join(r, file)))
            else:
                continue
    
    filesize = {}
    for r, d, f in os.walk(os.getcwd()):
        for file in f:
            if '.' in file:
                filesize.update([(os.path.join(r, file),os.path.getsize(os.path.join(r, file)))])
    os.chdir('..')
    javascript = '''var files, text, fLen, i, files2, cwd, cwdl;
    files = '''+str(filesname)+''';
    fLen = files.length;
    files2 = '''+str(files)+''';
    cwd = "'''+os.getcwd()+'''";
    cwdl = cwd.length;
    text = '';
    for (i = 0; i < fLen; i++) {
      text += '<a href="'+files2[i].substr(cwdl+4)+'">'+files[i]+'</a><br>';
    }
    text += '<br>';


    document.getElementById("files").innerHTML = text;'''

    javascript2 = str(filesize)
    html = '''<!DOCTYPE html>
    <html>
    <head>
    </head>
    <body>

    <h2>Welcome To Tether</h2>
    <p>Right click on the files below and click "Download link" to download your desired file</p>



    <p id="files"></p>


    <script>'''+javascript+'''

    </script>
    <script>'''+javascript2+'''
    </script>

    </body>
    </html>''' 
    
    html_file.write(html.encode('utf-8'))
    html_file.close()
    subprocess.call('attrib +h +s index.html', shell=True, startupinfo=si)                
    subprocess.call('start "" "'+resource_path1('httpserver.exe')+'"', shell=True, startupinfo=si)
    global real_ip
    subprocess.call('ping '+socket.gethostname()+' -4 >ip.txt', shell=True, startupinfo=si)
    ip = open('ip.txt', 'r')
    ip_str = str(ip.read()).replace('\r', '').strip('\n').split('\n')[0]
    ip_str_start = ip_str.find('[')+1
    real_ip = ip_str[ip_str_start:].replace('] with 32 bytes of data:', '')
    ip.close()
    os.remove('ip.txt')
    label.config(text='')
    label1.config(text='Tell the Sender to type your IP: '+real_ip+' when required')
    changesharefolder.grid()
    send_button.config(state='disabled')
    
def generate_frame(event):
    test_ip = ipvar.get()
    test_ip_mod = test_ip.split('.')
    while 1:
        if len(ipvar.get())>=9:
            if test_ip=="localhost" or test_ip=="127.0.0.1" or len(test_ip_mod)==4:
                break
            else:
                messagebox.showerror('Invalid IP', 'You entered an invalid IP address')
                return ip_entry.focus()
        else:
            messagebox.showerror('Invalid IP', 'You entered an invalid IP address')
            return ip_entry.focus()
                    
    logoframe.grid_remove()
    bodyframe.grid_remove()
    ip_frame.grid_remove()
    receivesend_frame.grid_remove()
    button.grid_remove()
    backbutton.grid()
    changesharefolder.grid_remove()
    changedownloadfolder.grid()
    
    global main3
    main3 = Frame(main, width=380, height=360)
    main3.grid(row=0, column=0)
    main3.grid_propagate(0)
        
    archive_url = 'http://'+str(ipvar.get())+':8888/'
    def get_file_links():
        r = requests.get(archive_url)
        soup = BeautifulSoup(r.content, 'html5lib')
        links = soup.findAll('script')
        untreated_files = []
        file_links = []
        for link in links:
            a = str(link)
            ap = a.find('files2 = ')
            l = a[ap:].split('\n')[0].strip('files2 = ;').strip('[]').split(', ')
            for lm in l:
                untreated_files.append(archive_url+lm[lm.find('sender'):].replace('\\\\', '\\').replace('\\', '/'))
        for f in untreated_files:
            if '"' in f:
                file_links.append(f.replace('"', ''))
            else:
                file_links.append(f.strip("'"))
        return file_links 
    def download_file_series(file_links):
        if len(file_links) == 0:
            return
        changedownloadfolder.config(state='disabled')
        quitbutton.config(state='disabled')
        quitbutton.unbind('<Button-1>')
        b1.config(state='disabled')
        backbutton.config(state='disabled')
        os.chdir('receiver')
        check_list_correct = []
        for check_l in file_links:
            if '.' in check_l.split('/')[-1]:
                check_list_correct.append(check_l)
            else:
                continue
        total_filesize = []
        for item_c in check_list_correct:
            total_filesize.append(file_size[item_c])
        real_total = eval(str(total_filesize).strip('[]').replace(',','+'))
        chunksize = 0
        file_number = 0
        for link in check_list_correct: 
            file_name = link.split('/')[-1] 
            l1.config(text='Donwloading... \n%s'%file_name)
            r = requests.get(link, stream=True)
            try:
                with open(file_name, 'wb') as f: 
                    for chunk in r.iter_content(chunk_size = 1024*1024*10):
                        if chunk:
                            f.write(chunk)
                            chunksize +=len(chunk)
                            percentage = 100*chunksize/int(real_total)
                            p_label.grid()
                            p_label.config(text=str(int(percentage))+'%')
                            pb['maximum'] = int(real_total)
                            pb_var.set(chunksize)
                            time.sleep(0.1)
                            pb_frame.update()
                    file_number+=1
            except:
                messagebox.showerror('Error', 'Oops! '+file_name+' cannot be downloaded due to an encountered error\nThis file will be skipped!')
                continue
        l1.config(text='')
        messagebox.showinfo('Successful Download', '%s file(s) are successfully downloaded!'%(file_number))
        os.chdir('..')
        changedownloadfolder.config(state='enabled')
        quitbutton.config(state='enabled')
        quitbutton.bind('<Button-1>', quit_)
        b1.config(state='enabled')
        backbutton.config(state='enabled')
        return  
    def start():
        file_links = check()
        download_file_series(file_links)
        return 
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
        if bcheckall_var.get()==1:
            for item in check_buttons.values():
                item.set(max_vlinks[i])
                i+=1
            bcheckall.config(text='Deselect all')
            showSize()
        else:
            for item in check_buttons.values():
                item.set('')
            bcheckall.config(text='Select all')
            size_label.grid_remove()
        return
    def closemain3():
        main3.destroy()
        main3.quit()
    def showSize():
        check_list = check()
        check_list_correct = []
        for check_l in check_list:
            if '.' in check_l.split('/')[-1]:
                check_list_correct.append(check_l)
            else:
                continue
        if len(check_list_correct) == 0:
            size_label.grid_remove()
            bcheckall_var.set(0)
            selectall()
            return 
        check_list_size = []
        for item_c in check_list_correct:
            check_list_size.append(file_size[item_c])
        real_total = eval(str(check_list_size).strip('[]').replace(',','+'))
        size_str = str(int(real_total))
        if len(size_str)>=4 and len(size_str)<7:
            size_str = str(int(real_total)/(1024))
            size_label.config(text=str(len(check_list_correct))+' file(s) size: '+size_str[:size_str.find('.')+3]+' KB')
        elif len(size_str)>=7 and len(size_str)<10:
            size_str = str(int(real_total)/(1024*1024))
            size_label.config(text=str(len(check_list_correct))+' file(s) size: '+size_str[:size_str.find('.')+3]+' MB')
        elif len(size_str)>=10:
            size_str = str(int(real_total)/(1024*1024*1024))
            size_label.config(text=str(len(check_list_correct))+' file(s) size: '+size_str[:size_str.find('.')+3]+' GB')
        else:
            size_label.config(text=str(len(check_list_correct))+' file(s) size: '+size_str+' B')
        size_label.grid()
    try:
        max_vlinks = get_file_links()
        check_buttons = {item:StringVar() for item in max_vlinks}
        file_size = {}
        sizes = requests.get(archive_url)
        soupsizes = BeautifulSoup(sizes.content, 'html5lib')
        sizes_l = soupsizes.select('script')
        actual_sizes = sizes_l[1].getText()
        size_dic_list = actual_sizes.replace('{','').replace('}','').replace('\n','').split(', ')
        for item in size_dic_list:
            item_list = item.split(':')
            if len(item_list)!=3:
                print(item_list)
                continue
            item_list[1] = archive_url+item_list[1][item_list[1].find('sender'):].replace('\\\\', '\\').replace('\\', '/')
            if '"' in item_list[1]:
                item_list[1] = item_list[1].replace('"', '')
            else:
                item_list[1] = item_list[1].strip("'")
            correct_list = []
            correct_list.append(item_list[1])
            correct_list.append(item_list[2].strip())
            correct_list[1] = int(correct_list[1])
            item_tuple = tuple(correct_list)
            file_size.update([item_tuple])
    except Exception as e:
        messagebox.showerror('Error', str(e)+'An error occurred\nTo fix this error:\n(1) Make sure you enter a valid IP address \n(2) Wait some seconds for the Sender to be ready')
        return 
    while 1:
        if os.path.exists('receiver'):
            break
        else:
            download_path = str(print_path_download())
            while 1:
                if download_path == '':
                    messagebox.showerror('Error', 'You must choose a folder')
                    download_path = str(print_path_download())
                else:
                    os.symlink(download_path, 'receiver')
                    break
            break 
   
    def init_checkbutton(frame):    
        r=0
        for item in max_vlinks:
            test_file = item.split('/')[-1]
            if '.' in test_file:
                C = ttk.Checkbutton(frame, text=str(item.split('/')[-1]), variable=check_buttons[item], onvalue=str(item), offvalue='', command=showSize)
                C.grid(row=r, column=0, sticky=W, padx=5)
                r+=1
            else:
                continue
    def onFrameConfigure(canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    iplabel = Label(main3, text='Your IP address is '+real_ip)
    iplabel.grid(row=0, column=0, pady=2)
    framewindow = Frame(main3, width=368, height=185)
    framewindow.grid(row=1, column=0)
    framewindow.grid_propagate(0)
    
    canvas = Canvas(framewindow, width=353, height=185)
    frame = Frame(canvas, bd=5)
    vsb = Scrollbar(framewindow, orient="vertical", command=canvas.yview)
    hsb = Scrollbar(framewindow, orient='horizontal', command=canvas.xview)
    canvas.configure(yscrollcommand=vsb.set)
    
    vsb.pack(side="right", fill='y')
    hsb.pack(side='bottom', fill='x')
    canvas.pack(side="left", fill='both', expand=1)
    
    canvas.create_window((0,0), window=frame, anchor="nw")
    
    canvas.bind_all('<MouseWheel>', lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
    
    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    
    init_checkbutton(frame)
    
    bcheckall_frame = Frame(main3)
    bcheckall_frame.grid(row=2, column=0, pady=5, padx=5, sticky=W)
    bcheckall_var = IntVar()
    
    bcheckall = ttk.Checkbutton(bcheckall_frame, text='Select all', variable=bcheckall_var, onvalue=1, offvalue=0, command=selectall)
    bcheckall.grid(row=0, column=0, padx=5, pady=5, sticky=W)
    pad_frame = Frame(bcheckall_frame, width=120)
    pad_frame.grid(row=0, column=1)
    pad_frame.grid_propagate(0)
    size_label = Label(bcheckall_frame, text='')
    size_label.grid(row=0, column=2, pady=5, padx=5, sticky=W)
    size_label.grid_remove()
        
    pb_frame = Frame(main3)
    pb_frame.grid(row=3, column=0)
    l1_frame = Frame(pb_frame, width=368, height=35)
    l1_frame.grid(row=0, column=0, sticky=W)
    l1_frame.grid_propagate(0)
    l1 = Label(l1_frame, text='', justify=LEFT)
    l1.grid(row=0, column=0, padx=5, sticky=W)
    
    pb_var = IntVar()
    pb = ttk.Progressbar(pb_frame, orient="horizontal", length=368, var=pb_var, mode="determinate")
    pb.grid(row=1, column=0, padx=5)
    pb["value"] = 0
    p_label = Label(pb_frame, text='')
    p_label.grid(row=1, column=0)
    p_label.grid_remove()
    
    b_frame = Frame(main3)
    b_frame.grid(row=4, column=0)
    b1 = ttk.Button(b_frame, text='Download', width=10, command=start)
    b1.grid(row=0, column=0, pady=5)
    
load = Image.open(resource_path1('tether logo.jpg'))
load = load.resize((380, 80), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(load)
logoframe = Frame(main, width=380, height=80)
logoframe.grid(row=0, column=0)
logoframe.grid_propagate(0)
logolabel = Label(logoframe, image=logo)
logolabel.pack()

bodyframe = Frame(main, width=380, height=240)
bodyframe.grid(row=1, column=0)
bodyframe.grid_propagate(0)
welcomeframe = Frame(bodyframe, width=368, height=60)
welcomeframe.grid(row=0, column=0)
welcomeframe.grid_propagate(0)

welcomelabel1 = Label(welcomeframe, text='Welcome to Tether')
welcomelabel1.grid(row=0, column=0, sticky=W)
welcomelabel2 = Label(welcomeframe, text='Choose one of the options below and \npress the \'Start\' button to carry out your command', justify=LEFT)
welcomelabel2.grid(row=1, column=0, sticky=W)

var = StringVar()

options = ttk.LabelFrame(bodyframe, text='Pick your action', width=368, height=70)
options.grid(row=1, column=0, pady=5, padx=10)
options.grid_propagate(0)

on = ttk.Radiobutton(options, text="Send", variable=var, value="Send")
var.set('Send')
on.grid(row=0, column=0, sticky=W)

off = ttk.Radiobutton(options, text="Receive", variable=var, value="Receive")
off.grid(row=1, column=0, sticky=W)

message_frame = Frame(bodyframe, width=368, height=80)
message_frame.grid(row=2, column=0)
message_frame.grid_propagate(0)
 
label = Label(message_frame, text='If you would choose the "Receive" option, MAKE SURE you \nCONNECT to the Sender\'s Wireless Network FIRST before starting', justify=LEFT)
label.grid(row=0, column=0, sticky=W)

label1 = Label(message_frame, justify=LEFT)
label1.grid(row=1, column=0, sticky=W)

label2 = Label(message_frame, justify=LEFT)
label2.grid(row=2, column=0, sticky=W)

def show_ip_frame():
    ip_frame.grid()
    ip_label.config(text='Receiver\'s IP address:')
    receive_button.grid_remove()
    receive_label_instruct.grid_remove()
    receive_framepad.config(width=113)
    ip_command.grid()
    ip_entry.focus()

receivesend_frame = Frame(main, width=380, height=40)
receivesend_frame.grid(row=2, column=0, padx=10)
receivesend_frame.grid_propagate(0)

receive_label_instruct = Label(receivesend_frame, text='Click the \'Receive\' button to \nreceive at same time', justify=LEFT)
receive_label_instruct.grid(row=0, column=0, sticky=W, pady=5, padx=10)
receive_label_instruct.grid_remove()
receive_framepad = Frame(receivesend_frame, width=120)
receive_framepad.grid(row=0, column=1)
receive_framepad.grid_propagate(0)
receive_button = ttk.Button(receivesend_frame, text='Receive', width=10, command=show_ip_frame)
receive_button.grid(row=0, column=2, sticky=E, pady=5, padx=10)
receive_button.grid_remove()

def send_button_funct():
    send_initiate() 
    changesharefolder.grid()

ip_frame = Frame(receivesend_frame, width=200)
ip_frame.grid(row=0, column=0, pady=5, padx=10)
ip_frame.grid_remove()

ip_label = Label(ip_frame, text='Sender\'s IP address:')
ip_label.grid(row=0, column=0, sticky=W, pady=5)

ipvar = StringVar()
ip_entry = ttk.Entry(ip_frame, textvariable=ipvar)
ip_entry.bind('<Return>', generate_frame)
ip_entry.grid(row=0, column=1, sticky=E, pady=5, padx=5)

ip_command = ttk.Button(receivesend_frame, text='Ok', width=10)
ip_command.bind('<Button-1>', generate_frame)
ip_command.grid(row=0, column=1, sticky=E, pady=5, padx=10)
ip_command.grid_remove()

buttonframe = Frame(main, width=380, height=40)
buttonframe.grid(row=3, column=0, padx=10)
buttonframe.grid_propagate(0)

def changeSharedFolder():
    subprocess.call('taskkill /im httpserver.exe /f >nul', shell=True, startupinfo=si)
    os.remove('index.html')
    os.remove('sender')
    send_initiate()
def changeDownloadFolder():
    os.remove('receiver')
    download_path = str(print_path_download())
    os.symlink(download_path, 'receiver')
    
paddingframeb = Frame(buttonframe, width=198, height=25)
paddingframeb.grid(row=0, column=0, padx=10)
paddingframeb.grid_propagate(0)
changesharefolder = ttk.Button(paddingframeb, text='Change Shared Folder', width=22, command=changeSharedFolder)
changesharefolder.grid(row=0, column=0, sticky=W)
changesharefolder.grid_remove()
changedownloadfolder = ttk.Button(paddingframeb, text='Change Download Folder', width=25, command=changeDownloadFolder)
changesharefolder.grid(row=0, column=0, sticky=W)
changesharefolder.grid_remove()
buttonframe_pos = Frame(buttonframe)
buttonframe_pos.grid(row=0, column=1, sticky=E, pady=5)
buttonframe_pos.grid_propagate(1)

button = ttk.Button(buttonframe_pos, text="Start", width=10)
button.grid(row=0, column=0, sticky=W, padx=10)
button.bind('<Button-1>', sel)

send_button = ttk.Button(buttonframe_pos, text='Send', width=10, command=send_button_funct)
send_button.grid(row=0, column=0, sticky=W, padx=10)
send_button.grid_remove()

quitbutton = ttk.Button(buttonframe_pos, text="Exit", width=10)
quitbutton.grid(row=0, column=1, sticky=E)  
quitbutton.bind('<Button-1>', quit_)

def backbutton_init():
    subprocess.call('tasklist |findstr httpserver.exe >http.txt', shell=True, startupinfo=si)
    http = open('http.txt', 'r')
    http_str = str(http.read())
    http.close()
    os.remove('http.txt')
    while 1:
        if len(http_str)==0:
            changesharefolder.grid_remove()
            break 
        else:
            changesharefolder.grid()
            changesharefolder.config(state='enabled')
            send_button.config(state='disabled')
            break
    main3.grid_remove()
    logoframe.grid()
    bodyframe.grid()
    welcomeframe.grid()
    welcomelabel1.grid_remove()
    welcomelabel2.config(text='You can either enter another Sender\'s IP below or\nClick on the "Change Shared Folder" button')
    options.grid_remove()
    receivesend_frame.grid()
    show_ip_frame()
    backbutton.grid_remove()
    button.grid()
    button.unbind('<Button-1>')
    button.config(state='disabled')
    changedownloadfolder.grid_remove()
    

backbutton = ttk.Button(buttonframe_pos, text='<Back', width=10, command=backbutton_init)
backbutton.grid(row=0, column=0, sticky=W, padx=10)
backbutton.grid_remove()

import atexit
@atexit.register
def restore():
    while 1:
        if os.path.exists('index.html'):
            os.remove('index.html')
            break
        else:
            break
    while 1:
        if os.path.exists('sender'):
            os.remove('sender')
            break
        else:
            break 
    while 1:
        if os.path.exists('receiver'):
            askdelete = messagebox.askyesno('Delete Download Folder', 'Do you want to make your chosen "Download Folder" default?')
            if askdelete:
                break
            else:
                os.remove('receiver')
                break 
        else:
            break 
    subprocess.call('tasklist |findstr httpserver.exe >http.txt', shell=True, startupinfo=si)
    http = open('http.txt', 'r')
    http_str = str(http.read())
    http.close()
    os.remove('http.txt')
    while 1:
        if len(http_str)==0:
            break
        else:
            subprocess.call('taskkill /im httpserver.exe /f >nul', shell=True, startupinfo=si)
            break
    main.quit()
main.mainloop()