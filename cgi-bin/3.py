#!/usr/bin/python3
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
print('Sending 3')
sock.send('3'.encode())

data = sock.recv(1024).decode()
sock.close()
