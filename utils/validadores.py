def validar_entero(mensaje):
    """Valida que el input sea un número entero"""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def validar_flotante(mensaje):
    """Valida que el input sea un número flotante"""
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debe ingresar un número válido.")

def validar_texto(mensaje, min_len=1):
    """Valida que el input sea un texto no vacío"""
    while True:
        valor = input(mensaje).strip()
        if len(valor) >= min_len:
            return valor
        print(f"Error: El texto debe tener al menos {min_len} caracteres.")