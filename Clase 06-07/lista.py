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
    
    def borrar(self,valorBuscado_):
        aux=self.primero
        while(aux!=None):
            if (aux.valor==valorBuscado_): #eliminar el primer valor
                if(aux.siguiente!=None):
                    nodoBorrar=aux
                    self.primero=aux.siguiente
                    print("Se elimino el valor: ",valorBuscado_)
                    del nodoBorrar
                    return
                else: #Eliminar un elemento de una lista de un solo elemento
                    self.primero=None
                    self.ultimo=None
                    print("Se elimino el valor: ",valorBuscado_)
                    del aux
                    return

            if(aux.siguiente!=None):
                if (aux.siguiente.valor==valorBuscado_):
                    # eliminar de la mitad de la lista
                    nodoEliminar=aux.siguiente
                    if (aux.siguiente.siguiente!=None):
                        aux.siguiente=aux.siguiente.siguiente
                        print("Se elimino el valor")
                        del nodoEliminar
                        return
                    else:
                        #Eliminar el ultimo
                        NodoBorrar=aux.siguiente
                        aux.siguiente=None
                        self.ultimo=aux
                        print("Se elimino el valor ",valorBuscado_)
                        del NodoBorrar
                        return

            aux=aux.siguiente
        print("No encontro el valor")