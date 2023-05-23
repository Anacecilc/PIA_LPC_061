#Ana cecilia Lopez castillo
#1996528
#PARTE 1
import socket

#PARTE 2
def scan (addr, port):
	socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	
	result = socket_obj.connect_ex((addr,port))

	socket_obj.close()
	return result

#PARTE 3
ports=[21,22,25,80]

#PARTE 4
for i in range (1,255):
	addr="192.168.0.{}".format(i)
	for port in ports:
		result= scan(addr, port)
		if result ==0:		
			print(addr, port, "OK")
		else:
			print(addr, port, "Failed")