#etree xml
from pickle import TRUE
import xml.etree.ElementTree as ET

#Mostrar todos los datos
def mostrar():
    arbol=ET.parse('empleado.xml')
    raiz_empresa=arbol.getroot()

    print("Empresa")
    for departamento in raiz_empresa:
        print("\tdepartamento: ",departamento.attrib['departamento'])
        for empleado in departamento:
            print("\t\tid: ",empleado.attrib['id'])
            print("\t\tnombre: ",empleado.findall('nombre')[0].text)
            print("\t\tsalario: ",empleado.findall('salario')[0].text)
            
#actualizar dato
def actualizar():
    arbol=ET.parse('empleado.xml')
    raiz_empresa=arbol.getroot()

    for departamento in raiz_empresa:
        for empleado in departamento:
            if (True): #aca estaria la condicion a evaluar
                empleado.findall('nombre')[0].text="nuevo Nombre"
                print("datos actualizados")
    arbol.write('nuevoarchivo.xml')

#borrar dato
def borrar():
    arbol=ET.parse('empleado.xml')
    raiz_empresa=arbol.getroot()
    contador=0
    for departamento in raiz_empresa:
        for empleado in departamento:
            contador+=1
            if (contador>2): #solo va a borrar el tercer empleado
                departamento.remove(empleado)
                print("datos eliminados")
    arbol.write('nuevoarchivo2.xml')

borrar()
