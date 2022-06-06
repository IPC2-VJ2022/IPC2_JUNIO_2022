class NodoPila:
    def __init__(self,valor_):
        self.valor = valor_
        self.anterior=None
        self.siguiente=None

class Pila:
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def push(self,valor_):
        nuevo=NodoPila(valor_)
        
        if (self.primero==None):
            self.primero=nuevo
        else:
            nuevo.anterior=self.ultimo
            self.ultimo.siguiente=nuevo
        self.ultimo=nuevo

    def imprimir(self):
        print("Elementos de la lista")
        aux=self.primero
        while(aux!=None):
            print(aux.valor)
            aux=aux.siguiente
    
    def pop(self):
        aux=self.ultimo
        if (aux.anterior!=None):
            self.ultimo=aux.anterior
            aux.anterior.siguiente=None
        else:
            self.primero=None
            self.ultimo=None
        print("Se elimino el elemento ",aux.valor)
        del aux