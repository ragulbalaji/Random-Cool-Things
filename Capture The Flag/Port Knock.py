# Simple Port Knocker

import socket

ports = [12345, 23456, 34567, 45678, 56789]

def knock(port):
	s = socket.socket()
	try:
		print("Knocking " + str(port))
		s.connect(("URL_goes_here", port))
	except Exception, e:
		print("Warn: %s" % (e))
	s.close()

for port in ports:
	knock(port);