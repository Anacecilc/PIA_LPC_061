#Ana Cecilia Lopez castillo
#1996528

import nmap
escaner = nmap.PortScanner()
menu = int(input(""" Buenas tardes,porfavor tecle la letra de la opcion que deseé realizar del menú
                    0. Escaneo UDP
                    1. Escaneo total
                    2. Hallar SO
                    3. Escaneo de red 
                    """))
if menu ==0:
    IP = input("Ingrese la direccion ip que desea que se escanee: ")
    pto1 = input("Ingrese el primer puerto para el escaneo: ")
    pto2 = input("Ingrese el segundo puerto para el escaneo: ")
    print("Realizando escaneo UDP......")
    escaner.scan(IP, pto1 + '-' + pto2, '-sU')
    for host in escaner.all_hosts():       
        print('Su usuario es: %s (%s)' % (host,escaner[host].hostname()))   
        print('Su estado es : %s' % escaner[host].state())                 
        for proto in escaner[host].all_protocols():                 
            print('Protocolo : %s' % proto )                     
            lport = escaner[host][proto].keys()                      
        
            for port in lport:                                                                 
                print('Puerto : %s\tstate : %s' % (port,escaner[host][proto][port]['state']))
if menu ==1:
    IP = input("Ingrese la direccion ip que desea que se escanee: ")
    print("Comenzado el escaneo total....")
    escaner.scan(ip)
    for host in escaner.all_hosts():       
        print('Su usuario es  : %s (%s)' % (host,escaner[host].hostname()))    
        print('Su estado es: %s' % escaner[host].state())                  
        for proto in escaner[host].all_protocols():                  
            print('-----------------------------------------------------')
            print('Protocolo : %s' % proto )                    
            lport = escaner[host][proto].keys()                      
        
            for port in lport:                                                                 
                print('Puerto : %s\tstate : %s' % (port,escaner[host][proto][port]['state']))
if menu ==2:
    IP = input("Ingrese la direccion ip que desea que se escanee: ")
    scan_raw_result = escaner.scan(ip, arguments='-v -n -A')
    
    for host, result in scan_raw_result['scan'].items():
        if result['status']['state'] == 'up':
            for os in result['osmatch']:
                print('El sistema operativo es:' + os['name'] + ' ' * 3)
if menu ==3:
    IP=input("Ingrese la direccion ip que desea que se escanee: ")
    #
    escaner.scan(hosts=ip, arguments='-sP')
    print("Realizando escaneo con ping...")
    for host in escaner.all_hosts():       
        print('---------------------------------------------------------')
        print('Su usuario es : %s (%s)' % (host,escaner[host].hostname()))   
        print('Su estado es : %s' % escaner[host].state())                 
        for proto in escaner[host].all_protocols():                 
            print('-----------------------------------------------------')
            print('Protocolo : %s' % proto )                    
            lport = escaner[host][proto].keys()                      
        
            for port in lport:                                                                  
                print('Puerto : %s\tstate : %s' % (port,escaner[host][proto][port]['state']))
