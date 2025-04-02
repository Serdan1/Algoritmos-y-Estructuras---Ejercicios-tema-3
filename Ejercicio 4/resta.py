from polinomio import Polinomio

def restar_polinomios(p1, p2):
    """Resta p2 de p1 y devuelve un nuevo polinomio."""
    resultado = Polinomio()
    act1 = p1.inicio
    act2 = p2.inicio
    
    while act1 or act2:
        if act1 and (not act2 or act1.grado > act2.grado):
            resultado.agregar_termino(act1.coeficiente, act1.grado)
            act1 = act1.siguiente
        elif act2 and (not act1 or act2.grado > act1.grado):
            resultado.agregar_termino(-act2.coeficiente, act2.grado)
            act2 = act2.siguiente
        else:  # Grados iguales
            coef = act1.coeficiente - act2.coeficiente
            if coef != 0:
                resultado.agregar_termino(coef, act1.grado)
            act1 = act1.siguiente
            act2 = act2.siguiente
    return resultado