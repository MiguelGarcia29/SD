import socket

HOST = 'localhost'
PORT = 1025

clt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clt.sendto(b"HOLA PIXA",(HOST,PORT))

msj,_ = clt.recvfrom(1024)
print(msj.decode("utf-8"))

nombre = input("Tu nombre: ")
clt.sendto(nombre.encode("utf-8"), (HOST,PORT))

msj,_ = clt.recvfrom(1024)
print(msj.decode("utf-8"))

while True:
    duda = input("Escriba una duda o 'exit' para salir: ")
    clt.sendto(duda.encode('utf-8'),(HOST,PORT))
    
    if duda == 'exit':
        print("Conexion finalizada")
        break
    
    msj,_ = clt.recvfrom(1024)
    print("Servidor: ", msj.decode("utf-8"))