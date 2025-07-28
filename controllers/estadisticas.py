from utils.helpers import limpiar, congelar, leer_json
from utils.validadores import validar_entero
import json

def ver_estadisticas():
    limpiar()
    print("  ========================== ")
    print("___ESTADÍSTICAS DEL TORNEO___")
    print("  ========================== ")
    
    torneos = leer_json('data/torneos.json')
    equipos = leer_json('data/equipos.json')
    estadisticas = leer_json('data/estadisticas.json')
    
    if not torneos:
        print("No hay torneos registrados.")
        congelar()
        return
    
    print("\nTorneos disponibles:")
    for torneo in torneos:
        print(f"{torneo['id']}. {torneo['nombre']}")
    
    id_torneo = validar_entero("\nSeleccione el ID del torneo: ")
    torneo_seleccionado = next((t for t in torneos if t['id'] == id_torneo), None)
    
    if not torneo_seleccionado:
        print("ID de torneo no válido.")
        congelar()
        return
    
    # Filtrar estadísticas solo para este torneo
    stats_torneo = [s for s in estadisticas if s['id_torneo'] == id_torneo]
    
    if not stats_torneo:
        print("No hay estadísticas registradas para este torneo.")
        congelar()
        return
    
    # Ordenar por puntos (descendente) y diferencia de goles (descendente)
    stats_ordenadas = sorted(
        stats_torneo,
        key=lambda x: (x['puntos'], x['dg']),
        reverse=True
    )
    
    # Mostrar tabla de posiciones
    limpiar()
    print(f"=== TABLA DE POSICIONES - {torneo_seleccionado['nombre'].upper()} ===")
    print("\nPos.  Equipo                PJ   PG   PE   PP   GF   GC   DG   Pts.")
    print("-" * 65)
    
    for posicion, stat in enumerate(stats_ordenadas, 1):
        equipo = next((e for e in equipos if e['id'] == stat['id_equipo']), None)
        nombre_equipo = equipo['nombre'] if equipo else "Desconocido"
        
        print(f"{posicion:<5} {nombre_equipo[:20]:<20} "
              f"{stat['pj']:>3}  {stat['pg']:>3}  {stat['pe']:>3}  {stat['pp']:>3}  "
              f"{stat['gf']:>3}  {stat['gc']:>3}  {stat['dg']:>3}  {stat['puntos']:>4}")
    
    congelar()

def actualizar_estadisticas(estadisticas, id_torneo, id_equipo, resultado, goles_favor, goles_contra):
    # Buscar o crear estadística del equipo en el torneo
    stat = next(
        (s for s in estadisticas 
         if s['id_torneo'] == id_torneo and s['id_equipo'] == id_equipo),
        None
    )
    
    if not stat:
        stat = {
            'id': len(estadisticas) + 1,
            'id_torneo': id_torneo,
            'id_equipo': id_equipo,
            'pj': 0,
            'pg': 0,
            'pe': 0,
            'pp': 0,
            'gf': 0,
            'gc': 0,
            'dg': 0,
            'puntos': 0
        }
        estadisticas.append(stat)
    
    # Actualizar valores
    stat['pj'] += 1
    stat['gf'] += goles_favor
    stat['gc'] += goles_contra
    stat['dg'] = stat['gf'] - stat['gc']
    
    if resultado == 'ganado':
        stat['pg'] += 1
        stat['puntos'] += 3
    elif resultado == 'empatado':
        stat['pe'] += 1
        stat['puntos'] += 1
    else:  # perdido
        stat['pp'] += 1