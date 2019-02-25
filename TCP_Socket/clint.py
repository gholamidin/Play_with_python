#!/usr/bin/python3
import socket

# Address
HOST = '127.0.0.1'
PORT = 8000
request = 'can you hear me?'
# configure socket
fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
fd.connect((HOST, PORT))

#客户端发送一个Request
fd.sendall(request.encode())

#接受来自Server的reply
reply = fd.recv(1024)
print('reply is : ',reply)

#close connection
fd.close()

