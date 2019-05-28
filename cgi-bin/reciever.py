#!/usr/bin/python3

import cgi
import socket

form = cgi.FieldStorage()
btn = form.getfirst("btnnum", None)

print("Content-type: text/html\n")
print('<!DOCTYPE HTML><html><head><meta charset="utf-8"><title>Header</title></head><body><h1>You pressed: {}</h1>'.format(btn))

sock = socket.socket()
sock.connect(('localhost', 9090))				# 2) Connecting
print('Sending {}...'.format(btn))
sock.send(btn.encode())					# 4) Sending info

try:
		data = sock.recv(1024)			# 5) Getting response
		udata = data.decode()
		print('Got this: ', udata)
		
except KeyboardInterrupt:
	print('Caught KbdInterrupt')
	sock.close()

sock.close()

print('</body></html>')

#import time
#start_time = time.time()
