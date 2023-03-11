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
main.iconbitmap(resource_path1('favicon.ico'))
          
def setPass():
    bodyframe.grid_remove()
    main2 = Frame(main, width=380, height=240)
    main2.grid(row=1, column=0)
    main2.grid_propagate(0)    
    def confirm(event):
        if len(str(newpasse_var.get())) < 8 :
            messagebox.showerror('Password Length Error', 'Enter a valid password of at least 8 characters long')
        else:        
            if str(newpasse_var.get()) == str(confirmpe_var.get()):
                subprocess.call('netsh wlan set hostednetwork key="'+str(confirmpe_var.get())+'" >nul', shell=True, startupinfo=si)
                main2.grid_remove()
                bodyframe.grid()
                sel(event)
                
            else:
                messagebox.showerror('Mismach error', 'Passwords mismatched!!!')
        
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
    confirmpe.bind('<Return>', confirm)
    
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
def showConnectedIp():
    subprocess.call('arp /a >ip.txt', shell=True, startupinfo=si)
    f = open('ip.txt', 'r')
    ip_str = f.read()
    # if (ip_str == 'No ARP Entries Found'):
    #     messagebox.showerror('Error', 'Your Wireless Network is currently switched off.\nSwitch on your Wireless Network and restart the "Send" option.')
    #     return
    real_ipTreat = ip_str.split('Interface: ')
    # real_ip = real_ipTreat[-1][:real_ipTreat[-1].find(' ---')]
    connIp = real_ipTreat[-1].split('\n')
    treatIp = []
    for ip in connIp:
        if (connIp[0] == ip or connIp[1] == ip):
            continue
        treatIp.append(ip)
    rawIp = []
    for ip in treatIp:
        if (ip == '' or 'ff-ff-ff-ff-ff-ff' in ip):
            break
        rawIp.append(ip[:-33])
    finishedConnIps = []
    for ip in rawIp:
        finishedConnIps.append(ip.strip('  ').strip('      '))
    
    f.close()
    os.remove('ip.txt')
    return finishedConnIps

def getIp():
    global real_ip                
    subprocess.call('arp /a >ip.txt', shell=True, startupinfo=si)
    ip = open('ip.txt', 'r')
    ip_str = ip.read()
    if ('No ARP Entries Found' in ip_str):
        return 1
    real_ipTreat = ip_str.split('Interface: ')
    real_ip = real_ipTreat[-1][:real_ipTreat[-1].find(' ---')]
    ip.close()
    os.remove('ip.txt')
    return 0

def getSenderIp():
    subprocess.call('arp /a >ip.txt', shell=True, startupinfo=si)
    ip = open('ip.txt', 'r')
    senderIp = ip.read().split('Interface: ')[-1].split('\n')[2][:-33].strip('  ').strip('      ')
    ip.close()
    os.remove('ip.txt')
    return senderIp

def genHTML(filesname, files, filesize):
    javascript = '''var files, text, fLen, i, files2, cwd, cwdl;
                files = '''+str(filesname)+''';
                fLen = files.length;
                files2 = '''+str(files)+''';
                cwd = "'''+os.getcwd()+'''";
                cwdl = cwd.length;
                text = '';
                for (i = 0; i < fLen; i++) {
                    text += '<input type="checkbox" class="mycheckboxes" name="'+files[i]+'" value="'+files2[i].substr(files2[i].indexOf("sender"))+'"><a href="'+files2[i].substr(files2[i].indexOf("sender"))+'" download>'+files[i]+'</a><br>';
                }
                document.getElementById("links-inner").innerHTML = text;
                var checkboxes = document.getElementsByClassName("mycheckboxes");
                function downloadFile() {
                    for (i=0; i<checkboxes.length; i++) {
                        if (checkboxes[i].checked) {
                            var downloadlink = document.createElement('a');
                            downloadlink.setAttribute("href", checkboxes[i].value);
                            downloadlink.setAttribute("download", checkboxes[i].name);
                            downloadlink.click();
                        } else {
                            continue;
                        }
                    }
                }
                function checkall() {
                    if (document.getElementById("checkall").innerHTML == "Select All") {
                        for (i=0; i<checkboxes.length; i++) {checkboxes[i].checked = true}
                        document.getElementById("checkall").innerHTML = "Deselect All";    
                    } else {
                        for (i=0; i<checkboxes.length; i++) {checkboxes[i].checked = false}
                        document.getElementById("checkall").innerHTML = "Select All";
                    }
                }
                '''

    javascript2 = str(filesize)
    html = '''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Tether</title>
                <link rel="icon" href="favicon.png" type="image/png">
                <style>
                .circle {
    background-color:white;
    box-shadow:0 0 20px white, 0 0 20px darkblue, 0 0 20px white;
    height:6.0%;
    width:1.4%;
    border-radius:100%;
}
.rightdiv, .leftdiv {
    display:none;
    height:11.3%; 
    width:2.9%;
    background-color:white;
    border:8px solid rgba(0, 0, 139, 0.61);
    box-shadow: 0 0 20px white, 0 0 10px darkblue, 0 0 20px white;
    animation: glow 1s;
}
.bottomdiv {
    display:block;
    height:11.3%; 
    width:2.9%;
    background-color:white;
    border:8px solid rgba(0, 0, 139, 0.61);
    box-shadow: 0 0 20px white, 0 0 10px darkblue, 0 0 20px white;
}
@keyframes glow {
    from {opacity:0.1;}
    to {opacity:1;}
}
.image-container {
    position:relative; 
    margin:0; 
    padding:0; 
    height:330px; 
    width:100%
}
.links-container {
    width:100%;
    display:block;
    padding:30px;
    margin:0;
    box-sizing:border-box;
}
#links {
    width:80%;
    background-color:white;
    font-family:Verdana, sans-serif;
    font-size:16px;
    border-radius:15px;
    box-shadow: 0 0 20px rgba(0, 0, 139, 0.3);
    padding:20px;
    box-sizing:border-box;
    overflow-x:auto;
    margin:auto;
    white-space:nowrap;
}
#welcometext { 
    width:70%;
    font-family:Verdana, sans-serif;
    color:blue;
    font-size:35px;
    text-align:center;
    margin:auto;
    font-weight:bold;
}
#instruction {
    text-align:center;
    width:70%;
    font-size:17px;
    font-family:Verdana, sans-serif;
    box-sizing:border-box;
    margin:auto;
}
#checkall {
    border:none;
    display:block;
    background-color:blue;
    width:35%;
    padding:10px 10px;
    border-radius:50px;
    cursor:pointer;
    font-size:16px;
    color:white;
}
#checkall:hover {
    background-color:darkblue;
}
#button {
    background-color:darkblue;
    width:55%;
    display:block;
    margin:auto;
    padding:15px 10px;
    border:none;
    border-radius:50px;
    cursor:pointer;
    color:white;
    text-align:center;
    font-size:18px;
}
#button:hover {
    background-color:blue;
    box-shadow:2px 2px 5px blue;
}
a {
    text-decoration:none;
}
a:hover {
    text-decoration:underline;
}
#links-inner {
    max-height:200px;
    overflow:auto;
    white-space:nowrap;
    margin:20px 0;
}
                </style>
            </head>
            <body style="padding:0; margin:0; background-color:rgba(137, 137, 255, 0.2);">
                <header>
                    <div class="image-container">
                        <img src="tether logo.jpg" style="width:100%; height:100%; margin:0; padding:0;">
                        <div class="circle" style="position:absolute; top:56.4%; left:24.5%;"></div>
                        <div class="circle" style="position:absolute; top:56.4%; left:24.5%;"></div>
                        <div class="leftdiv" style="position:absolute; top:4.8%; left:14.5%;"></div>
                        <div class="rightdiv" style="position:absolute; top:4.8%; left:31.5%;"></div>
                        <div class="bottomdiv" style="position:absolute; top:51.8%; left:23.0%;"></div>
                    </div>
                </header>
                <div class="links-container">
                    <div id="welcometext">Welcome to Tether</div>
                    <div id="instruction"><p>Select your desired files and click the "Download" button to initiate the download process, or individually click your desired file(s) to download</p></div>
                    <div id="links">
                    <button id="checkall" onclick="checkall()">Select All</button><br>
                    <div id="links-inner"></div>
                    <input type="button" id="button" onclick="downloadFile()" value="Download">
                    </div>
                </div>
                <script>'''+javascript+'''

                </script>
                <script>
                windowwidth = window.innerWidth || document.body.clientWidth || document.documentElement.clientWidth;
if (windowwidth < 600 && windowwidth > 249) {setDim300();};
if (windowwidth < 1349 && windowwidth > 889) {setDim900();};
function setDim900() {
    var calcheight = (windowwidth*330)/1349;
    var imagecontainer = document.getElementsByClassName("image-container");
    var leftdiv = document.getElementsByClassName("leftdiv");
    var rightdiv = document.getElementsByClassName("rightdiv");
    var bottomdiv = document.getElementsByClassName("bottomdiv");
    imagecontainer[0].style.height = calcheight + "px";
    leftdiv[0].style.border = "5px solid rgba(0, 0, 139, 0.61)"
    rightdiv[0].style.border = "5px solid rgba(0, 0, 139, 0.61)";
    bottomdiv[0].style.border = "5px solid rgba(0, 0, 139, 0.61)";
};
function setDim300() {
    var calcheight = (windowwidth*330)/1349;
    var imagecontainer = document.getElementsByClassName("image-container");
    var links = document.getElementById("links");
    var instruction = document.getElementById("instruction");
    var welcometext = document.getElementById("welcometext");
    var checkallb = document.getElementById("checkall");
    var button = document.getElementById("button");
    var leftdiv = document.getElementsByClassName("leftdiv");
    var rightdiv = document.getElementsByClassName("rightdiv");
    var bottomdiv = document.getElementsByClassName("bottomdiv");
    var circles = document.getElementsByClassName("circle");
    var linksInner = document.getElementById("links-inner");
    linksInner.style.margin = "10px 0";
    linksInner.style.maxHeight = "250px";
    for (var i=0; i<circles.length; i++) {circles[i].style.boxShadow = "0 0 20px white, 0 0 20px darkblue, 0 0 20px white";};
    leftdiv[0].style.border = "2px solid rgba(0, 0, 139, 0.61)"
    rightdiv[0].style.border = "2px solid rgba(0, 0, 139, 0.61)";
    bottomdiv[0].style.border = "2px solid rgba(0, 0, 139, 0.61)";
    imagecontainer[0].style.height = calcheight + "px";
    links.style.fontSize = "12px";
    links.style.borderRadius = "10px";
    links.style.border = "1px solid blue";
    links.style.padding = "10px";
    instruction.style.fontSize = "12px";
    welcometext.style.fontSize = "20px";
    checkallb.style.padding = "5px";
    checkallb.style.fontSize = "12px";
    checkallb.style.width = "60%";
    button.style.padding = "10px";
    button.style.fontSize = "14px";
    button.style.width = "70%";
}
circlepos = document.getElementsByClassName("circle");
setInterval(moves, 3000);
function moves() {
    var pos = 0;
    for (var h = 0; h < circlepos.length; h++) {
        circlepos[h].style.top = "56.4%";
        circlepos[h].style.left = "24.5%";
    }
    var moveInterval = setInterval(movecircles, 5);
    document.getElementsByClassName("leftdiv")[0].style.display = "none";
    document.getElementsByClassName("rightdiv")[0].style.display = "none";
    document.getElementsByClassName("bottomdiv")[0].style.display = "block";
    function movecircles() {
        if (pos == 313) {
            move2();
            clearInterval(moveInterval);
        } else {
            pos += 1;
            if (pos == 46) {
                document.getElementsByClassName("bottomdiv")[0].style.display = "none";
                for (var l=0; l < circlepos.length; l++) {circlepos[l].style.top = "39.2%";}    
            }
            for (var i=0; i < circlepos.length; i++) {
                var finalpos = ((((circlepos[i].style.top).replace("%","")/1)*10) - (0.1*10))/10;
                circlepos[i].style.top = finalpos + "%";
            }
        }
    }
}
function move2() {
    var pos2 = 0;
    var moveInterval2 = setInterval(movecircles2, 10);
    function movecircles2() {
        if (pos2 == 52) {
            clearInterval(moveInterval2);
        } else {
            pos2 += 1;
            if (pos2 == 37) {
                document.getElementsByClassName("leftdiv")[0].style.display = "block";
                document.getElementsByClassName("rightdiv")[0].style.display = "block";
                for (n = 0; n < circlepos.length; n++) {
                    if (n == 0) {circlepos[n].style.left = "31.6%"}
                    else {circlepos[n].style.left = "17.0%"}
                }
            }
            for (var j=0; j < circlepos.length; j++) {
                if (j == 0) {
                    var finalpos2 = ((((circlepos[j].style.left).replace("%","")/1)*10) + (0.1*10))/10;
                    circlepos[j].style.left = finalpos2 + "%";
                } else {
                    var finalpos2 = ((((circlepos[j].style.left).replace("%","")/1)*10) - (0.1*10))/10;
                    circlepos[j].style.left = finalpos2 + "%";
                }
            }
        }
    }
}
                </script>
                <script>'''+javascript2+'''
                </script>
                </body>
                </html>''' 
    return html

def sel(event):
    button.config(text="Starting...")
    button.unbind('<Button-1>')
    main.update_idletasks()
    if var.get()=="Send":
        global initOpt 
        initOpt = 0
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
            if pass_set_str == '    User security key      : <Not specified>' or pass_set_str == '    User security key      : tether1234567':
                setPass()
            else: 
                global pfile_save
                subprocess.call('netsh wlan start hostednetwork >nul', shell=True, startupinfo=si)
                subprocess.call('netsh wlan show hostednetwork security |findstr User >pass.txt', shell=True, startupinfo=si)
                pfile = open('pass.txt', 'r')
                pfile_save = str(pfile.read()).replace('\r', '').strip('\n').split('\n')[0][29:]
                pfile.close()
                os.remove('pass.txt')
                
                subprocess.call('netsh wlan set hostednetwork key="tether1234567" >nul', shell=True, startupinfo=si)
                ipStatus = getIp()
                if (ipStatus == 1):
                    messagebox.showerror('Network Error', 'Switch on your Wireless Network or WiFi and try again')
                    button.config(text="Start")
                    button.bind('<Button-1>', sel)
                    main.update_idletasks()
                    return
                
                if os.path.exists('sender'):
                    os.remove('sender')
                
                if os.path.exists('index.html'):
                    os.remove('index.html')
                     
                askfolderorfile = messagebox.askyesno('Folder or Files', 'Do you want to share a folder?\nClick "No" to share files')
                while 1:
                    if askfolderorfile:
                        sender_path = str(print_path())
                        while 1:
                            if sender_path == '':
                                messagebox.showerror('Error', 'You must choose a folder')
                                sender_path = str(print_path())
                            else:
                                os.symlink(sender_path, 'sender')
                                break
                        os.chdir('sender')

                        for r, d, f in os.walk(os.getcwd()):
                            for file in f:
                                if '.' in file:
                                    if ',' in file or '%' in file:
                                        os.rename(os.path.join(r, file),os.path.join(r, file).replace(',',' ').replace('%',''))
                        files = []

                        for r, d, f in os.walk(os.getcwd()):
                            for file in f:
                                if '.' in file:
                                    files.append(os.path.join(r, file))
                        
                        filesname = []
                        for r, d, f in os.walk(os.getcwd()):
                            for file in f:
                                if '.' in file:
                                    filesname.append(os.path.basename(os.path.join(r, file)))
                        
                        filesize = {}
                        for r, d, f in os.walk(os.getcwd()):
                            for file in f:
                                if '.' in file:
                                    filesize.update([(os.path.join(r, file),os.path.getsize(os.path.join(r, file)))])

                        os.chdir('..')
                        break
                    else:
                        files_untreated = list(filedialog.askopenfilenames(parent=main, initialdir=str(os.getcwd()), title="Choose Files to be Shared"))
                        filesnofolder = []
                        files = []
                        filesname = []
                        filesize = {}
                        sender_folder = ''
                        for file in files_untreated:
                            if ',' in file or '%' in file:
                                os.rename(file, file.replace(',',' ').replace('%',''))
                        for file in files_untreated:
                            if ',' in file or '%' in file:
                                filesnofolder.append(file.replace(',', ' ').replace('%', ''))
                            else:
                                filesnofolder.append(file)
                        for file in filesnofolder:
                            sender_folder = sender_folder+os.path.dirname(file)
                            break
                        os.chdir(os.getcwd())
                        os.symlink(sender_folder, 'sender')
                        for file in filesnofolder:
                            files.append(os.path.join(sender_folder.replace(sender_folder, os.path.join(os.getcwd(), 'sender')), os.path.basename(file)))
                        for file in files:
                            filesname.append(os.path.basename(file))
                        for file in files:
                            filesize.update([(file,os.path.getsize(file))])
                        
                        break
                
                html_file = open("index.html", "wb")
                
                html = genHTML(filesname, files, filesize)
                
                html_file.write(html.encode('utf-8'))
                html_file.close()
                subprocess.call('attrib +h +s index.html', shell=True, startupinfo=si)
                        
                subprocess.call('start "" "'+resource_path1('httpserver.exe')+'"', shell=True, startupinfo=si)
                options.grid_remove()
                message_frame.config(height=230)
                label.config(text='Tell the Receiver to connect to '+socket.gethostname()+'\nwith "tether1234567" as password, on the WiFi network')
                label1.config(text='Tell the receiver to type your IP: '+real_ip+' when required')
                label2.config(text='In case your receiver wants to use the browser, '+real_ip+':8888\nshould be used')
                welcomeframe.grid_remove()
                button.config(state='disabled')
                button.unbind('<Button-1>')
                receive_label_instruct.grid()
                receive_button.grid()
                changesharefolder.grid()
                button.config(text="Start")
                main.update_idletasks()
        else:
            button.config(text="Start")
            main.update_idletasks()
            messagebox.showerror('Missing Network Driver', "Your PC does not have the hosted network driver\nPlease update your network driver or contact a \ncomputer scientist to fix this problem \nChoose the Receive option instead")
            
    else:
        # global initOpt 
        initOpt = 1
        ipStatus = getIp()
        if (ipStatus == 1):
            button.config(text="Start")
            button.bind('<Button-1>', sel)
            main.update_idletasks()
            messagebox.showerror('Network not found', 'Connect to the Sender\'s Wireless Network first')
            return 
        welcomeframe.grid_remove()
        options.grid_remove()
        label.config(text='Click the "Send" button, if you want to send at the same time')
        label1.config(text="Ask your sender to reveal his/her \nIP address to you. Then type it when required")
        show_ip_frame()
        ip_label.config(text='Sender\'s IP address:')
        button.grid_remove()
        send_button.grid()
        while 1:
            if (int(getSenderIp().split('.')[0]) != 192):
                getSenderIp()
            else:
                break

        ipvar.set(getSenderIp())
        button.config(text="Start")
        main.update_idletasks()

def quit_(event):
    confirmexit = messagebox.askyesno('Exit Confirmation', 'Are you sure you want to exit?')
    if confirmexit:
        main.quit()
    else:
        return

def send_initiate():
    if os.path.exists('sender'):
        os.remove('sender')
    if os.path.exists('index.html'):
        os.remove('index.html')
    
    askfolderorfile = messagebox.askyesno('Folder or Files', 'Do you want to share a folder?\nClick "No" to share files')
    while 1:
        if askfolderorfile:
            sender_path = str(print_path())
            while 1:
                if sender_path == '':
                    messagebox.showerror('Error', 'You must choose a folder')
                    sender_path = str(print_path())
                else:
                    os.symlink(sender_path, 'sender')
                    break
            os.chdir('sender')

            for r, d, f in os.walk(os.getcwd()):
                for file in f:
                    if '.' in file:
                        if ',' in file or '%' in file:
                            os.rename(os.path.join(r, file),os.path.join(r, file).replace(',',' ').replace('%',''))        
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
            break
        else:
            files_untreated = list(filedialog.askopenfilenames(parent=main, initialdir=str(os.getcwd()), title="Choose Files to be Shared"))
            filesnofolder = []
            files = []
            filesname = []
            filesize = {}
            sender_folder = ''
            for file in files_untreated:
                if ',' in file or '%' in file:
                    os.rename(file, file.replace(',',' ').replace('%',''))
                else:
                    continue
            for file in files_untreated:
                if ',' in file or '%' in file:
                    filesnofolder.append(file.replace(',', ' ').replace('%', ''))
                else:
                    filesnofolder.append(file)
            for file in filesnofolder:
                sender_folder = sender_folder+os.path.dirname(file)
                break
            os.chdir(os.getcwd())
            os.symlink(sender_folder, 'sender')
            for file in filesnofolder:
                files.append(os.path.join(sender_folder.replace(sender_folder, os.path.join(os.getcwd(), 'sender')), os.path.basename(file)))
            for file in files:
                filesname.append(os.path.basename(file))
            for file in files:
                filesize.update([(file,os.path.getsize(file))])
            break
    
    html_file = open("index.html", "wb")
    
    html = genHTML(filesname, files, filesize)
    
    html_file.write(html.encode('utf-8'))
    html_file.close()
    subprocess.call('attrib +h +s index.html', shell=True, startupinfo=si)                
    subprocess.call('start "" "'+resource_path1('httpserver.exe')+'"', shell=True, startupinfo=si)
    getIp()
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
                if 'sender' in lm:
                    untreated_files.append(archive_url+lm[lm.find('sender'):].replace('\\\\', '\\').replace('\\', '/'))
                else:
                    untreated_files.append(archive_url+lm.replace('\\\\', '\\').replace('\\', '/').split('/')[-1])
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
        actual_sizes = sizes_l[2].getText()
        size_dic_list = actual_sizes.replace('{','').replace('}','').replace('\n','').split(', ')
        for item in size_dic_list:
            item_list = item.split(':')
            if len(item_list)!=3:
                print(item_list)
                continue
            if 'sender' in item_list[1]:
                item_list[1] = archive_url+item_list[1][item_list[1].find('sender'):].replace('\\\\', '\\').replace('\\', '/')
            else:
                item_list[1] = archive_url+item_list[1].replace('\\\\', '\\').replace('\\', '/').split('/')[-1]
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
def setIpVar():
    # print(iptext.get())
    ipvar.set(iptext.get())

def init_radiobutton(frame):
    r = 0
    for ip in showConnectedIp():
        radio = ttk.Radiobutton(frame, text=ip, variable=iptext, value=ip)
        radio.grid(row = r, column=0, sticky=W)
        r += 1

iptext = StringVar()
def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def refreshIp(frame):
    frame.destroy()
    if len(showConnectedIp()) > 6:  
        subprocess.call('arp -d *', shell=True, startupinfo=si)
    showIpListFrame()

def showIpListFrame():
    iplist = Frame(message_frame, width=380, height=100)
    iplist.grid(row=3, column=0)
    # iplist.grid_remove()
    testing = Label(iplist, text="Choose the matching receiver's IP,\nthen click the 'Set IP' button")
    testing.grid(row=0, column=0, ipady=5)
    ipframewindow = Frame(iplist, width=250, height=90)
    ipframewindow.grid(row=1, column=0)
    ipframewindow.grid_propagate(0)

    ipcanvas = Canvas(ipframewindow, width=200, height=90)
    ipframe = Frame(ipcanvas, bd=5)
    ipvsb = Scrollbar(ipframewindow, orient="vertical", command=ipcanvas.yview)
    # hsb = Scrollbar(iplist, orient='horizontal', command=canvas.xview)
    ipcanvas.configure(yscrollcommand=ipvsb.set)

    ipvsb.pack(side="right", fill='y')
    # hsb.pack(side='bottom', fill='x')
    ipcanvas.pack(side="left", fill='both', expand=1)

    ipcanvas.create_window((0,0), window=ipframe, anchor="nw")

    ipcanvas.bind_all('<MouseWheel>', lambda event: ipcanvas.yview_scroll(int(-1*(event.delta/120)), "units"))

    ipframe.bind("<Configure>", lambda event, canvas=ipcanvas: onFrameConfigure(canvas))

    init_radiobutton(ipframe)

    btnContainer = Frame(iplist, width=130, height=90)
    btnContainer.grid(row=1, column=1)
    setbtn = ttk.Button(btnContainer, text="Set IP", command=setIpVar)
    setbtn.grid(row=0, column=0, padx=5)
    refreshbtn = ttk.Button(btnContainer, text="Refresh IP List", command=lambda ipframe=ipframe: refreshIp(ipframe))
    refreshbtn.grid(row=1, column=0, padx=5)

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
welcomeframe = Frame(bodyframe, width=380, height=70)
welcomeframe.grid(row=0, column=0)
welcomeframe.grid_propagate(0)

welcomelabel1 = Label(welcomeframe, text='Welcome to Tether', font='ravie', fg='blue')
welcomelabel1.grid(row=0, column=0, sticky=E)

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

message_frame = Frame(bodyframe, width=380, height=70)
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
    showIpListFrame()

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

initOpt = -1

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
    if len(http_str)==0:
        changesharefolder.grid_remove()
    else:
        changesharefolder.grid()
        changesharefolder.config(state='enabled')
        send_button.config(state='disabled')
    main3.grid_remove()
    logoframe.grid()
    bodyframe.grid()
    # welcomeframe.grid()
    welcomelabel1.grid_remove()
    # welcomelabel2.config(text='You can either enter another Sender\'s IP below or\nClick on the "Change Shared Folder" button')
    options.grid_remove()
    receivesend_frame.grid()
    show_ip_frame()
    if (initOpt == 1):
        ip_label.config(text="Sender's IP address:")
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
    quitbutton.config(text="Exiting...")
    main.update_idletasks()
    subprocess.call('netsh wlan show drivers |findstr Hosted >driver.txt', shell=True, startupinfo=si)
    driver_hotspot = open('driver.txt', 'r')
    driver_hotspot_str = str(driver_hotspot.read())
    driver_hotspot.close()
    os.remove('driver.txt')
    if 'Yes' in driver_hotspot_str: 
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
    else:
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