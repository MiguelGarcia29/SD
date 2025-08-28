import socket

HOST = 'localhost'
PORT = 1025

socketServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketServer.bind((HOST,PORT))
socketServer.listen(1)
print("ESPERANDO")

s_cliente,addr = socketServer.accept()
mensaje = s_cliente.recv(1024)
print ("RECIBIDO: " + mensaje.decode("utf-8") + " IP: " +str(addr))
s_cliente.send("HOLA SOY S".encode("utf-8"))
s_cliente.close()
socketServer.close()

