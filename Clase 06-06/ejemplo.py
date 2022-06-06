listaNueva=["H","Z","L","N","A","F"]
lista=[2,6,8,7,11,0,22]
# listaNueva2=["h","i","j"]

# Funciones de listas

# print("Len: ",len(lista))
# print("Min: ",min(lista))
# print("Max: ",max(lista))
# print("Sum: ",sum(lista))

#Listas y cadenas

cadenaLetras="nueva,Cadena"
listaletras=list(cadenaLetras)
print(listaletras)

listaPartida=cadenaLetras.split(",")
print(listaPartida)

nuevaCadena="*".join(listaPartida)
print(nuevaCadena)