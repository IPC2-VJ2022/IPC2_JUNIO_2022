#Ejemplo eTree

# Importar xml.etree
import xml.etree.ElementTree as ET
from subprocess import check_output

#crear variables para el arbol y la raiz
arbol=None
raiz=None

def mostrarEmpleados(raiz_):
    for departamento in raiz_:
        print('Departamento: ',departamento.attrib['departamento'],'; Ubicacion:',departamento.attrib['ubicacion'])
        for empleado in departamento:
            print('\t ID: ',empleado.attrib['id'])
            print('\t\t Nombre: ',empleado.findall('nombre')[0].text)
            
            for salario in empleado.findall('./salario'):
                print('\t\t salario: ',salario.findall('neto')[0].text)
                print('\t\t bono: ',salario.findall('bono')[0].text)

def modificarEmpleado(raiz_,idBuscado,nuevoNombre_):
    for departamento in raiz_:
        # print('Departamento: ',departamento.attrib['departamento'],'; Ubicacion:',departamento.attrib['ubicacion'])
        for empleado in departamento:
            idActual=int(empleado.attrib['id'])
            if(idActual==idBuscado):
                empleado.findall('nombre')[0].text=nuevoNombre_
                return
    print('No se encontro el id')

def eliminarEmpleado(raiz_,idBuscado):
    for departamento in raiz_:
        # print('Departamento: ',departamento.attrib['departamento'],'; Ubicacion:',departamento.attrib['ubicacion'])
        for empleado in departamento:
            idActual=int(empleado.attrib['id'])
            if(idActual==idBuscado):
                departamento.remove(empleado)
                return
    print('No se encontro el id')

def Graficar(raiz_):
    # paso 1 Crear una cadena de txt con los comandos de graphviz
    # paso 2 Crear un archivo e introducirle los comandos de graphviz
    # pase 3 Compilar el archivo con el comando Dot
    
    contenido=""
    contenido+="digraph G { \n"
    contenido+="node[shape=box] \n"
    contenido+="nodoRaiz[label=\"Empresa\"] \n"

    contadorDep=0
    contadorEmpl=0
    for departamento in raiz_:
        # print('Departamento: ',departamento.attrib['departamento'],'; Ubicacion:',departamento.attrib['ubicacion'])
        nombreNodoDep="nodoDepto"+departamento.attrib['departamento']
        contenido+=nombreNodoDep+"[label=\""+departamento.attrib['departamento']+"\"] \n"
        contenido+="nodoRaiz ->"+nombreNodoDep+"\n"

        for empleado in departamento:
            # print('\t ID: ',empleado.attrib['id'])
            nombreNodoIDEmpleado="nodoEmpl"+empleado.attrib['id']
            contenido+=nombreNodoIDEmpleado+"[label=\"Empleado: "+empleado.attrib['id']+" \"] \n"
            contenido+=nombreNodoDep+"->"+nombreNodoIDEmpleado+"\n"

            # print('\t\t Nombre: ',empleado.findall('nombre')[0].text)
            nombreNodoNmaeEmpleado=nombreNodoIDEmpleado+"name"
            nombreEmpleado=empleado.findall('nombre')[0].text
            var1=nombreEmpleado.replace('"','\\"')
            contenido+=nombreNodoNmaeEmpleado+"[label=\"Nombre: "+var1+" \"] \n"
            contenido+=nombreNodoIDEmpleado+"->"+nombreNodoNmaeEmpleado+"\n"
            
    
    contenido+="}"
    archivoDot=open("comandos/archivo.dot",'w',encoding="utf-8")
    archivoDot.write(contenido)
    archivoDot.close()
    print(contenido)
    comandoDot = "dot -Tjpg comandos/archivo.dot -o reportes/reporteEmpleados.jpg"
    check_output(comandoDot, shell=True)




while True:
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

