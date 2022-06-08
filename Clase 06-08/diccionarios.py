#Ejemplo de recorrer diccionarios
diccionario1={
    "clave1":10,
    "clave2":"cadena",
    "clave3":[1,2,3]
}

for clave in diccionario1:
    valor=diccionario1.get(clave)
    print("clave: ",clave,"; valor: ",valor)