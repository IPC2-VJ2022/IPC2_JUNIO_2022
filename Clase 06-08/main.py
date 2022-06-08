# Ejemplo graphviz

from subprocess import check_output

comando = "dot -Tjpg comandos.txt -o nueva.jpg"
check_output(comando, shell=True)

manf=open("comandos/abc.dot",'w')
contenido="digraph G {\nnode [shape=circle];\na->b\na->c\n}"
manf.write(contenido)
manf.close()
comando = "dot -Tjpg comandos/abc.dot -o reportes/nuevoReporte.jpg"
check_output(comando, shell=True)
