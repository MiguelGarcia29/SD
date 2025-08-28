from bottle import post,request,response, HTTPError, run
import json

#EN WINDWOS
# curl -X POST -H "Content-Type: application/json" -d "{\"elementoa\": \"fresa\"}" http://localhost:8083/inserta

mis_elementos=[]
@post('/inserta')
def insert_element():
    try:
        data = request.json
        
        #Dentro de Data hay un par con la clave elmento
        if 'elemento' in data:
            elemento = data['elemento']
            
            if elemento not in mis_elementos:
                mis_elementos.append(elemento)

                #CREO UN 'JSON' PARA DEVOLVERLO
                response.content_type = 'application/json'
                
                return json.dumps({'mi_lista':mis_elementos})
        else :
            raise HTTPError(400,"Clave 'elemento' no encontrad en JSON")
    except:
         raise HTTPError(500, "ERROR") 

if __name__ == '__main__':
    run(host='localhost', port=8083)