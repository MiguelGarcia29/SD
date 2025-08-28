import requests

URL = "http://localhost:8083"

if __name__ == '__main__':
    aux=0

    while aux!=6:
        print("Elige que opcion deseas realizar:\n"
    "1. Dar de alta\n"
    "2. Modificar los datos\n"
    "3. Consultar lista de todas \n"
    "4. Consultar mediante identificador\n"
    "5. Consultar lista cat\n"
    "6. Salir")
        aux = int(input())
        
    