#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
from RPi import GPIO 
from time import sleep 

pinA=22 #Ahead
pinB=23 #Backwards

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
GPIO.setup(pinA, GPIO.OUT)
GPIO.setup(pinB, GPIO.OUT)

def blinker():							# Нужно выводить в отдельный поток, чтобы не останавливал работу сервера
	try: 
		while True: 
			GPIO.output(pinA, True) 
			sleep(0.5) 
			GPIO.output(pinA, False) 
			sleep(0.5) 
	except KeyboardInterrupt: 
		print('program stop')
		GPIO.cleanup()


print('Starting server on port {}'.format('9090'))
sock = socket.socket()
sock.bind(('', 9090))						# 1) Creating socket

def scktsrv():
	sock.listen(2)						# 2) Waiting for clients
	conn, addr = sock.accept()
	print('connected: ', addr)					# 3) Someone connected
	while True:
			data = conn.recv(1024)			# 4) Waiting for info
			if not data:
				break
			udata = data.decode()			# 5) Getting info
			if udata == "1":
				GPIO.output(pinB, False)
				GPIO.output(pinA, True)
				print('Forward')
			elif udata == "2":
				GPIO.output(pinA, False)
				GPIO.output(pinB, False)
				print('Stop')
			elif udata == "3":
				GPIO.output(pinA, False)
				GPIO.output(pinB, True)
				print('Revers')
#			print('Recieved: ', udata)
#			conn.send(udata.encode())			# 6) Answering

try:
	while True:
		scktsrv()
except KeyboardInterrupt:
	print("This is KeyboardInterrupt!")
	sock.close()
	GPIO.cleanup()