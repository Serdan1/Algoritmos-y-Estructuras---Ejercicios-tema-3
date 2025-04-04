# Importar las funciones principales de cada ejercicio
from Ejercicio1.main import torre_hanoi
from Ejercicio2.determinante_recursivo import determinante_recursivo
from Ejercicio2.determinante_iterativo import determinante_iterativo
from Ejercicio3.nave import Nave
from Ejercicio3.ejecucion import (
    tarea_1_ordenar_naves, tarea_2_mostrar_especificas, 
    tarea_3_top_5_pasajeros, tarea_4_max_tripulantes, 
    tarea_5_naves_gx, tarea_6_pasajeros_6_o_mas, 
    tarea_7_extremos_longitud
)
from Ejercicio4.polinomio import Polinomio
from Ejercicio4.resta import restar_polinomios
from Ejercicio4.division import dividir_polinomios
from Ejercicio4.eliminar import eliminar_termino
from Ejercicio4.existe import existe_termino

def run_ejercicio1():
    """Ejecuta el Ejercicio 1: Puzzle de la Pirámide de Piedras Preciosas."""
    print("=== Ejercicio 1: Puzzle de la Pirámide de Piedras Preciosas ===\n")
    num_piedras = 3  # Usamos 3 para probar (el enunciado dice 74, pero es inviable)
    columna_origen = "A"
    columna_auxiliar = "B"
    columna_destino = "C"
    
    print(f"Resolviendo el Puzzle de la Pirámide con {num_piedras} piedras:")
    torre_hanoi(num_piedras, columna_origen, columna_auxiliar, columna_destino)
    
    movimientos_totales = 2 ** 74 - 1
    print(f"\nNúmero total de movimientos necesarios para 74 piedras: {movimientos_totales}\n")

def run_ejercicio2():
    """Ejecuta el Ejercicio 2: Secreto de la Cifra Mágica."""
    print("=== Ejercicio 2: Secreto de la Cifra Mágica ===\n")
    matriz_ejemplo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Matriz de ejemplo:")
    for fila in matriz_ejemplo:
        print(fila)
    
    det_recursivo = determinante_recursivo(matriz_ejemplo)
    det_iterativo = determinante_iterativo(matriz_ejemplo)
    
    print(f"\nDeterminante (Recursivo): {det_recursivo}")
    print(f"Determinante (Iterativo): {det_iterativo}\n")

def run_ejercicio3():
    """Ejecuta el Ejercicio 3: Gran Rally Espacial."""
    print("=== Ejercicio 3: Gran Rally Espacial ===\n")
    naves = [
        Nave("Cometa Veloz", 150, 5, 10),
        Nave("Titán del Cosmos", 300, 12, 25),
        Nave("GX-Alpha", 80, 3, 4),
        Nave("Estrella Fugaz", 200, 8, 15),
        Nave("GX-Beta", 120, 4, 6),
        Nave("Nebulosa", 250, 10, 20),
        Nave("Astro Rey", 90, 6, 8),
        Nave("GX-Gamma", 110, 5, 7),
        Nave("Cosmo Explorer", 180, 7, 12),
        Nave("Luz Estelar", 130, 9, 18)
    ]
    
    tarea_1_ordenar_naves(naves.copy())
    tarea_2_mostrar_especificas(naves)
    tarea_3_top_5_pasajeros(naves.copy())
    tarea_4_max_tripulantes(naves)
    tarea_5_naves_gx(naves)
    tarea_6_pasajeros_6_o_mas(naves)
    tarea_7_extremos_longitud(naves)
    print()

def run_ejercicio4():
    """Ejecuta el Ejercicio 4: Matemática de los Encantamientos."""
    print("=== Ejercicio 4: Matemática de los Encantamientos ===\n")
    p1 = Polinomio()
    p1.agregar_termino(5, 3)
    p1.agregar_termino(2, 1)
    p1.agregar_termino(-1, 0)
    
    p2 = Polinomio()
    p2.agregar_termino(2, 3)
    p2.agregar_termino(3, 2)
    
    print("P1:", p1)
    print("P2:", p2)
    
    resta = restar_polinomios(p1, p2)
    print("\n1. P1 - P2:", resta)
    
    p3 = Polinomio()
    p3.agregar_termino(6, 2)
    p3.agregar_termino(5, 1)
    p3.agregar_termino(1, 0)
    
    p4 = Polinomio()
    p4.agregar_termino(2, 1)
    p4.agregar_termino(1, 0)
    
    print("\nP3:", p3)
    print("P4:", p4)
    cociente, resto = dividir_polinomios(p3, p4)
    print("2. P3 / P4 -> Cociente:", cociente, "Resto:", resto)
    
    print("\nP1 antes de eliminar 2x:", p1)
    eliminar_termino(p1, 1)
    print("3. P1 tras eliminar término de grado 1:", p1)
    
    existe = existe_termino(p1, 5, 3)
    print("\n4. ¿Existe 5x^3 en P1?:", "Sí" if existe else "No")
    existe = existe_termino(p1, 2, 1)
    print("   ¿Existe 2x en P1?:", "Sí" if existe else "No")

if __name__ == "__main__":
    print("=== Ejecución de Todos los Ejercicios ===\n")
    run_ejercicio1()
    run_ejercicio2()
    run_ejercicio3()
    run_ejercicio4()