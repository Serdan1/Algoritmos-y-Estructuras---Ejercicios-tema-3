# Algoritmos-y-Estructuras---Ejercicios-tema-3

https://github.com/Serdan1/Algoritmos-y-Estructuras---Ejercicios-tema-3.git


# Tarea 3 - Algoritmos y Estructuras

Soluciones a la Tarea 3 de Algoritmos y Estructuras.

## Estructura
- **Ejercicio1/**:
  - `hanoi.py`: Función recursiva de la Torre de Hanói.
  - `main.py`: Ejecuta el puzzle.
  - `__init__.py`
- **Ejercicio2/**:
  - `determinante_recursivo.py`: Método recursivo para el determinante.
  - `determinante_iterativo.py`: Método iterativo para el determinante.
  - `main.py`: Ejecuta ambos métodos.
  - `__init__.py`
- **Ejercicio3/**:
  - `nave.py`: Clase Nave.
  - `ejecucion.py`: Implementaciones con Quicksort y tareas.
  - `main.py`: Ejecuta las tareas.
  - `__init__.py`
- **Ejercicio4/**:
  - `nodo.py`: Clase Nodo para términos.
  - `polinomio.py`: Clase Polinomio.
  - `resta.py`: Resta de polinomios.
  - `division.py`: División de polinomios.
  - `eliminar.py`: Eliminar un término.
  - `existe.py`: Verificar existencia de un término.
  - `main.py`: Ejecuta todas las operaciones.
  - `__init__.py`

## Instrucciones
- Ejecutar: `python EjercicioX/main.py`.


## Estructura del Repositorio

```mermaid
graph TD
    A[Algoritmos-y-Estructuras-TareaX/] --> B[README.md]
    A --> C[Ejercicio1/]
    A --> D[Ejercicio2/]
    A --> E[Ejercicio3/]
    A --> F[Ejercicio4/]
    
    C --> C1[__init__.py]
    C --> C2[hanoi.py]
    C --> C3[main.py]
    
    D --> D1[__init__.py]
    D --> D2[determinante_recursivo.py]
    D --> D3[determinante_iterativo.py]
    D --> D4[main.py]
    
    E --> E1[__init__.py]
    E --> E2[nave.py]
    E --> E3[ejecucion.py]
    E --> E4[main.py]
    
    F --> F1[__init__.py]
    F --> F2[nodo.py]
    F --> F3[polinomio.py]
    F --> F4[resta.py]
    F --> F5[division.py]
    F --> F6[eliminar.py]
    F --> F7[existe.py]
    F --> F8[main.py]