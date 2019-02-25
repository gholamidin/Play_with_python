#!/usr/bin/python3

import socket

#Address
HOST = '127.0.0.1'
PORT = 8000

listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listenfd.bind((HOST,PORT))

listenfd.listen(3)

connectfd, addr = listenfd.accept()

#receive massage
request = connectfd.recv(1024)
print ('The request is : ',request)
print ('Connected by : ',addr)

#send massage
reply = 'Yes!'
connectfd.sendall(reply.encode())

#close connection
connectfd.close()
