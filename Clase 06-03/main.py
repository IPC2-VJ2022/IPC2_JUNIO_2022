#Ejemplo Lista
class Nodo:
    def __init__(self,valor_):
        self.valor = valor_
        self.siguiente=None

class Lista:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self,valor_):
        nuevo=Nodo(valor_)
        if(self.primero==None):
            self.primero=nuevo
        else:
            self.ultimo.siguiente=nuevo
        
        self.ultimo=nuevo

    def imprimir(self):
        aux=self.primero
        while(aux!=None):
            print(aux.valor)
            aux=aux.siguiente
    
    def buscar(self,valor_):
        aux=self.primero
        while(aux!=None):
            if(aux.valor==valor_):
                print("Encontro el valor")
                return
            aux=aux.siguiente
        print("No encontro el valor")

x=Lista()
x.insertar(10)
x.insertar(5)
x.insertar(4)
x.buscar(1000)
