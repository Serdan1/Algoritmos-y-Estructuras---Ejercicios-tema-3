from polinomio import Polinomio
from resta import restar_polinomios
from division import dividir_polinomios
from eliminar import eliminar_termino
from existe import existe_termino

if __name__ == "__main__":
    # Crear polinomios de ejemplo
    p1 = Polinomio()
    p1.agregar_termino(5, 3)  # 5x^3
    p1.agregar_termino(2, 1)  # 2x
    p1.agregar_termino(-1, 0)  # -1
    
    p2 = Polinomio()
    p2.agregar_termino(2, 3)  # 2x^3
    p2.agregar_termino(3, 2)  # 3x^2
    
    print("=== Ejercicio 4: La Matemática de los Encantamientos ===\n")
    print("P1:", p1)
    print("P2:", p2)
    
    # Tarea 1: Restar polinomios
    resta = restar_polinomios(p1, p2)
    print("\n1. P1 - P2:", resta)
    
    # Tarea 2: Dividir polinomios
    p3 = Polinomio()
    p3.agregar_termino(6, 2)  # 6x^2
    p3.agregar_termino(5, 1)  # 5x
    p3.agregar_termino(1, 0)  # 1
    
    p4 = Polinomio()
    p4.agregar_termino(2, 1)  # 2x
    p4.agregar_termino(1, 0)  # 1
    
    print("\nP3:", p3)
    print("P4:", p4)
    cociente, resto = dividir_polinomios(p3, p4)
    print("2. P3 / P4 -> Cociente:", cociente, "Resto:", resto)
    
    # Tarea 3: Eliminar término
    print("\nP1 antes de eliminar 2x:", p1)
    eliminar_termino(p1, 1)
    print("3. P1 tras eliminar término de grado 1:", p1)
    
    # Tarea 4: Verificar existencia
    existe = existe_termino(p1, 5, 3)
    print("\n4. ¿Existe 5x^3 en P1?:", "Sí" if existe else "No")
    existe = existe_termino(p1, 2, 1)
    print("   ¿Existe 2x en P1?:", "Sí" if existe else "No")