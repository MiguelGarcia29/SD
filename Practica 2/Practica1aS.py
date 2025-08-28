import socket;

HOST = 'localhost'
PORT = 1025

s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_udp.bind((HOST,PORT))

print ("ESPERANDO")
mensaje, addr=s_udp.recvfrom(1024)

print("Recibido: " + str(mensaje.decode("utf-8")))
print("IP cliente: " + str(addr[0]) )
print("Puerto: " + str(addr[1]))