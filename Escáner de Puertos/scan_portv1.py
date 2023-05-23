#!/usr/bin/python
# -*- coding: utf-8 -*-

#Ana Cecilia Lopez Castillo
#1996528

#PARTE 1

import sys
from socket import *

#PARTE 2

host= sys.argv[1]
portstrs= sys.argv[2].split('-')

#PARTE 3

start_port= int(portstrs[0])
end_port= int(portstrs[1])

#PARTE 4

target_ip= gethostbyname(host)
opened_ports =[]

#PARTE 5

for port in range(start_port, end_port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.settimeout(10)
	result= sock.connect_ex((target_ip, port))
	if result == 0:
		opened_ports.append(port)

#PARTE 6
print("Opened ports:")
for i in opened_ports:
	print(i)