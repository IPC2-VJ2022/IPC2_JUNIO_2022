#pip install flask
from xml.dom.minidom import Identified
from flask import Flask,request,render_template
import xml.etree.ElementTree as ET
import json
import re
import os

#App va a ser nuestra varianble para crear las rutas POST GET
app=Flask(__name__)

#definimos vairables iniciales
# arbol=None
# raiz=None

#Definimos nuestra ruta inicial
@app.route('/')
def inicio():
    return 'Pantalla de inicio IPC2'

#Definimos una ruta GET
@app.route('/ruta1')
def ruta1():
    cadena=""
    cadena+="{"+"\n"
    cadena+="\"datos\": \"mensaje deprueba\""+"\n"
    cadena+="}"
    #objeto json para guardar la info
    objJson=json.loads(cadena)
    return objJson

#Definimos una ruta GET mostrar empleados
@app.route('/empleados')
def empleados():
    #Cargamos la info
    arbol=ET.parse('empleados.xml')
    #Obtenemos la raiz getroot con minuscula
    raiz=arbol.getroot()

    #cadena de txt en donde guardamos la info en formato JSON
    cadena=escribirJSONempleado(raiz)

    #convertir la cadena de txt a JSON
    objJson=json.loads(cadena)
    return objJson

#metodo para exribir la cadena de txt en formato JSON
def escribirJSONempleado(raiz_):
    cadena=""
    cadena+="{"+"\n"
    cadena+="\"empresa\":{"+"\n"
    cadena+="\"departamento\":["+"\n"

    #buscamos la cantidad de departamentos existentes
    cantDepartamentos=len(raiz_.findall('./departamento'))
    contadorDep=0

    #recorrer los departamentos para escribirlos en la cadena
    for departamento in raiz_:
        contadorDep+=1
        
        
        cadena+="{"+"\n"
        nombreDepartamento=departamento.attrib['departamento']

        cadena+="\"departamento\":"+"\""+nombreDepartamento+"\","+"\n"
        cadena+="\"empleado\":["+"\n"

        cantEmpleados=len(departamento.findall('./empleado'))
        contadorEmpleados=0

        #recorremos cada empleado del departamento y lo escribimos
        for empleado in departamento:
            contadorEmpleados+=1
            
            
            cadena+="{"+"\n"
            idEmpleado=empleado.attrib['id']
            nombreEmpleado=empleado.findall('nombre')[0].text
            cadena+="\"id\":"+"\""+idEmpleado+"\""+",\n"
            cadena+="\"nombre\":"+"\""+nombreEmpleado+"\""+"\n"
            
            #cerrar el objeto Empleado
            cadena+="}"+"\n"
            #Si no es el ultimo elemento, agregar una ,
            if(contadorEmpleados<cantEmpleados):
                cadena+=","+"\n"

        #Cerramos el listado de empleados del departamento
        cadena+="]"+"\n"

        #Cerramos el objeto departamento
        cadena+="}"+"\n"

        #Si no es el ultimo elemento, agregar una ,
        if(contadorDep<cantDepartamentos):
            cadena+=","+"\n"

    #Aqui ya salimos de los departamentos, cerramos el arreglo
    cadena+="]"+"\n"

    #Aqui cerramos el objeto: departamentos
    cadena+="}"+"\n"

    #Aqui cerramos el JSON
    cadena+="}"
    return cadena

#Definimos una ruta GET
@app.route('/reporteEmpleados')
def reporte1():
    #cargamos los datos
    arbol=ET.parse('empleados.xml')
    #Obtenemos la raiz getroot con minuscula
    raiz=arbol.getroot()
    Graficar1(raiz)
    return 'listo'

def Graficar1(raiz_):
    # paso 1 Crear una cadena de txt con los comandos de graphviz
    # paso 2 Crear un archivo e introducirle los comandos de graphviz
    # pase 3 Compilar el archivo con el comando Dot
    
    contenido=""
    contenido+="digraph G { \n"
    contenido+="node[shape=elipse] \n"
    contenido+="nodoRaiz[label=\"Empresa\"] \n"

    for departamento in raiz_:
        # print('Departamento: ',departamento.attrib['departamento'],'; Ubicacion:',departamento.attrib['ubicacion'])
        #nombre del nodo Departamento actual
        nombreNodoDep="nodoDepto"+departamento.attrib['departamento']
        
        #label del nodo Departamento actual
        contenido+=nombreNodoDep+"[label=\""+departamento.attrib['departamento']+"\"] \n"
        
        #apuntador Raiz->Nodo Departamento actual
        contenido+="nodoRaiz ->"+nombreNodoDep+"\n"

        #Recorrer los empleados de cada departamento
        for empleado in departamento:
            # print('\t ID: ',empleado.attrib['id'])

            #nombre del nodo del empleado actual
            nombreNodoIDEmpleado="nodoEmpl"+empleado.attrib['id']

            #label del nodo empleado actual
            contenido+=nombreNodoIDEmpleado+"[label=\"Empleado: "+empleado.attrib['id']+" \"] \n"
            
            #apuntador: departamento actual -> Empleado actual
            contenido+=nombreNodoDep+"->"+nombreNodoIDEmpleado+"\n"

            # -------Datos del empleado----------
            #nombre del nodo con el nombre del empleado
            nombreNodoNmaeEmpleado=nombreNodoIDEmpleado+"name"

            #Nombre del empleado actual
            nombreEmpleado=empleado.findall('nombre')[0].text

            #Reemplazamos " por \"
            var1=nombreEmpleado.replace('"','\\"')

            #colocarle label al nodo del nombre del empleado actual
            contenido+=nombreNodoNmaeEmpleado+"[label=\"Nombre: "+var1+" \"] \n"
            
            #Apuntar empleado actual -> Nombre empelado actual
            contenido+=nombreNodoIDEmpleado+"->"+nombreNodoNmaeEmpleado+"\n"
            
    #Cerramos el grafico
    contenido+="}"

    #Crear un archivo con el contenido que escribimos
    archivoDot=open("comandos/archivo.dot",'w',encoding="utf-8")
    #Esribmimos el contenido
    archivoDot.write(contenido)

    #IMPORTANTE: Cerrar el archivo
    archivoDot.close()

    #Print para verificar lo que escribimos
    print(contenido)

    #Ejecutar el comando
    comandoDot = "dot -Tjpg comandos/archivo.dot -o reportes/reporte2.jpg"
    os.system(comandoDot)

#peticion POST modificar empleado
@app.route('/modificarEmpleado',methods=["POST"])
def modificarEmp():
    #leer los datos del json
    jsonres=request.get_json()

    #Guardar en variables los campos del JSON
    id_=int(jsonres["id"])
    nombre_=jsonres["nombre"]

    #Leemos el XML
    arbol=ET.parse('empleados.xml')
    #Obtenemos la raiz getroot con minuscula

    #modificamos el empleado
    modificarEmpleado(arbol,id_,nombre_)
    return 'listo'

def modificarEmpleado(arbol_,idBuscado,nuevoNombre_):
    raiz_=arbol_.getroot()
    for departamento in raiz_:
        # print('Departamento: ',departamento.attrib['departamento'],'; Ubicacion:',departamento.attrib['ubicacion'])
        for empleado in departamento:
            idActual=int(empleado.attrib['id'])
            if(idActual==idBuscado):
                #encontramos el empleado que estabamos buscando
                empleado.findall('nombre')[0].text=nuevoNombre_
                arbol_.write('empleados.xml',xml_declaration=True,encoding="utf-8")
                return #Despues de actualizar el dato, nos salimos del metodo
    print('No se encontro el id')
    input()


#METODO PRINCIPAL
if(__name__=='__main__'):
    app.run(host="0.0.0.0",port=9000,debug=False)
