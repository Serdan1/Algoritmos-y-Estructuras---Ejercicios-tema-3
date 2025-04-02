def determinante_recursivo(matriz):
    """
    Calcula el determinante de una matriz cuadrada usando recursión (expansión por cofactores).
    """
    n = len(matriz)
    
    # Caso base: matriz 1x1
    if n == 1:
        return matriz[0][0]
    
    # Caso base: matriz 2x2
    if n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    # Expansión por la primera fila para matrices 3x3 o mayores
    det = 0
    for j in range(n):
        det += matriz[0][j] * cofactor(matriz, 0, j)
    return det

def cofactor(matriz, fila, columna):
    """Calcula el cofactor de un elemento en la posición (fila, columna)."""
    return (-1) ** (fila + columna) * determinante_recursivo(menor(matriz, fila, columna))

def menor(matriz, fila, columna):
    """Devuelve la submatriz (menor) eliminando la fila y columna dadas."""
    return [[matriz[i][j] for j in range(len(matriz)) if j != columna]
            for i in range(len(matriz)) if i != fila]