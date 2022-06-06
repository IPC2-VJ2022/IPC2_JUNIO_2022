class NodoListaC:
    def __init__(self,valor_):
        self.valor = valor_
        self.siguiente=None

class ListaC:
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def insertar(self,valor_):
        nuevo=NodoListaC(valor_)
        
        if (self.primero==None):
            self.primero=nuevo
        else:
            self.ultimo.siguiente=nuevo
        self.ultimo=nuevo
        self.ultimo.siguiente=self.primero

    def imprimir(self):
        print("Elementos de la lista circular")
        aux=self.primero
        while(aux!=None):
            print(aux.valor)
            if (aux.siguiente==self.primero):
                return
            aux=aux.siguiente

    def buscar(self, valor_buscado):
        aux=self.primero
        while(aux!=None):
            if (aux.valor==valor_buscado):
                print("actual: ",aux.valor)
                print("sgte: ",aux.siguiente.valor)

            if (aux.siguiente==self.primero):
                return
            aux=aux.siguiente