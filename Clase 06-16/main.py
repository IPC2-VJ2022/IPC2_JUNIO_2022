#Ejemplo eTree

# Importar xml.etree
import xml.etree.ElementTree as ET
#importar la libreria para poder ejecutar comandos de cmd
from subprocess import check_output
#Para limpiar pantalla, o para ejecutar comandos cmd
import os

#crear variables para el arbol y la raiz
arbol=None #va a contener TODA la inforamcion del archivo
raiz=None #Va a contener el primer nodo del archivo

def mostrarEmpleados(raiz_):
    for departamento in raiz_:
        print('Departamento: ',departamento.attrib['departamento'],'; Ubicacion:',departamento.attrib['ubicacion'])
        for empleado in departamento:
            print('\t ID: ',empleado.attrib['id'])
            print('\t\t Nombre: ',empleado.findall('nombre')[0].text)
            
            for salario in empleado.findall('./salario'):
                print('\t\t salario: ',salario.findall('neto')[0].text)
                print('\t\t bono: ',salario.findall('bono')[0].text)
    input()

def modificarEmpleado(raiz_,idBuscado,nuevoNombre_):
    for departamento in raiz_:
        # print('Departamento: ',departamento.attrib['departamento'],'; Ubicacion:',departamento.attrib['ubicacion'])
        for empleado in departamento:
            idActual=int(empleado.attrib['id'])
            if(idActual==idBuscado):
                #encontramos el empleado que estabamos buscando
                empleado.findall('nombre')[0].text=nuevoNombre_
                return #Despues de actualizar el dato, nos salimos del metodo
    print('No se encontro el id')
    input()

def eliminarEmpleado(raiz_,idBuscado):
    for departamento in raiz_:
        # print('Departamento: ',departamento.attrib['departamento'],'; Ubicacion:',departamento.attrib['ubicacion'])
        for empleado in departamento:
            idActual=int(empleado.attrib['id'])
            if(idActual==idBuscado):
                departamento.remove(empleado)
                return
    print('No se encontro el id')
    input()

def Graficar(raiz_):
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

    #Ejecutar el comando en CMD
    comandoDot = "dot -Tjpg comandos/archivo.dot -o reportes/reporteEmpleados.jpg"
    check_output(comandoDot, shell=True)
    comandoDot2 = "dot -Tjpg comandos/archivo.dot -o reportes/reporte2.jpg"
    os.system(comandoDot2)


while True:
    # os.system('cls')
    print('1. Cargar datos')
    print('2. Mostrar datos')
    print('3. modificar datos')
    print('4. eliminar datos')
    print('5. Graficar datos')
    print('6. Contar datos')
    print('7. Salir')
    op=int(input('Seleccione op:'))

    if (op==1):
        #Leemos el arbol
        arbol=ET.parse('empleado.xml')
        #Obtenemos la raiz getroot con minuscula
        raiz=arbol.getroot()
        print('datos cargados')
    elif(op==2):
        mostrarEmpleados(raiz)
    elif(op==3):
        idEmpleado_=int(input('Ingrese el id del empleado: '))
        nuevoNombre_=input('Ingrese el nombre del empleado: ')
        modificarEmpleado(raiz,idEmpleado_,nuevoNombre_)
    elif(op==4):
        idEmpleado_=int(input('Ingrese el id del empleado: '))
        eliminarEmpleado(raiz,idEmpleado_)
    elif(op==5):
        Graficar(raiz)
    elif(op==6):
        print('La raiz tiene ',len(raiz[0]), 'hijos directos')
    elif(op==7):
        exit()

