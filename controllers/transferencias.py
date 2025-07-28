import json
from utils.helpers import limpiar, congelar, leer_json, escribir_json
from utils.validadores import validar_texto, validar_entero
from datetime import datetime

def seleccionar_torneo():
    torneos = leer_json('data/torneos.json')
    
    if not torneos:
        print("No hay torneos registrados.")
        congelar()
        return None
    
    print("\nTorneos disponibles:")
    for torneo in torneos:
        print(f"{torneo['id']}. {torneo['nombre']}")
    
    id_torneo = validar_entero("\nSeleccione ID del torneo: ")
    return next((t for t in torneos if t['id'] == id_torneo), None)

def seleccionar_equipo(torneo):
    equipos = leer_json('data/equipos.json')
    equipos_torneo = [e for e in equipos if e['id'] in torneo['equipos_inscritos']]
    
    if not equipos_torneo:
        print("Este torneo no tiene equipos inscritos.")
        congelar()
        return None
    
    print(f"\nEquipos inscritos en {torneo['nombre']}:")
    for equipo in equipos_torneo:
        print(f"{equipo['id']}. {equipo['nombre']}")
    
    id_equipo = validar_entero("\nSeleccione ID del equipo: ")
    return next((e for e in equipos_torneo if e['id'] == id_equipo), None)

def seleccionar_jugador(equipo):
    jugadores = leer_json('data/jugadores.json')
    jugadores_equipo = [j for j in jugadores if j['id_equipo'] == equipo['id']]
    
    if not jugadores_equipo:
        print("Este equipo no tiene jugadores registrados.")
        congelar()
        return None
    
    print(f"\nJugadores de {equipo['nombre']}:")
    for jugador in jugadores_equipo:
        print(f"{jugador['id']}. {jugador['nombre']} (Dorsal: {jugador['dorsal']}, Posición: {jugador['posicion']})")
    
    id_jugador = validar_entero("\nSeleccione ID del jugador: ")
    return next((j for j in jugadores_equipo if j['id'] == id_jugador), None)

def gestionar_transferencia():
    limpiar()
    print("=================================")
    print("=== GESTIÓN DE TRANSFERENCIAS ===")
    print("=================================")
    
    # Paso 1: Seleccionar torneo
    torneo = seleccionar_torneo()
    if not torneo:
        return
    
    # Paso 2: Seleccionar equipo origen
    print("\nSeleccione equipo ORIGEN:")
    equipo_origen = seleccionar_equipo(torneo)
    if not equipo_origen:
        return
    
    # Paso 3: Seleccionar jugador
    jugador = seleccionar_jugador(equipo_origen)
    if not jugador:
        return
    
    # Paso 4: Seleccionar equipo destino
    print("\nSeleccione equipo DESTINO:")
    equipo_destino = seleccionar_equipo(torneo)
    if not equipo_destino:
        return
    
    if equipo_origen['id'] == equipo_destino['id']:
        print("No puede transferir a un jugador al mismo equipo.")
        congelar()
        return
    
    # Paso 5: Seleccionar tipo de transferencia
    print("\nTipos de transferencia:")
    print("1. Venta")
    print("2. Préstamo")
    tipo_transferencia = validar_entero("Seleccione tipo (1-2): ")
    
    if tipo_transferencia not in [1, 2]:
        print("Opción no válida.")
        congelar()
        return
    
    tipo = "Venta" if tipo_transferencia == 1 else "Préstamo"
    monto = 0
    fecha_fin = None
    
    if tipo == "Venta":
        monto = validar_entero("Monto de la transferencia: ")
    else:
        fecha_fin = validar_texto("Fecha de fin de préstamo (DD/MM/AAAA): ")
    
    # Registrar la transferencia
    transferencias = leer_json('data/transferencias.json')
    
    nueva_transferencia = {
        'id': len(transferencias) + 1,
        'id_jugador': jugador['id'],
        'nombre_jugador': jugador['nombre'],
        'equipo_origen': equipo_origen['id'],
        'nombre_equipo_origen': equipo_origen['nombre'],
        'equipo_destino': equipo_destino['id'],
        'nombre_equipo_destino': equipo_destino['nombre'],
        'tipo': tipo,
        'monto': monto,
        'fecha': datetime.now().strftime("%d/%m/%Y"),
        'fecha_fin': fecha_fin if tipo == "Préstamo" else None
    }
    
    transferencias.append(nueva_transferencia)
    escribir_json('data/transferencias.json', transferencias)
    
    # Actualizar jugador (mover a nuevo equipo)
    jugadores = leer_json('data/jugadores.json')
    for j in jugadores:
        if j['id'] == jugador['id']:
            j['id_equipo'] = equipo_destino['id']
            break
    
    escribir_json('data/jugadores.json', jugadores)
    
    # Actualizar equipos
    equipos = leer_json('data/equipos.json')
    for e in equipos:
        if e['id'] == equipo_origen['id'] and jugador['id'] in e['jugadores']:
            e['jugadores'].remove(jugador['id'])
        elif e['id'] == equipo_destino['id']:
            e['jugadores'].append(jugador['id'])
    
    escribir_json('data/equipos.json', equipos)
    
    print(f"\nTransferencia de {jugador['nombre']} registrada exitosamente!")
    print(f"De {equipo_origen['nombre']} a {equipo_destino['nombre']} ({tipo})")
    congelar()