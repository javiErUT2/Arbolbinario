class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para insertar un nodo en el árbol
def insertar(raiz, valor):
    if raiz is None:  # Si no hay raíz, crea un nuevo nodo con el valor
        return Nodo(valor)
    else:
        if valor < raiz.valor:  # Si el valor es menor, va al subárbol izquierdo
            raiz.izquierda = insertar(raiz.izquierda, valor)
        else:  # Si es mayor, va al subárbol derecho
            raiz.derecha = insertar(raiz.derecha, valor)
    return raiz

# Función para imprimir el árbol visualmente
def imprimir_arbol(raiz, espacio, espacio_incremento):
    if raiz is None:
        return
    
    espacio += espacio_incremento

    # Recorre primero el subárbol derecho para imprimir los nodos superiores a la derecha
    imprimir_arbol(raiz.derecha, espacio, espacio_incremento)
    print(" " * espacio + str(raiz.valor))  # Imprime el nodo actual con espacios para representar su profundidad
    # Luego recorre el subárbol izquierdo para imprimir los nodos inferiores a la izquierda
    imprimir_arbol(raiz.izquierda, espacio, espacio_incremento)

# Funciones para los diferentes tipos de recorrido en el árbol
def inorden(raiz):
    if raiz:
        inorden(raiz.izquierda)
        print(raiz.valor, end=" ")
        inorden(raiz.derecha)

def preorden(raiz):
    if raiz:
        print(raiz.valor, end=" ")
        preorden(raiz.izquierda)
        preorden(raiz.derecha)

def postorden(raiz):
    if raiz:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.valor, end=" ")

# Crear un árbol vacío
raiz = None

# Solicitar números para construir el árbol
print("Ingresa los números para construir el árbol (ingresa 0 para finalizar):")
numeros = []
while True:
    num = int(input("Ingrese un número (o '0' para finalizar): "))
    if num == 0:
        break
    numeros.append(num)

# Insertar los números ingresados en el árbol
for num in numeros:
    raiz = insertar(raiz, num)

# Mostrar el árbol visualmente
print("\nÁrbol binario:")
imprimir_arbol(raiz, 0, 4)

# Realizar el recorrido inorden
print("\nRecorrido inorden:")
inorden(raiz)

# Imprimir los números ordenados para inorden
numeros.sort()
print("\nRecorrido inorden de los números ingresados:")
print(*numeros, end=" ")

# Realizar el recorrido preorden
print("\nRecorrido preorden:")
preorden(raiz)

# Imprimir los números ordenados para preorden
numeros.sort()
print("\nRecorrido preorden de los números ingresados:")
print(*numeros, end=" ")

# Realizar el recorrido postorden
print("\nRecorrido postorden:")
postorden(raiz)

# Imprimir los números ordenados para postorden
numeros.sort()
print("\nRecorrido postorden de los números ingresados:")
print(*numeros, end=" ")
