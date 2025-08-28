from bottle import get,put,post,request,run,HTTPError

import json


class Personas:
    def __init__(self, dni, nombre, correo, dept, cat, asig):
        self.dni = dni
        self.nombre = nombre
        self.correo = correo
        self.dept = dept
        self.cat = cat
        self.asig = asig 

usu = dict()

@post('/alta')
def alta():
    data = request.json

    claves_req=['dni','nombre','correo','dept','cat','asig']
    if not all(clave in data for clave in claves_req):
        raise HTTPError(400, 'Faltan campos obligatorios en el JSON')

    usu[data.get('dni')]=Personas(data.get('dni'),data.get('nombre'),data.get('correo'),data.get('dept'),data.get('cat'),data.get('asig'))
    
    json = {'dni':data.get('dni'),
            'nombre':data.get('nombre'),
            'correo':data.get('correo'),
            'dept':data.get('dept'),
            'cat':data.get('cat'),
            'asig':data.get('asig')}
    
    response.headers['Content-Type'] = 'application/json'

    return json

if __name__ == '__main__':    
    run(host='localhost', port=8083)