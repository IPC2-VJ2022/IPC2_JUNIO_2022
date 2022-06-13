#Ejemplo modelo DOM
from xml.dom import minidom

# empleado
# guardar el modelo DOM en la variable doc
doc=minidom.parse('empleado.xml')

#Crear un listado de objetos 'empleado' y guardarlo en la variable empleados
empleados=doc.getElementsByTagName('empleado')

#Recorrer el listado de empleados para obtener valores de cada <empleado>
for item in empleados:
    #crear variables para cada sube etiqueta de empleado
    nombre_=item.getElementsByTagName('nombre')[0]
    salario_=item.getElementsByTagName('salario')[0]
    print(nombre_.firstChild.data)
    print(salario_.firstChild.data)
    print("")


departamentos=doc.getElementsByTagName('departamento')

#Recorrer el listado de departamentos para obtener valores de cada <empleado>
for item in departamentos:
    #crear variables para cada sube etiqueta de empleado
    nombre_=item.getElementsByTagName('nombre')[0]
    salario1_=item.getElementsByTagName('neto')[0]
    salario2_=item.getElementsByTagName('bono')[0]
    print(nombre_.firstChild.data)
    print(salario1_.firstChild.data)
    print(salario2_.firstChild.data)
    print("")

#Mostrar atributos de TAG
#Recorrer el listado de departamentos para obtener valores de cada <empleado>
for item in departamentos:
    #Accediendop a atributos de TAG
    nombreDepto=item.attributes['departamento'].value
    ubicacion=item.attributes['ubicacion'].value

    #crear variables para cada sube etiqueta de empleado
    nombre_=item.getElementsByTagName('nombre')[0]
    salario1_=item.getElementsByTagName('neto')[0]
    salario2_=item.getElementsByTagName('bono')[0]
    print(nombreDepto,"; Ubicacion: ",ubicacion)
    print(nombre_.firstChild.data)
    print(salario1_.firstChild.data)
    print(salario2_.firstChild.data)
    print("")