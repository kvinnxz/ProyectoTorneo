from utils.helpers import limpiar, congelar, leer_json, escribir_json
from utils.validadores import validar_texto, validar_entero
import json

def registrar_equipo():
    limpiar()
    print(" ========================== ")
    print("|| REGISTRAR NUEVO EQUIPO ||")
    print(" ========================== ")
    equipos = leer_json('data/equipos.json')
    
    nuevo_equipo = {
        'id': len(equipos) + 1,
        'nombre': validar_texto("Nombre del equipo: "),
        'fundacion': validar_entero("Año de fundación: "),
        'estadio': validar_texto("Nombre del estadio: "),
        'jugadores': [],
        'cuerpo_tecnico': []
    }
    
    equipos.append(nuevo_equipo)
    escribir_json('data/equipos.json', equipos)
    
    print(f"\nEquipo {nuevo_equipo['nombre']} registrado exitosamente!")
    congelar()

def ver_equipos():
    limpiar()
    print("=== LISTADO DE EQUIPOS ===")
    
    equipos = leer_json('data/equipos.json')
    
    if not equipos:
        print("No hay equipos registrados.")
    else:
        for equipo in equipos:
            print(f"\nID: {equipo['id']}")
            print(f"Nombre: {equipo['nombre']}")
            print(f"Año fundación: {equipo['fundacion']}")
            print(f"Estadio: {equipo['estadio']}")
            print(f"Jugadores: {len(equipo['jugadores'])}")
            print(f"Cuerpo técnico: {len(equipo['cuerpo_tecnico'])}")
            print("-" * 30)
    
    congelar()

def borrar_equipo():
    limpiar()
    print("=== ELIMINAR EQUIPO ===")
    
    equipos = leer_json('data/equipos.json')
    
    if not equipos:
        print("No hay equipos registrados.")
        congelar()
        return
    
    print("\nEquipos disponibles:")
    for equipo in equipos:
        print(f"{equipo['id']}. {equipo['nombre']}")
    
    id_equipo = validar_entero("\nIngrese ID del equipo a eliminar: ")
    equipo = next((e for e in equipos if e['id'] == id_equipo), None)
    
    if not equipo:
        print("ID de equipo no válido.")
        congelar()
        return
    
    # Confirmación
    confirmar = input(f"¿Está seguro de eliminar el equipo {equipo['nombre']}? (S/N): ").strip().upper()
    if confirmar != "S":
        print("Operación cancelada.")
        congelar()
        return
    
    # 1. Eliminar jugadores del equipo
    jugadores = leer_json('data/jugadores.json')
    jugadores = [j for j in jugadores if j['id_equipo'] != id_equipo]
    escribir_json('data/jugadores.json', jugadores)
    
    # 2. Eliminar cuerpo técnico del equipo
    cuerpo_tecnico = leer_json('data/cuerpotecnico.json')
    cuerpo_tecnico = [c for c in cuerpo_tecnico if c['id_equipo'] != id_equipo]
    escribir_json('data/cuerpotecnico.json', cuerpo_tecnico)
    
    # 3. Actualizar torneos (quitar equipo inscrito)
    torneos = leer_json('data/torneos.json')
    for torneo in torneos:
        if id_equipo in torneo['equipos_inscritos']:
            torneo['equipos_inscritos'].remove(id_equipo)
    escribir_json('data/torneos.json', torneos)
    
    # 4. Eliminar equipo
    equipos = [e for e in equipos if e['id'] != id_equipo]
    escribir_json('data/equipos.json', equipos)
    
    print(f"\nEquipo {equipo['nombre']} eliminado exitosamente!")
    congelar()