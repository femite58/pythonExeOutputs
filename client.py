import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()
port = 9999
s.connect((host, port))
while 1:
    rcvmsg = s.recv(1024) 
    print (str(host)+': '+rcvmsg.decode('ascii'))
    msg = input('Enter you message:')
    s.send(msg.encode('ascii'))
    s.shutdown()