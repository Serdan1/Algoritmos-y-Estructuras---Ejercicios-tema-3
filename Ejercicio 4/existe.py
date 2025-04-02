def existe_termino(polinomio, coeficiente, grado):
    """Devuelve True si el término (coeficiente, grado) existe."""
    actual = polinomio.inicio
    while actual:
        if actual.coeficiente == coeficiente and actual.grado == grado:
            return True
        actual = actual.siguiente
    return False