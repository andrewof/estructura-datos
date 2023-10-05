class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
        
        
class ListaDoble:
    def __init__(self):
        self.primero = None
        self.segundo = None
        
    def vacia(self):
        return self.primero is None
    
    def agregar_al_final(self, dato):
        nuevoNodo = Nodo(dato)
        if self.vacia():
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            nuevoNodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo
            
    def recorrerAdelante(self):
        actual = self.primero
        while actual:
            print(actual.dato, end=' ')
            actual = actual.siguiente
        print()
        
    def recorrerAtras(self):
        actual = self.ultimo
        while actual:
            print(actual.dato, end=' ')
            actual = actual.anterior
        print()
        
        
lista = ListaDoble()
lista.agregar_al_final(1)
lista.agregar_al_final(2)
lista.agregar_al_final(3)

print('Recorrido hacía adelante')
lista.recorrerAdelante()

print('\nRecorrido hacía atrás')
lista.recorrerAtras()