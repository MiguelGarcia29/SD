import socket

HOST = "localhost"
PORT = 1025

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    cliente.connect((HOST,PORT))
    accion = input("NOMBRE DEL ARCHIVO").strip()
    with open(accion,'r',encoding='utf-8') as f:
        contenido = f.read()
        
    
    cliente.sendall(contenido.encode('utf-8'))
    
    datos = cliente.recv(1024).decode('utf-8')
    
    with open(accion,'w',encoding='utf-8') as f:
        f.write(datos)
    
except Exception as e:
    print("ERROR {e}")