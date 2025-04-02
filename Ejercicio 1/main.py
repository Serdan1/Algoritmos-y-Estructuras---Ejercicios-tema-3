from hanoi import torre_hanoi

if __name__ == "__main__":
    # Configuración del problema
    num_piedras = 3  # Usamos 3 para probar, pero el enunciado dice 74
    columna_origen = "A"
    columna_auxiliar = "B"
    columna_destino = "C"
    
    print(f"Resolviendo el Puzzle de la Pirámide con {num_piedras} piedras:")
    torre_hanoi(num_piedras, columna_origen, columna_auxiliar, columna_destino)
    
    # Cálculo del número total de movimientos para el caso original (74 piedras)
    movimientos_totales = 2 ** 74 - 1
    print(f"\nNúmero total de movimientos necesarios para 74 piedras: {movimientos_totales}")