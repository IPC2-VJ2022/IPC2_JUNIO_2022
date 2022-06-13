#Ejemplo eTree

# Importar xml.etree
import xml.etree.ElementTree as ET

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

def modificarEmpleado(raiz_,idBuscado):
    for departamento in raiz_:
        # print('Departamento: ',departamento.attrib['departamento'],'; Ubicacion:',departamento.attrib['ubicacion'])
        for empleado in departamento:
            idActual=int(empleado.attrib['id'])
            if(idActual==idBuscado):
                empleado.findall('nombre')[0].text='Nuevo nombre'
    arbol.write('empleadoNuevo.xml')

def eliminarEmpleado(raiz_,idBuscado):
    for departamento in raiz_:
        # print('Departamento: ',departamento.attrib['departamento'],'; Ubicacion:',departamento.attrib['ubicacion'])
        for empleado in departamento:
            idActual=int(empleado.attrib['id'])
            if(idActual==idBuscado):
                departamento.remove(empleado)
    arbol.write('empleadoNuevo.xml')


while True:
    print('1. Cargar datos')
    print('2. Mostrar datos')
    print('3. modificar datos')
    print('4. eliminar datos')
    print('5. Salir')
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
        modificarEmpleado(raiz,3)
    elif(op==4):
        eliminarEmpleado(raiz,2)
    elif(op==5):
        exit()
