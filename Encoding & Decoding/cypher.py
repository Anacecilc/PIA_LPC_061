from cryptography.fernet import Fernet


#Ana Cecilia Lopez Castillo 1996528  15/03/2023

def genwrite():
    key = Fernet.generate_key()
    with open("pass.key","wb") as key_file:
        key_file.write(key)
genwrite()

def call_key():
    return open ("pass.key","rb").read()
key = call_key()
notce= "Bienvenido a Laboratorio de Programación en Ciberseguridad (LPC)".encode()
a = Fernet(key)
coded_notce = a.encrypt(notce)
print(coded_notce)

key = call_key()
b = Fernet(key)
decoded_notce = b.decrypt(coded_notce)
print(decoded_notce)
