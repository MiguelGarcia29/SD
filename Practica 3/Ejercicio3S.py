from bottle import put,post,get,request,response,HTTPError,run

import json
import os

habs=[]
FICHERO = "hoteles.json"

class Habitaciones:
    #Inicializar atributos
    def __init__(self, id, plazas, equipamiento, ocupada):
        self.id = id
        self.plazas = plazas
        self.equipamiento = equipamiento
        self.ocupada= ocupada
    
    def to_dict(self):
        return {
            "id": self.id,
            "plazas": self.plazas,
            "equipamiento": self.equipamiento,
            "ocupada": self.ocupada
        }
        
@post('/alta')
def alta_hab():
    try:
        data = request.json
        
         # Lista de claves obligatorias
        claves_requeridas = ['id', 'plazas', 'equipamiento', 'ocupada']

        # Comprobar si todas las claves están presentes
        if not all(clave in data for clave in claves_requeridas):
            raise HTTPError(400, "Faltan campos obligatorios en el JSON")
        
        hab = Habitaciones(data.get('id'),data.get('plazas'),data.get('equipamiento'),data.get('ocupada'))
        
        habs.append(hab)
        
        with open(FICHERO, "w") as f:
            json.dump([h.to_dict() for h in habs], f, indent=4)
        
        return "<p>Se ha insertado.</p>"

    except:
         raise HTTPError(500, "ERROR") 

@put('/mod/<id>')
def mod_hab(id):
    try:
        id=int(id)
        hab = None
        for h in habs:
            if(h.id == id):
                data = request.json
                h.plazas = data.get('plazas')
                h.equipamiento = data.get('equipamiento')
                h.ocupada = data.get('ocupada')
                hab = h
                break
        
        if hab is None:
            raise HTTPError(400, "ID no encontrada")
        
        with open(FICHERO, "w") as f:
            json.dump([h.to_dict() for h in habs], f, indent=4)
        
        return "<p>Modifcado correctamente</p>"
        
    except HTTPError as e:
        # Re-lanza errores personalizados como el 400
        raise e
    except Exception as e:
        # Para otros errores no esperados
        raise HTTPError(500, f"ERROR INTERNO: {str(e)}")
  
@get("/consultar")
def listar():
    habitas = []
    
    for h in habs:
        habitas.append({
            "id": h.id,
            "plazas": h.plazas,
            "equipamiento": h.equipamiento,
            "ocupada": h.ocupada
        })
        
    response.headers['Content-Type'] = 'application/json'
    
    return json.dumps(habitas)

@get("/consultar/<id>")
def listar(id):
    try:
        id=int(id)
        hab = None
        for h in habs:
            if(h.id == id):
                hab = h
                response.content_type = 'application/json'
                return json.dumps({
                    "id": hab.id,
                    "plazas": hab.plazas,
                    "equipamiento": hab.equipamiento,
                    "ocupada": hab.ocupada
                })
                
        
        if hab is None:
            raise HTTPError(400, "ID no encontrada")
    except HTTPError as e:
        raise e           
    except Exception:
         raise HTTPError(500, "ERROR") 
     
@get("/ocupadas/<flag>")
def ocupadas(flag):
   
    habitas = []
    
    for h in habs:
        if(h.ocupada==flag):
            print("hey")
            habitas.append({
                "id": h.id,
                "plazas": h.plazas,
                "equipamiento": h.equipamiento,
                "ocupada": h.ocupada
            })
        
    response.headers['Content-Type'] = 'application/json'
    
    return json.dumps(habitas)
    
if __name__ == '__main__':
    if os.path.exists(FICHERO):
        with open(FICHERO, "r") as f:
            datos = json.load(f)
            for d in datos:
                # Crear objetos Habitaciones desde los diccionarios guardados
                hab = Habitaciones(d["id"], d["plazas"], d["equipamiento"], d["ocupada"])
                habs.append(hab)
            
    if not os.path.exists(FICHERO):
        with open(FICHERO, "w") as f:
            json.dump([], f)
    
    run(host='localhost', port=8083)