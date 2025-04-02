def torre_hanoi(n, origen, auxiliar, destino):
    """
    Resuelve el problema de la Torre de Hanói de forma recursiva.
    Parámetros:
    - n: número de piedras a mover
    - origen: columna de donde se mueven las piedras
    - auxiliar: columna auxiliar
    - destino: columna donde se deben apilar todas las piedras
    """
    # Caso base: si solo hay una piedra, muévela directamente
    if n == 1:
        print(f"Mover piedra 1 de {origen} a {destino}")
        return
    
    # Paso 1: Mover las (n-1) piedras superiores de origen a auxiliar
    torre_hanoi(n - 1, origen, destino, auxiliar)
    
    # Paso 2: Mover la piedra más grande de origen a destino
    print(f"Mover piedra {n} de {origen} a {destino}")
    
    # Paso 3: Mover las (n-1) piedras de auxiliar a destino
    torre_hanoi(n - 1, auxiliar, origen, destino)