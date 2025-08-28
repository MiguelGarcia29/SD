import socket

HOST = 'localhost'
PORT = 1025

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

s.send ("HOLA,S".encode("UTF-8"))
mensaje = s.recv(1024)
print("Recibido: " + mensaje.decode("UTF-8"))

s.close()