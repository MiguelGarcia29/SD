import os
import socket

HOST = 'localhost'
PORT = 1025

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)

con,addr = server.accept()
nombre_archivo = con.recv(1024).decode('utf-8')
print(f"Cliente ha solicitado: {nombre_archivo}")

if not os.path.isfile(nombre_archivo):
    con.sendall(b"ERROR")
    print("Archivo no encontrado.")
else:
    con.sendall(b"OK")  
    
    with open(nombre_archivo,'rb') as f:
        while True:
            bytes = f.read(1024)
            if not bytes:
                break
            
            con.sendall(bytes)
    
        print("Archivo enviado")