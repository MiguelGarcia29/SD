import socket

HOST = 'localhost'
PORT = 1025

serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serv.bind((HOST,PORT))

msj,dir = serv.recvfrom(1024)
bienvenida = "¡Bienvenido! ¿Cuál es su nombre para que pueda dirigirme a usted?"
serv.sendto(bienvenida.encode('utf-8'),dir)

msj,dir = serv.recvfrom(1024)
nombre = msj.decode("utf-8")
print(f"Nombre: {nombre}")

mensaje = f"{nombre}, ¿en que puedo ayudarte?"
serv.sendto(mensaje.encode("utf-8"),dir)

while True:
    msj,dir = serv.recvfrom(1024)
    msj = msj.decode('utf-8')
    if msj == "exit":
        print(f"{nombre} se fue")
        break
    
    respuesta = "Debe ponerse en contacto con el servicio de atención de dudas cuya dirección es dudas@ejemplo.com"
    serv.sendto(respuesta.encode("utf-8"),dir)
    
