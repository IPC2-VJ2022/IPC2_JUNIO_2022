import re

ER= "[0-9a-zA-Z]{8,12}"
entrada=input("Ingrese cadena: ")

resultado=re.match(ER,entrada)
if(resultado!=None):
    print("cadena aceptada")
else:
    print("cadena rechazada")
