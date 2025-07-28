"""
Autor: Kevin Pico
Grupo: J3
Fecha:28/07/2025
Descripcion: Proyecto torneos de futbol

"""

import os
import json
from utils.helpers import limpiar, congelar
from controllers.equipos import registrar_equipo, ver_equipos, borrar_equipo
from controllers.jugadores import (
    registrar_jugador, 
    ver_jugadores_por_equipo, 
    borrar_jugador
)
from controllers.cuerpotecnico import (
    registrar_cuerpo_tecnico, 
    ver_cuerpo_tecnico_por_equipo, 
    borrar_cuerpo_tecnico
)
from controllers.torneos import registrar_torneo, ver_torneos, inscribir_equipos_torneo, borrar_torneo
from controllers.partidos import registrar_partido, ver_partidos, borrar_partido
from controllers.transferencias import gestionar_transferencia
from controllers.estadisticas import ver_estadisticas

def archivos_json():
    archivos = [
        'data/equipos.json',
        'data/jugadores.json',
        'data/cuerpotecnico.json',
        'data/torneos.json',
        'data/partidos.json',
        'data/transferencias.json',
        'data/estadisticas.json'
    ]
    
    for archivo in archivos:
        directorio = os.path.dirname(archivo)
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        if not os.path.exists(archivo):
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=2)

def men_prin():
    while True:
        limpiar()
        print("---GESTOR DE TORNEOS DE FÚTBOL---")
        print("1. |   Gestión de Equipos    |")
        print("2. |  Gestión de Jugadores   |")
        print("3. |Gestión de Cuerpo Técnico|")
        print("4. |   Gestión de Torneos    |")
        print("5. |   Gestión de Partidos   |")
        print("6. |      Transferencias     |")
        print("7. |       Estadísticas      |")
        print("8. |          Salir          |")
        
        opcion = input("\: ")
        
        if opcion == "1":
            men_equipo()
        elif opcion == "2":
            men_jugadores()
        elif opcion == "3":
            men_tecnicos()
        elif opcion == "4":
            men_torneos()
        elif opcion == "5":
            men_partidos()
        elif opcion == "6":
            gestionar_transferencia()
        elif opcion == "7":
            ver_estadisticas()
        elif opcion == "8":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            congelar()


def men_equipo():
    while True:
        limpiar()
        print("--- GESTIÓN DE EQUIPOS ---")
        print("1. |Registrar nuevo equipo    |")
        print("2. |Listar equipos registrados|")
        print("3. |Eliminar equipo           |")
        print("4. |Volver al menú principal  |")
        
        opcion = input("\n: ")
        
        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            ver_equipos()
        elif opcion == "3":  
            borrar_equipo()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            congelar()

def men_jugadores():
    """Submenú para gestión de jugadores"""
    while True:
        limpiar()
        print("--- GESTIÓN DE JUGADORES ---")
        print("1. ||Registrar nuevo jugador")
        print("2. ||Listar jugadores por equipo")
        print("3. ||Eliminar jugador")
        print("4. ||Volver al menú principal")
        
        opcion = input("\n: ")
        
        if opcion == "1":
            registrar_jugador()
        elif opcion == "2":
            ver_jugadores_por_equipo()
        elif opcion == "3":
            borrar_jugador()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            congelar()

def men_tecnicos():
    """Submenú para gestión de cuerpo técnico"""
    while True:
        limpiar()
        print("--- GESTIÓN DE CUERPO TÉCNICO ---")
        print("1. ||Registrar nuevo miembro")
        print("2. ||Listar cuerpo técnico por equipo")
        print("3. ||Eliminar miembro")
        print("4. ||Volver al menú principal")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            registrar_cuerpo_tecnico()
        elif opcion == "2":
            ver_cuerpo_tecnico_por_equipo()
        elif opcion == "3":
            borrar_cuerpo_tecnico()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            congelar()

def men_torneos():
    while True:
        limpiar()
        print("--- GESTIÓN DE TORNEOS ---")
        print("1. ||Registrar nuevo torneo")
        print("2. ||Listar torneos registrados")
        print("3. ||Inscribir equipos en torneo")
        print("4. ||Eliminar torneo") 
        print("5. ||Volver al menú principal")
        
        opcion = input("\n: ")
        
        if opcion == "1":
            registrar_torneo()
        elif opcion == "2":
            ver_torneos()
        elif opcion == "3":
            inscribir_equipos_torneo()
        elif opcion == "4": 
            borrar_torneo()  
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            congelar()

def men_partidos():
    while True:
        limpiar()
        print("---GESTIÓN DE PARTIDOS---")
        print("1. ||Registrar nuevo partido")
        print("2. ||Listar partidos registrados")
        print("3. ||eliminar partidos")
        print("4. ||Volver al menú principal")
        
        opcion = input("\n: ")
        
        if opcion == "1":
            registrar_partido()
        elif opcion == "2":
            ver_partidos()
        elif opcion == "3":
            borrar_partido()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            congelar()

if __name__ == "__main__":
    archivos_json()
    men_prin()