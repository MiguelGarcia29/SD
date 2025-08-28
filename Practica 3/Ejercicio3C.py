import requests

URL = "http://localhost:8083"


if __name__ == '__main__':
    aux=0

    while aux!=6:
        print("Elige que opcion deseas realizar:\n"
    "1. Dar de alta una nueva habitacion\n"
    "2. Modificar los datos de un habitacion\n"
    "3. Consultar lista de todas las habitaciones\n"
    "4. Consultar una habitacion mediante identificador\n"
    "5. Consultar lista de habitaciones ocupadas o desocupadas\n"
    "6. Salir")
        aux = int(input())
        
        if aux == 1:
            id = int(input("Introduzca el id: "))
            plazas = int(input("Numero de plaza: "))
            equipamiento = input("Equipamiento: ").split(',')
            ocupada = input("Introduce si esta ocupada(true/false): ")
            while ocupada != "true" and ocupada != "false":
                ocupada = input("Introduce si esta ocupada(true/false): ") 
            
            data = {'id':id,
                    'plazas':plazas,
                    'equipamiento':equipamiento,
                    'ocupada':ocupada}
            
            response = requests.post(url=URL+"/alta",json=data)
            pastebin_url = response.text
            print(pastebin_url)
            
        if aux == 2:
            id = int(input("Introduzca el id a modificar: "))
            plazas = int(input("Numero de plaza: "))
            equipamiento = input("Equipamiento: ").split(',')
            ocupada = input("Introduce si esta ocupada(true/false): ")
            while ocupada != "true" and ocupada != "false":
                ocupada = input("Introduce si esta ocupada(true/false): ") 
                
            data = {'id':id,
                    'plazas':plazas,
                    'equipamiento':equipamiento,
                    'ocupada':ocupada}
            
            response = requests.put(url=URL+"/mod/"+str(id),json=data)
            pastebin_url = response.text
            print(pastebin_url)
            
        if aux == 3:
            response = requests.get(url=URL+"/consultar")
            pastebin_url = response.text
            print(pastebin_url)
            
        if aux == 4:
            id = int(input("Introduzca el id a consultar: "))
            response = requests.get(url=URL+"/consultar/"+str(id))
            pastebin_url = response.text
            print(pastebin_url)
        if aux == 5:
            flg = input("Introduzca true o false: ")
            response = requests.get(url=URL+"/ocupadas/"+flg)
            pastebin_url = response.text
            print(pastebin_url)