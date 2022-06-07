#Ejemplo de diccionarios

diccionario1={
    "clave1":10,
    "clave2":"cadena",
    "clave3":[1,2,3]
}
diccionario1["clave3"]=4444
diccionario1.update({"clave4":"nuevoElemento"})
print(len(diccionario1))