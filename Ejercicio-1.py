class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None
        

class listaDobleEnlazada:
    def __init__(self):
        self.primerNodo = None
        self.ultimoNodo = None
        
    def registrar(self, dato):
        nuevoNodo = Nodo(dato)
        if self.primerNodo is None:
            self.primerNodo = nuevoNodo
            self.ultimoNodo = nuevoNodo
        else:
            nuevoNodo.anterior = self.ultimoNodo
            self.ultimoNodo.siguiente = nuevoNodo
            self.ultimoNodo = nuevoNodo
            
    def adicionar(self, dato):
        nuevoNodo = Nodo(dato)
        if self.primerNodo is None:
            self.primerNodo = nuevoNodo
            self.ultimoNodo = nuevoNodo
        else:
            nuevoNodo.siguiente = self.primerNodo
            self.primerNodo.anterior = nuevoNodo
            self.primerNodo = nuevoNodo
            
    def eliminar(self, dato):
        nodoActual = self.primerNodo
        while nodoActual is not None:
            if nodoActual.dato == dato:
                if nodoActual.anterior is not None:
                    nodoActual.anterior.siguiente = nodoActual.siguiente
                else:
                    self.primerNodo = nodoActual.siguiente
                
                if nodoActual.siguiente is not None:
                    nodoActual.siguiente.anterior = nodoActual.anterior
                else:
                    self.ultimoNodo = nodoActual.anterior
                return 
            nodoActual = nodoActual.siguiente
            
    def visualizar(self):
        nodoActual = self.primerNodo
        while nodoActual is not None:
            print(nodoActual.dato)
            nodoActual = nodoActual.siguiente
            
if __name__ == "__main__":
    lista = listaDobleEnlazada()
    
    while True:
        print("""\n
                 --Menú--
              1. Registrar dato
              2. Adicionar dato
              3. Visualizar dato
              4. Eliminar dato
              5. Salir
              """)
        opcion = int(input('Digite una opción: '))
        
        if opcion == 1:
            valor = int(input('\nIngrese un número entero: '))
            lista.registrar(valor)
        elif opcion == 2:
            valor = int(input('\nIngrese un número entero: '))
            lista.adicionar(valor)
        elif opcion == 3:
            print('\nElementos en la lista')
            lista.visualizar()
        elif opcion == 4:
            valor = int(input('\nDigite el número a eliminar: '))
            lista.eliminar(valor)
        elif opcion == 5:
            print('\nPrograma finalizado')
            break
        else:
            print('\nOpción incorrecta')