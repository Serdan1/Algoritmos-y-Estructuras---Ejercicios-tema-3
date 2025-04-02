from nave import Nave
from ejecucion import (tarea_1_ordenar_naves, tarea_2_mostrar_especificas, 
                      tarea_3_top_5_pasajeros, tarea_4_max_tripulantes, 
                      tarea_5_naves_gx, tarea_6_pasajeros_6_o_mas, 
                      tarea_7_extremos_longitud)

if __name__ == "__main__":
    # Lista de ejemplo con 10 naves
    naves = [
        Nave("Cometa Veloz", 150, 5, 10),
        Nave("Titán del Cosmos", 300, 12, 25),
        Nave("GX-Alpha", 80, 3, 4),
        Nave("Estrella Fugaz", 200, 8, 15),
        Nave("GX-Beta", 120, 4, 6),
        Nave("Nebulosa", 250, 10, 20),
        Nave("Astro Rey", 90, 6, 8),
        Nave("GX-Gamma", 110, 5, 7),
        Nave("Cosmo Explorer", 180, 7, 12),
        Nave("Luz Estelar", 130, 9, 18)
    ]
    
    print("=== Ejercicio 3: El Gran Rally Espacial ===\n")
    
    # Ejecutar todas las tareas
    tarea_1_ordenar_naves(naves.copy())  # Usamos copy para no modificar la lista original
    tarea_2_mostrar_especificas(naves)
    tarea_3_top_5_pasajeros(naves.copy())
    tarea_4_max_tripulantes(naves)
    tarea_5_naves_gx(naves)
    tarea_6_pasajeros_6_o_mas(naves)
    tarea_7_extremos_longitud(naves)