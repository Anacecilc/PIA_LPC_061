#Ana Cecilia Lopez Castillo
#1996528

import smtplib, ssl
import getpass

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

remitente_email= input("Ingrese el correo del remitente: ")
destinatario_email= input("Ingrese el correo destinatario: ")
contraseña= getpass.getpass("Ingrese la contraseña del remitente: ")

#Se revisa lo que se enviará en el asunto del correo
mensaje= MIMEMultipart("alternative")
mensaje["Subject"]= "Prueba de envio (script python) - 1996528"
mensaje["From"]= remitente_email
mensaje["To"]= destinatario_email

#Acomodamos nuestro mensaje en el formato deseado: HTML
html = """\
<html>
    <body>


    <p><strong> <h1> PRÁCTICA 12 </h2> </strong> <br>
       Ejercicio de la práctica 12 para envío de correos <br>
       <strong> Alumno: </strong> Ana Cecilia López Castillo <br>
       <strong> Matrícula: </strong> 1996528 <br>
    </p>
   </body>
</html>
"""

#Agregamos lo anterior de HTML al correo
html_part = MIMEText(html, 'html')
mensaje.attach(html_part)

#Indicamos que imagen enviaremos que en esta ocasión sera: fcfm_cool.png
arch= 'fcfm_cool.png'

#Se abre el archivo
with open(arch, 'rb') as adjunto:
    cont_adjunto = MIMEBase('application', 'octet-stream')
    cont_adjunto.set_payload(adjunto.read())
encoders.encode_base64(cont_adjunto)
cont_adjunto.add_header(
    "Content-Disposition",
    f"attachment; filename= {arch}"
)


#Agregamos lo que abrimos anteriormente al mensaje 
mensaje.attach(cont_adjunto)
mensaje_final = mensaje.as_string()


#Conectamos con smtp
with smtplib.SMTP("smtp.gmail.com", 587) as server:
                  server.ehlo()
                  server.starttls()
                  server.login(remitente_email, contraseña)
                  server.sendmail(
                      remitente_email, destinatario_email, mensaje.as_string()
                )









    
