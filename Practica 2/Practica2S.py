# Servidor TCP
import socket
import os

def archivo_existe(nombre_archivo):
    return os.path.isfile("recibidos/"+nombre_archivo)

def recibir_archivo(conn, nombre_archivo):
    with open("recibidos/"+nombre_archivo, 'wb') as archivo:
        while True:
            datos = conn.recv(1024)
            # Se detiene cuando el cliente cierra la conexión
            if not datos:
                break
            archivo.write(datos)

def iniciar_servidor(direccion, puerto):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((direccion, puerto))
    servidor.listen(1)
    print(f"Servidor escuchando en {direccion}:{puerto}")

    while True:
        try:
            conn, addr = servidor.accept()
            print(f"Conexión establecida desde {addr}")

            # Recibir nombre del archivo
            nombre_archivo = conn.recv(1024).decode('utf-8').strip()
            print(f"Cliente desea enviar: {nombre_archivo}")

            if archivo_existe(nombre_archivo):
                conn.sendall(b"EXISTE")
                respuesta = conn.recv(1024).decode('utf-8').strip()
                if respuesta != "SI":
                    print("El cliente canceló la transferencia.")
                    conn.close()
                    continue
            else:
                conn.sendall(b"OK")

            # Recibir el archivo hasta que el cliente cierre la conexión
            recibir_archivo(conn, nombre_archivo)
            print(f"Archivo {nombre_archivo} recibido correctamente.")

        except Exception as e:
            print(f"Error en el servidor: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    iniciar_servidor('localhost', 65432)
