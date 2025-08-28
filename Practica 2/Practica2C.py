# Cliente TCP
import socket
import os

def enviar_archivo(servidor, puerto, ruta_archivo):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((servidor, puerto))
        nombre_archivo = os.path.basename(ruta_archivo)
        cliente.sendall(nombre_archivo.encode('utf-8'))

        respuesta = cliente.recv(1024).decode('utf-8').strip()
        if respuesta == "EXISTE":
            accion = input(f"El archivo {nombre_archivo} ya existe en el servidor. ¿Desea sobrescribirlo? (SI/NO): ").strip().upper()
            cliente.sendall(accion.encode('utf-8'))
            if accion != "SI":
                print("Transferencia cancelada.")
                cliente.close()
                return

        # Enviar contenido del archivo
        with open(ruta_archivo, 'rb') as archivo:
            while True:
                datos = archivo.read(1024)
                if not datos:
                    # Finaliza cuando ya no hay más datos que leer
                    break
                cliente.sendall(datos)

        # Cerrar el socket completamente para que el servidor detecte fin de transmisión
        cliente.close()

    except Exception as e:
        print(f"Error en el cliente: {e}")

if __name__ == "__main__":
    enviar_archivo('localhost', 65432, 'ej.pdf')
