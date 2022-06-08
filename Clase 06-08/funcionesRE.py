import re

# cadena ="el arbol es verde y grande"
# patron="verde"

# resultado=re.search(patron,cadena)
# resultado2=re.match(patron,cadena)

# print(resultado)
# # en que posicion encontro la coincidencia
# # start()
# print("coincencia encontrada en la pos ",resultado.start())

cadena ="el arbol es verde, el arbol antiguo y el arbol grande"
patron="el arbol"

resultado=re.findall(patron,cadena)

print(resultado)
