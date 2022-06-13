from pydoc import doc
from xml.dom import minidom

#contenido del archivo
documento=minidom.parse('discos.xml')

#listado de cd 
discos=documento.getElementsByTagName('cd')

#recorrer el listado
for cd in discos:
    tituto=cd.getElementsByTagName('title')[0]
    artista=cd.getElementsByTagName('artist')[0]
    anio=cd.getElementsByTagName('year')[0]
    print(tituto.firstChild.data)
    print(artista.firstChild.data)
    print(anio.firstChild.data)
    
