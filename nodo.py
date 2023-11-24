class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    else:
        if valor < raiz.valor:
            raiz.izquierda = insertar(raiz.izquierda, valor)
        else:
            raiz.derecha = insertar(raiz.derecha, valor)
    return raiz

def imprimir_arbol(raiz, espacio):
    if raiz is None:
        return
    
    espacio += 5
    imprimir_arbol(raiz.derecha, espacio)
    print(" " * espacio + str(raiz.valor))
    imprimir_arbol(raiz.izquierda, espacio)

# Crear un árbol
raiz = None
numeros = [5, 3, 7, 2, 4, 6, 8]

for num in numeros:
    raiz = insertar(raiz, num)

# Mostrar el árbol
print("Árbol binario:")
imprimir_arbol(raiz, 0)
