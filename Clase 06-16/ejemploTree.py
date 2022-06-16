import xml.etree.ElementTree as ET

#Crear el elemento data, el contenido del archivo
data=ET.Element('data')

#Crear objeto Raiz
items= ET.SubElement(data,'items')

#Agregarle hijos a raiz (padre, etiqueta)
item1=ET.SubElement(items,'item')
item2=ET.SubElement(items,'item')

#Agregar valores a los hijos
item1.set('name','item1')
item2.set('name','item2')

item1.text='Item1IPC'
item2.text='Item2IPC'

datos=str(ET.tostring(data))

fichero=open('nuevoEjemploXML.xml','w')
fichero.write(datos)
fichero.close()