from tkinter import *
from tkinter import messagebox, ttk, filedialog
import requests, html5lib, os, subprocess, http.server, socketserver, socket, time, sys
from bs4 import BeautifulSoup 

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
          
def setPass():
    main2 = Toplevel(main)
    main2.title('Set Password')
    
    def confirm(event):
        if len(str(newpasse_var.get())) < 8 :
            errorl.grid()
            errorl.config(text='Enter a valid password of at least 8 characters long', fg='red')
        else:        
            if str(newpasse_var.get()) == str(confirmpe_var.get()):
                subprocess.call('netsh wlan set hostednetwork key="'+str(confirmpe_var.get())+'"', shell=True, startupinfo=si)
                main2.destroy()
                main2.quit()
            else:
                errorl.grid()
                errorl.config(text='Passwords mismatched!!!', fg='red')
        
            
    new_pass = Frame(main2)
    new_pass.grid(row=0, column=0, columnspan=3, pady=5, padx=5)
    
    newpasse_var = StringVar()
    confirmpe_var = StringVar()
    
    newpassl = Label(new_pass, text="New Password")
    newpassl.grid(row=0, column=0, pady=5)
    newpasse = ttk.Entry(new_pass, show='*', textvariable=newpasse_var)
    newpasse.grid(row=0, column=1, pady=5, padx=5)
    
    confirmpl = Label(new_pass, text="Confirm Password")
    confirmpl.grid(row=1, column=0, pady=5)
    confirmpe = ttk.Entry(new_pass, show='*', textvariable=confirmpe_var)
    confirmpe.grid(row=1, column=1, pady=5, padx=5)
    
        
    errorl = Label(new_pass)
    errorl.grid(row=2, column=0, pady=5)
    errorl.grid_remove()
    
    button = ttk.Button(new_pass, text='Create Password')
    button.grid(row=3, column=0, pady=5)
    button.bind('<Button-1>', confirm)
    
    main2.mainloop()
    
    
def print_path():
    f = filedialog.askdirectory(parent=main, initialdir=str(os.getcwd()), title='Choose folder to be shared')
    return f
def print_path_download():
    df = filedialog.askdirectory(parent=main, initialdir=str(os.getcwd()), title='Choose Download folder')
    return df
def sel(event):
    if var.get()=="Send":
        subprocess.call('netsh wlan show drivers |findstr Hosted >driver.txt', shell=True, startupinfo=si)
        driver_hotspot = open('driver.txt', 'r')
        driver_hotspot_str = str(driver_hotspot.read())
        driver_hotspot.close()
        os.remove('driver.txt')
        if 'Yes' in driver_hotspot_str: 
            subprocess.call('netsh wlan show hostednetwork security |findstr User >pass.txt', shell=True, startupinfo=si)
            pass_set = open('pass.txt', 'r')
            pass_set_str = str(pass_set.read()).replace('\r', '').strip('\n').split('\n')[0]
            pass_set.close()
            os.remove('pass.txt')
            if pass_set_str == '    User security key      : <Not specified>':
                setPass()
            else: 
                global pfile_save
                subprocess.call('netsh wlan start hostednetwork >nul', shell=True, startupinfo=si)
                subprocess.call('netsh wlan show hostednetwork security |findstr User >pass.txt', shell=True, startupinfo=si)
                pfile = open('pass.txt', 'r')
                pfile_save = str(pfile.read())replace('\r', '').strip('\n').split('\n')[0][29:]
                pfile.close()
                os.remove('pass.txt')
                
                subprocess.call('netsh wlan set hostednetwork key="sender1234567" >nul', shell=True, startupinfo=si)
                                
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
                options.grid_remove()
                sender_path = str(print_path())
                os.symlink(sender_path, 'sender')
                                
                label.config(text='Tell the Receiver to connect to '+socket.gethostname()+'\nwith "sender1234567" as password, on the WiFi network')
                label1.config(text='Tell the receiver to type your IP: '+real_ip+' when required')
                                
                html_file = open("index.html", "w")
                os.chdir('sender')

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
                os.chdir('..')
                javascript = '''var files, text, fLen, i, files2, cwd, cwdl;
                files = '''+str(filesname)+''';
                fLen = files.length;
                files2 = '''+str(files)+''';
                cwd = "'''+os.getcwd()+'''";
                cwdl = cwd.length;
                text = '';
                for (i = 0; i < fLen; i++) {
                  text += '<a href="'+files2[i].substr(cwdl+5)+'">'+files[i]+'</a><br>';
                }
                text += '<br>';


                document.getElementById("files").innerHTML = text;'''


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

                </body>
                </html>''' 
                
                html_file.write(html)
                html_file.close()
                subprocess.call('attrib +h +s index.html', shell=True, startupinfo=si)
                        
                subprocess.call('start "" "'+resource_path1('httpserver.exe')+'"', shell=True, startupinfo=si)
                receive_label_instruct.grid()
                receive_button.grid()
                changesharefolder.grid()
        else:
            messagebox.showerror('Missing Network Driver', "Your PC does not have the hosted network driver\nPlease update your network driver or contact a \ncomputer scientist to fix this problem \nChoose the Receive option instead")
            
    else:
        subprocess.call('netsh wlan show hostednetwork |findstr Status >status.txt', shell=True, startupinfo=si)
        status_str = open('status.txt', 'r')
        status_str_save = str(status_str.read()).strip('\r\n')
        status_str.close()
        os.remove('status.txt')
        while 1:
            if status_str_save == '    Status                 : Not started':
                break 
            else:
                subprocess.call('netsh wlan set hostednetwork key='+'"{}"'.format(pfile_save)+' >nul', shell=True, startupinfo=si)
                subprocess.call('taskkill /im httpserver.exe /f >nul', shell=True, startupinfo=si)
                subprocess.call('netsh wlan stop hostednetwork >nul', shell=True, startupinfo=si)
                os.remove('index.html')
                os.remove('sender')
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
            ip_frame.grid()
            receive_framepad.config(width=113)
            ip_command.grid()
            ip_entry.focus()
            button.grid_remove()
            send_button.grid()

def quit_(event):
    main.quit()

def send_initiate():
    sender_path = str(print_path())
    os.symlink(sender_path, 'sender')
        
    html_file = open("index.html", "w")
    os.chdir('sender')

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
    os.chdir('..')
    javascript = '''var files, text, fLen, i, files2, cwd, cwdl;
    files = '''+str(filesname)+''';
    fLen = files.length;
    files2 = '''+str(files)+''';
    cwd = "'''+os.getcwd()+'''";
    cwdl = cwd.length;
    text = '';
    for (i = 0; i < fLen; i++) {
      text += '<a href="'+files2[i].substr(cwdl+5)+'">'+files[i]+'</a><br>';
    }
    text += '<br>';


    document.getElementById("files").innerHTML = text;'''


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

    </body>
    </html>''' 
    
    html_file.write(html)
    html_file.close()
    subprocess.call('attrib +h +s index.html', shell=True, startupinfo=si)                
    subprocess.call('start "" "'+resource_path1('httpserver.exe')+'"', shell=True, startupinfo=si)
    ip_str = subprocess.run('ping '+socket.gethostname()+' -4', shell=True, startupinfo=si, stdout=subprocess.PIPE).stdout.decode('ascii').replace('\r', '').strip('\n').split('\n')[0]
    ip_str_start = ip_str.find('[')+1
    real_ip = ip_str[ip_str_start:].replace('] with 32 bytes of data:', '')
    label.config(text='Tell the Sender to type your IP: '+real_ip+' when required')
    changesharefolder.grid()
    
def generate_frame(event):
    while 1:
        if ipvar.get()=="":
            messagebox.showerror('Incorrect IP', 'You entered an incorrect IP address')
            ip_entry.focus()
            return
        else:
            break
    while 1:
        if os.path.exists('receiver'):
            break
        else:
            download_path = str(print_path_download())
            os.symlink(download_path, 'receiver')
            break
    
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
        file_links = []
        for link in links:
            a = str(link)
            ap = a.find('files2 = ')
            l = a[ap:].split('\n')[0].strip('files2 = ;').replace("'", "").strip('[]').split(', ')
            for lm in l:
                file_links.append(archive_url+lm[len(os.getcwd())+6:].replace('\\\\', '\\').replace('\\', '/'))
        return file_links 
    def download_file_series(file_links):
        os.chdir('receiver')
        n=1
        for link in file_links: 
            file_name = link.split('/')[-1] 
            l1.config(text='Donwloading... \n%s'%file_name)
            r = requests.get(link, stream=True)
            with open(file_name, 'wb') as f: 
                for chunk in r.iter_content(chunk_size = 1024*1024):
                    if chunk:
                        f.write(chunk)
            
            while n<len(file_links)+1:
                pb['maximum'] = len(file_links)
                pb_var.set(n)
                n+=1
                time.sleep(0.5)
                pb_frame.update()
                break 
        l1.config(text='')
        messagebox.showinfo('Successful Download', 'All files are successfully downloaded!')
        os.chdir('..')
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
        else:
            for item in check_buttons.values():
                item.set('')
            bcheckall.config(text='Select all')
        return
    def closemain3():
        main3.destroy()
        main3.quit()
    
    max_vlinks = get_file_links()
    check_buttons = {item:StringVar() for item in max_vlinks}
   
    def init_checkbutton(frame):    
        r=0
        for item in max_vlinks:
            C = ttk.Checkbutton(frame, text=str(item.split('/')[-1]), variable=check_buttons[item], onvalue=str(item), offvalue='').grid(row=r, column=0, sticky=W, padx=5)
            r+=1
    def onFrameConfigure(canvas):
        canvas.configure(scrollregion=canvas.bbox("all"))

    framewindow = Frame(main3, width=368, height=225)
    framewindow.grid(row=0, column=0)
    framewindow.grid_propagate(0)
    
    canvas = Canvas(framewindow, width=353, height=225)
    frame = Frame(canvas)
    vsb = Scrollbar(framewindow, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)
    
    vsb.pack(side="right", fill='y')
    canvas.pack(side="left", fill='both', expand=1)
    
    canvas.create_window((0,0), window=frame, anchor="nw")
    
    canvas.bind_all('<MouseWheel>', lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))
    
    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    
    init_checkbutton(frame)
    
    bcheckall_var = IntVar()
    
    bcheckall = ttk.Checkbutton(main3, text='Select all', variable=bcheckall_var, onvalue=1, offvalue=0, command=selectall)
    bcheckall.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        
    pb_frame = Frame(main3)
    pb_frame.grid(row=2, column=0)
    l1_frame = Frame(pb_frame, width=368, height=35)
    l1_frame.grid(row=0, column=0, sticky=W)
    l1_frame.grid_propagate(0)
    l1 = Label(l1_frame, text='', justify=LEFT)
    l1.grid(row=0, column=0, padx=5, sticky=W)
    
    pb_var = IntVar()
    pb = ttk.Progressbar(pb_frame, orient="horizontal", length=368, maximum=len(check()), var=pb_var, mode="determinate")
    pb.grid(row=1, column=0, padx=5, sticky=W)
    pb["value"] = 0
    
    b_frame = Frame(main3)
    b_frame.grid(row=3, column=0)
    b1 = ttk.Button(b_frame, text='Download', width=10, command=start)
    b1.grid(row=0, column=0, pady=5)
    
logoframe = Frame(main, width=380, height=80)
logoframe.grid(row=0, column=0)

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
ip_label.grid(row=0, column=0, sticky=W, pady=5, padx=5)

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
    main3.grid_remove()
    logoframe.grid()
    bodyframe.grid()
    welcomelabel1.config(text='')
    welcomelabel2.config(text='You can either enter another Sender\'s IP below or\nClick on the "Change Shared Folder" button')
    options.grid_remove()
    receivesend_frame.grid()
    show_ip_frame()
    backbutton.grid_remove()
    button.grid()
    button.unbind('<Button-1>')
    button.config(state='disabled')
    changesharefolder.config(state='enabled')
    

backbutton = ttk.Button(buttonframe_pos, text='<Back', width=10, command=backbutton_init)
backbutton.grid(row=0, column=0, sticky=W, padx=10)
backbutton.grid_remove()

import atexit
@atexit.register
def restore():
    subprocess.call('netsh wlan show hostednetwork |findstr Status >status.txt', shell=True, startupinfo=si)
    status_str = open('status.txt', 'r')
    status_str_save = str(status_str.read()).strip('\r\n')
    status_str.close()
    os.remove('status.txt')
    if status_str_save == '    Status                 : Not started':
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
    
    else:
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
                
        subprocess.call('netsh wlan set hostednetwork key='+'"{}"'.format(pfile_save)+' >nul', shell=True, startupinfo=si)
        subprocess.call('taskkill /im httpserver.exe /f >nul', shell=True, startupinfo=si)
        subprocess.call('netsh wlan stop hostednetwork >nul', shell=True, startupinfo=si)
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
        main.quit()
main.mainloop()