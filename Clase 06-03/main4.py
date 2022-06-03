class Gato:
    # Contructor de la clase
    def __init__(self):
        self.nombre=""
        self.edad=0
        self.peso=0
    
    def dormir(self):
        print("El gato ",self.nombre,"durmio")
    
    def mauyar(self):
        return "miau"

#declarando la isntancia
# gato1=Gato()
# gato2=Gato()
# gato1.nombre="Carlos"
# gato2.nombre="Jose"
# gato1.dormir()
# gato2.dormir()
# print(gato1.mauyar())

class Cliente:
    # Contructor de la clase
    def __init__(self):
        self.id=0
        self.nombre=""
        self.carrito=0

nuevoCliente1=Cliente()
nuevoCliente1.id=10
nuevoCliente1.nombre="Juan"
nuevoCliente1.carrito=5

print("Los datos del cliente son: ")
print("id:",nuevoCliente1.id)
print("nombre",nuevoCliente1.nombre)
print("carrito",nuevoCliente1.carrito)
