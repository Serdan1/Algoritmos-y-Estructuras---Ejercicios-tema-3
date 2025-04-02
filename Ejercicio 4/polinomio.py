from nodo import Nodo

class Polinomio:
    def __init__(self):
        self.inicio = None
    
    def agregar_termino(self, coeficiente, grado):
        """Agrega un término al polinomio en orden descendente por grado."""
        nuevo = Nodo(coeficiente, grado)
        if not self.inicio or grado > self.inicio.grado:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
        else:
            actual = self.inicio
            while actual.siguiente and actual.siguiente.grado > grado:
                actual = actual.siguiente
            if actual.grado == grado:  # Sumar coeficientes si el grado ya existe
                actual.coeficiente += coeficiente
            else:
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
    
    def __str__(self):
        """Convierte el polinomio a una cadena legible."""
        if not self.inicio:
            return "0"
        terminos = []
        actual = self.inicio
        while actual:
            if actual.coeficiente != 0:
                if actual.grado == 0:
                    terminos.append(f"{actual.coeficiente}")
                elif actual.grado == 1:
                    terminos.append(f"{actual.coeficiente}x")
                else:
                    terminos.append(f"{actual.coeficiente}x^{actual.grado}")
            actual = actual.siguiente
        return " + ".join(terminos) if terminos else "0"