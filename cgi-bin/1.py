#!/usr/bin/python3
import socket

try:
	sock = socket.socket()
	sock.connect(('localhost', 9090))
#	print('Sending 1')
	sock.send('1'.encode())
	data = sock.recv(1024).decode()
#	print('Content-type: text/html\n')
#	print('<!DOCTYPE HTML><html><head><meta charset="utf-8"><title>Script №1 page</title></head><body>I hope there is "1"</body></html>')

except Exception:
	sock.close()
