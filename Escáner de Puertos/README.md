# Escáner de Puertos
# Contenido 
1° [Scan_portv1.py](https://github.com/Anacecilc/PIA_LPC_061/blob/main/Esc%C3%A1ner%20de%20Puertos/scan_portv1.py)


2° [Scan_portv2.py](https://github.com/Anacecilc/PIA_LPC_061/blob/main/Esc%C3%A1ner%20de%20Puertos/scan_portv2.py)


3° [Scan_portv3.py](https://github.com/Anacecilc/PIA_LPC_061/blob/main/Esc%C3%A1ner%20de%20Puertos/scan_portv3.py)


4° [Script.py](https://github.com/Anacecilc/PIA_LPC_061/blob/main/Esc%C3%A1ner%20de%20Puertos/script.py)


 Como podemos observar en esta sección se encuentran contenidos 4 scripts, haciendo uso del lenguaje Python.
 
 
 El 1° script nos localizará y mostrará los puertos de nuestra IP que se encuentren abiertos.
 
 
 En el 2° script se llevara acabo el intento de conectarse a los puertos que se definen dentro del script.
 
 
 El 3° script tiene una similitud con el script 1° hablando de su función pero a diferencia de su antecesor este hace uso de varios hilos gracias a una libreria de Python llamada Threading
 
El 4° script nos muestra un menú el cual nos da a escoger de 4 opciones de las cuales podemos realizar distintos tipos de escaneos, tales como de red, udp, uno total y uno para encontrar nuestro sistema operativo.
 
En el escaneo de la red utilizamos una IP la cual la obtenemos con ping logrando saber el estado en el que se encuentra.


En el escaneo total hace en una IP un escaneo de tipo TCP con la finalidad de obtener el estado en el que se hallan los puertos que se encuentran en esa dirección.


En el escaneo udp utilizamos nmap para que realice en una IP un escaneo UDP, dando la situación en la que se encuentra los puertos que se encuentren en ella


Por ultimo en el escaneo para encontrar el SO se detecta cual es el sistema operativo que trabaja en la IP que se ingreso.
 
 # Objetivo
 Nuestro principal objetivo en esta sección es seguir realizando escaneos en este caso se necesitarios 2 librerias de Python, Nmap la cual ya habia sido utilizada y una llamada Socket. 
 Seguimos aprendiendo y conociendo en que podemos llevar acabo escaneos para encontrar información valiosa o simplemente para hacer nuestras tareas más sencillas
 


