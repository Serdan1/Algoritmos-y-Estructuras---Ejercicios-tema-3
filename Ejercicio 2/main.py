from determinante_recursivo import determinante_recursivo
from determinante_iterativo import determinante_iterativo

if __name__ == "__main__":
    # Matriz de ejemplo 3x3
    matriz_ejemplo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Mostrar la matriz
    print("Matriz de ejemplo:")
    for fila in matriz_ejemplo:
        print(fila)
    
    # Calcular determinante con ambos métodos
    det_recursivo = determinante_recursivo(matriz_ejemplo)
    det_iterativo = determinante_iterativo(matriz_ejemplo)
    
    print(f"\nDeterminante (Recursivo): {det_recursivo}")
    print(f"Determinante (Iterativo): {det_iterativo}")