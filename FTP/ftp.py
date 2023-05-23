#Ana Cecilia Lopez Castillo
# Matricula 1996528

#Importamos el modulo ftp
from ftplib import FTP

#Conectamos al servidor por medio de la direccion IP de nuestro equipo
ftp= FTP('192.168.0.15')

#Iniciamos colocando los datos utilizados al momento de crear el usuario
ftp.login ('johnny','1996528')

#Nos movemos al directorio upload de ftp para si poder agregar el archivo que desemos en esta ubicacion 
ftp.cwd('upload')


#Con este comando vemos una lista que nos muestra que contiene la ruta en la que nos encontramos 
ftp.retrlines('LIST')


#Colocamos nuestro archivo ADVERTENCIA.txt en esta rura
ftp.storlines('STOR ADVERTENCIA.txt', open ('ADVERTENCIA.txt','rb'))

#fnalizamos nuestra trasferencia entre python y ftp por medio de este codigo 
ftp.quit()
