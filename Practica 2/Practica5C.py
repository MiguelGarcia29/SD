import socket

HOST = 'localhost'
PORT = 1025

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cliente.connect((HOST,PORT))
imagen = input("Que imagen quieres: ")

cliente.sendall(imagen.encode('UTF-8'))
respuesta = cliente.recv(1024).decode("UTF-8")
if (respuesta=="ERROR"):
    print(respuesta)
else:
    with open("imagen_recibida.jpeg",'wb') as f:
        while True:
            datos = cliente.recv(1024)
            if not datos:
                break
            f.write(datos)
