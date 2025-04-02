def eliminar_termino(polinomio, grado):
    """Elimina el término con el grado especificado."""
    if not polinomio.inicio:
        return
    
    if polinomio.inicio.grado == grado:
        polinomio.inicio = polinomio.inicio.siguiente
        return
    
    actual = polinomio.inicio
    while actual.siguiente and actual.siguiente.grado != grado:
        actual = actual.siguiente
    if actual.siguiente:
        actual.siguiente = actual.siguiente.siguiente