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

# Encuentra el nodo con el valor mínimo en un subárbol
def encontrar_minimo(raiz):
    actual = raiz
    while actual.izquierda is not None:
        actual = actual.izquierda
    return actual

# Elimina un nodo con un valor específico del árbol
def eliminar_nodo(raiz, valor):
    if raiz is None:
        return raiz
    
    if valor < raiz.valor:
        raiz.izquierda = eliminar_nodo(raiz.izquierda, valor)
    elif valor > raiz.valor:
        raiz.derecha = eliminar_nodo(raiz.derecha, valor)
    else:
        if raiz.izquierda is None:
            temp = raiz.derecha
            raiz = None
            return temp
        elif raiz.derecha is None:
            temp = raiz.izquierda
            raiz = None
            return temp
        temp = encontrar_minimo(raiz.derecha)
        raiz.valor = temp.valor
        raiz.derecha = eliminar_nodo(raiz.derecha, temp.valor)
    return raiz

# Crear un árbol vacío
raiz = None

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

# Mostrar el árbol
print("\nÁrbol binario:")
imprimir_arbol(raiz, 0, 4)

# Recorridos del árbol
print("\nRecorrido inorden:")
inorden(raiz)
print("\nRecorrido preorden:")
preorden(raiz)
print("\nRecorrido postorden:")
postorden(raiz)

# Ordenar los números ingresados
numeros.sort()
print("\nNúmeros ingresados ordenados:")
print(*numeros, end=" ")

# Opción para buscar o eliminar
while True:
    opcion = input("\n\n¿Deseas buscar (B) o eliminar (E) un número? (S para salir): ").upper()
    if opcion == 'B':
        num_buscar = int(input("Ingresa el número que quieres buscar: "))
        if num_buscar in numeros:
            print(f"El número {num_buscar} está en el árbol.")
        else:
            print(f"El número {num_buscar} no está en el árbol.")
    elif opcion == 'E':
        num_eliminar = int(input("Ingresa el número que quieres eliminar: "))
        if num_eliminar in numeros:
            numeros.remove(num_eliminar)
            raiz = None
            for num in numeros:
                raiz = insertar(raiz, num)
            print(f"El número {num_eliminar} ha sido eliminado del árbol.")
            print("\nÁrbol binario actualizado:")
            imprimir_arbol(raiz, 0, 4)
        else:
            print(f"El número {num_eliminar} no está en el árbol.")
    elif opcion == 'S':
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
