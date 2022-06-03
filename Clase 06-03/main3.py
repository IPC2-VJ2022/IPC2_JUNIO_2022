# class Gato:
#     # A simple example class
#     i = 123450

#     def f(self):
#         return 'hello world'

# class CamaGato:
#     # A simple example class
#     i = 10
#     def __init__(self):
#         self.gato = Gato()

#     def f(self):
#         return 'hello Cworld'

# x = CamaGato()
# y = CamaGato()
# x.gato.i=11111
# print(x.gato.i)
# print(y.gato.i)

class Nodo:
    # A simple example class

    def __init__(self,valor_):
        self.valor = valor_
        self.siguiente=None

class Lista:
    # A simple example class

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self,valor_):
        aux=Nodo(valor_)
        if(self.primero==None):
            self.primero=aux
        else:
            self.ultimo.siguiente=aux
        
        self.ultimo=aux
    
    def ver(self):
        aux=self.primero
        while aux!=None:
            print(aux.valor)
            aux=aux.siguiente

x = Lista()
y=int(input("Ingrese numeros: "))
for z in range(1, y+1):
    x.insertar(z)

x.ver()