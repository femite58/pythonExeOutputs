import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname() 
port = 9999
serversocket.bind((host, port))

serversocket.listen(5)
clientsocket, addr = serversocket.accept()
print ("Got a connection from %s" %str(addr))
while True:     
    msg = input('Enter your message:')
    clientsocket.send(msg.encode('ascii'))
    rcvmsg = clientsocket.recv(1024)
    print(str(addr)+': '+rcvmsg.decode('ascii'))