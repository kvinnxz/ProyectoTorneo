from utils.helpers import limpiar, congelar, leer_json, escribir_json
from utils.validadores import validar_texto, validar_entero
import json

def registrar_torneo():
    limpiar()
    print("========================")
    print("=== REGISTRAR TORNEO ===")
    print("========================")
    torneos = leer_json('data/torneos.json')
    
    nuevo_torneo = {
        'id': len(torneos) + 1,
        'nombre': validar_texto("Nombre del torneo: "),
        'pais': validar_texto("País sede: "),
        'fecha_inicio': validar_texto("Fecha de inicio (DD/MM/AAAA): "),
        'fecha_fin': validar_texto("Fecha de fin (DD/MM/AAAA): "),
        'equipos_inscritos': [],
        'partidos': []
    }
    
    torneos.append(nuevo_torneo)
    escribir_json('data/torneos.json', torneos)
    
    print(f"\nTorneo {nuevo_torneo['nombre']} registrado exitosamente!")
    congelar()

def ver_torneos():
    limpiar()
    print("=========================")
    print("=== LISTADO DE TORNEOS ===")
    print("=========================")
    
    torneos = leer_json('data/torneos.json')
    
    if not torneos:
        print("No hay torneos registrados.")
    else:
        for torneo in torneos:
            print(f"\nID: {torneo['id']}")
            print(f"Nombre: {torneo['nombre']}")
            print(f"País sede: {torneo['pais']}")
            print(f"Fecha inicio: {torneo['fecha_inicio']}")
            print(f"Fecha fin: {torneo['fecha_fin']}")
            print(f"Equipos inscritos: {len(torneo['equipos_inscritos'])}")
            print(f"Partidos programados: {len(torneo['partidos'])}")
            print("-" * 30)
    
    congelar()


def inscribir_equipos_torneo():
    limpiar()
    print("===================================")
    print("=== INSCRIBIR EQUIPOS EN TORNEO ===")
    print("===================================")
    
    torneos = leer_json('data/torneos.json')
    equipos = leer_json('data/equipos.json')
    
    if not torneos:
        print("No hay torneos registrados.")
        congelar()
        return
    
    if not equipos:
        print("No hay equipos registrados.")
        congelar()
        return
    
    print("\nTorneos disponibles:")
    for torneo in torneos:
        print(f"{torneo['id']}. {torneo['nombre']} ({torneo['fecha_inicio']} a {torneo['fecha_fin']})")
    
    id_torneo = validar_entero("\nID del torneo: ")
    torneo = next((t for t in torneos if t['id'] == id_torneo), None)
    
    if not torneo:
        print("ID de torneo no válido.")
        congelar()
        return
    
    print("\nEquipos disponibles para inscripción:")
    equipos_no_inscritos = [e for e in equipos if e['id'] not in torneo['equipos_inscritos']]
    
    if not equipos_no_inscritos:
        print("Todos los equipos ya están inscritos en este torneo.")
        congelar()
        return
    
    for equipo in equipos_no_inscritos:
        print(f"{equipo['id']}. {equipo['nombre']}")
    
    id_equipo = validar_entero("\nID del equipo a inscribir: ")
    equipo = next((e for e in equipos_no_inscritos if e['id'] == id_equipo), None)
    
    if not equipo:
        print("ID de equipo no válido o ya inscrito.")
        congelar()
        return
    
    # Inscribir equipo en torneo
    for t in torneos:
        if t['id'] == id_torneo:
            t['equipos_inscritos'].append(id_equipo)
            break
    
    escribir_json('data/torneos.json', torneos)
    
    print(f"\nEquipo {equipo['nombre']} inscrito exitosamente en el torneo {torneo['nombre']}!")
    congelar()

def borrar_torneo():
    limpiar()
    print("========================")
    print("=== ELIMINAR TORNEO ===")
    print("========================")
    
    torneos = leer_json('data/torneos.json')
    
    if not torneos:
        print("No hay torneos registrados.")
        congelar()
        return
    
    print("\nTorneos disponibles:")
    for torneo in torneos:
        print(f"{torneo['id']}. {torneo['nombre']}")
    
    id_torneo = validar_entero("\nIngrese ID del torneo a eliminar: ")
    torneo = next((t for t in torneos if t['id'] == id_torneo), None)
    
    if not torneo:
        print("ID de torneo no válido.")
        congelar()
        return
    
    # Confirmación
    confirmar = input(f"¿Está seguro de eliminar el torneo {torneo['nombre']}? (S/N): ").strip().upper()
    if confirmar != "S":
        print("Operación cancelada.")
        congelar()
        return
    
    
    # 1. Eliminar partidos del torneo
    partidos = leer_json('data/partidos.json')
    partidos = [p for p in partidos if p['id_torneo'] != id_torneo]
    escribir_json('data/partidos.json', partidos)
    
    # 2. Eliminar estadísticas del torneo
    estadisticas = leer_json('data/estadisticas.json')
    estadisticas = [s for s in estadisticas if s['id_torneo'] != id_torneo]
    escribir_json('data/estadisticas.json', estadisticas)
    
    # 3. Eliminar torneo
    torneos = [t for t in torneos if t['id'] != id_torneo]
    escribir_json('data/torneos.json', torneos)
    
    print(f"\nTorneo {torneo['nombre']} eliminado exitosamente!")
    congelar()