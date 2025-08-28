import socket



HOST = "localhost"
PORT = 1025

serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    serv.bind((HOST,PORT))
    serv.listen(1)
    
    while True:
        try:
            con,addr = serv.accept()
            print(f"Conexion establecida")
            datos = con.recv(1024).decode('utf-8')
            
            textInv = datos[::-1]
            
            con.sendall(textInv.encode('utf-8'))
            
            
        except Exception as e:
            print(f"ERROR {e}")
        finally:
            con.close()
    
    
except Exception as e:
    print("ERRORE {e}")