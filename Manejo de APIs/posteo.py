import requests 

# Nombre de Alumno: Ana Cecilia López Castillo
#Matricula: 1996528


if __name__ == '__main__':
    url= 'http://httpbin.org/post'
    argumentos = {'nombre':'Ana Cecilia López Castillo','matricula':'1996528','Curso':'Laboratorio de Programación para Ciberseguridad'}

    response = requests.post(url, params=argumentos)
    
    if response.status_code == 200:
        print(response.content)
