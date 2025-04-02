def determinante_iterativo(matriz):
    """
    Calcula el determinante de una matriz 3x3 usando la regla de Sarrus.
    """
    if len(matriz) != 3 or len(matriz[0]) != 3:
        raise ValueError("La matriz debe ser 3x3")
    
    a, b, c = matriz[0][0], matriz[0][1], matriz[0][2]  # Primera fila
    d, e, f = matriz[1][0], matriz[1][1], matriz[1][2]  # Segunda fila
    g, h, i = matriz[2][0], matriz[2][1], matriz[2][2]  # Tercera fila
    
    # Regla de Sarrus: suma de diagonales principales - suma de diagonales secundarias
    positivas = a * e * i + b * f * g + c * d * h
    negativas = c * e * g + a * f * h + b * d * i
    return positivas - negativas