from polinomio import Polinomio
from resta import restar_polinomios

def dividir_polinomios(dividendo, divisor):
    """Divide dividendo entre divisor y devuelve cociente y resto."""
    if not divisor.inicio:
        raise ValueError("División por polinomio nulo")
    
    cociente = Polinomio()
    resto = Polinomio()
    # Copiar dividendo al resto
    act = dividendo.inicio
    while act:
        resto.agregar_termino(act.coeficiente, act.grado)
        act = act.siguiente
    
    grado_divisor = divisor.inicio.grado
    coef_divisor = divisor.inicio.coeficiente
    
    while resto.inicio and resto.inicio.grado >= grado_divisor:
        coef_cociente = resto.inicio.coeficiente / coef_divisor
        grado_cociente = resto.inicio.grado - grado_divisor
        cociente.agregar_termino(coef_cociente, grado_cociente)
        
        # Multiplicar término del cociente por divisor y restar del resto
        temp = Polinomio()
        act_div = divisor.inicio
        while act_div:
            temp.agregar_termino(coef_cociente * act_div.coeficiente, 
                               grado_cociente + act_div.grado)
            act_div = act_div.siguiente
        resto = restar_polinomios(resto, temp)
    
    return cociente, resto