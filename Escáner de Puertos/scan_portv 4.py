#Ana Cecilia Lopez castillo 
#1996528

import nmap


scanner = nmap. PortScanner ()
scanner.scan ('192.168.0.15','1-1024', '-v-sV')
scanner. command_line()
scanner.all_hosts()
scanner ['192.168.0.15' ].state()
scanner ['192.168.0.15'].all_protocols()
scanner ['192.168.0.15' ]['tcp'].keys()
scanner ['192.168.0.15'].has_tcp(21)
scanner ['192.168.0.15' ].has_tcp (22)
scanner ['192.168.0.15']['tcp'][22]
scanner ['192.168.0.15' ]['tcp'][22][product ]
