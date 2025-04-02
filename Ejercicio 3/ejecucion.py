from nave import Nave

# Quicksort para ordenar por nombre (ascendente) y longitud (descendente)
def quicksort_naves(lista, inicio, fin):
    if inicio < fin:
        pivote = particion_naves(lista, inicio, fin)
        quicksort_naves(lista, inicio, pivote - 1)
        quicksort_naves(lista, pivote + 1, fin)

def particion_naves(lista, inicio, fin):
    pivote = lista[fin]
    i = inicio - 1
    for j in range(inicio, fin):
        if (lista[j].nombre < pivote.nombre) or \
           (lista[j].nombre == pivote.nombre and lista[j].longitud > pivote.longitud):
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1

# Quicksort para ordenar por cantidad de pasajeros (descendente)
def quicksort_pasajeros(lista, inicio, fin):
    if inicio < fin:
        pivote = particion_pasajeros(lista, inicio, fin)
        quicksort_pasajeros(lista, inicio, pivote - 1)
        quicksort_pasajeros(lista, pivote + 1, fin)

def particion_pasajeros(lista, inicio, fin):
    pivote = lista[fin].pasajeros
    i = inicio - 1
    for j in range(inicio, fin):
        if lista[j].pasajeros > pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1

# Funciones para las tareas
def tarea_1_ordenar_naves(lista):
    """Ordena por nombre (ascendente) y longitud (descendente)."""
    quicksort_naves(lista, 0, len(lista) - 1)
    print("1. Lista ordenada por nombre (ascendente) y longitud (descendente):")
    for nave in lista:
        print(nave)

def tarea_2_mostrar_especificas(lista):
    """Muestra información de 'Cometa Veloz' y 'Titán del Cosmos'."""
    print("\n2. Información de 'Cometa Veloz' y 'Titán del Cosmos':")
    for nave in lista:
        if nave.nombre in ["Cometa Veloz", "Titán del Cosmos"]:
            print(nave)

def tarea_3_top_5_pasajeros(lista):
    """Muestra las 5 naves con más pasajeros."""
    quicksort_pasajeros(lista, 0, len(lista) - 1)
    print("\n3. Cinco naves con mayor cantidad de pasajeros:")
    for i in range(min(5, len(lista))):
        print(lista[i])

def tarea_4_max_tripulantes(lista):
    """Muestra la nave con más tripulantes."""
    max_tripulantes = max(lista, key=lambda x: x.tripulantes)
    print("\n4. Nave con mayor cantidad de tripulación:")
    print(max_tripulantes)

def tarea_5_naves_gx(lista):
    """Muestra naves cuyo nombre comienza con 'GX'."""
    print("\n5. Naves cuyo nombre comienza con 'GX':")
    for nave in lista:
        if nave.nombre.startswith("GX"):
            print(nave)

def tarea_6_pasajeros_6_o_mas(lista):
    """Muestra naves con 6 o más pasajeros."""
    print("\n6. Naves con 6 o más pasajeros:")
    for nave in lista:
        if nave.pasajeros >= 6:
            print(nave)

def tarea_7_extremos_longitud(lista):
    """Muestra la nave más pequeña y más grande por longitud."""
    min_longitud = min(lista, key=lambda x: x.longitud)
    max_longitud = max(lista, key=lambda x: x.longitud)
    print("\n7. Nave más pequeña y más grande:")
    print("Más pequeña:", min_longitud)
    print("Más grande:", max_longitud)