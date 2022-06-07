# from lista import Lista

# nuevaLista=Lista()
# nuevaLista.insertar(2)
# nuevaLista.insertar(7)
# nuevaLista.insertar(11)
# nuevaLista.insertar(4)
# nuevaLista.imprimir()
# print("------------")
# nuevaLista.borrarTodo()
# print("------------")
# nuevaLista.insertar(10)
# nuevaLista.insertar(100)
# nuevaLista.insertar(1000)

# nuevaLista.imprimir()

#ejemplo de como ignorar la primera linea
# manf=open(input("ingrese el nombre archivo: "))
# contador=0
# for linea in manf:
#     contador+=1
#     if(contador<2):
#         continue
#     print(linea)

# try:
#     manf=open("abc.txt",'r')
#     contenido=manf.read()
#     depurado=repr(contenido)
#     print(depurado)
# except:
#     print("Error al abrir archivo")

try:
    manf=open("archivoDeComandos.Dot",'w')
    contenido="digraph G {\nnode [shape=triangle];\na->b\na->c\n}"
    manf.write(contenido)
except:
    print("Error al abrir archivo")

