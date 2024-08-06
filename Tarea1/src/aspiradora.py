import time
import random

# Diccionario que contiene los estados posibles de la aspiradora.
# La clave es el estado de la aspiradora y el valor es una lista con:
# 1. Número de estado asociado a la imagen.
# 2. Contador de cuántas veces ha estado en ese estado.
posibles_estados = {
    ('A', 'DIRTY', 'DIRTY'): [1, 0],
    ('B', 'DIRTY', 'DIRTY'): [2, 0],
    ('A', 'DIRTY', 'CLEAN'): [3, 0],
    ('B', 'DIRTY', 'CLEAN'): [4, 0],
    ('A', 'CLEAN', 'DIRTY'): [5, 0],
    ('B', 'CLEAN', 'DIRTY'): [6, 0],
    ('A', 'CLEAN', 'CLEAN'): [7, 0],
    ('B', 'CLEAN', 'CLEAN'): [8, 0]
}

def visito_todos() -> bool:
    """
    Verifica si todos los estados han sido visitados al menos una vez.
    
    Returns:
        bool: True si todos los estados han sido visitados, False de lo contrario.
    """
    return all(valores[1] > 0 for valores in posibles_estados.values())

def reflex_agent(location, state):
    """
    Decide la acción a tomar según la ubicación y el estado actual.

    Args:
        location (str): Ubicación actual de la aspiradora ('A' o 'B').
        state (str): Estado de la habitación actual ('DIRTY', 'CLEAN', 'REPEATED').

    Returns:
        str: Acción a realizar ('CLEAN', 'RIGHT', 'LEFT').
    """
    if state == "DIRTY":
        return 'CLEAN'
    elif state == "REPEATED":
        return 'DIRTY'
    elif location == 'A':
        return 'RIGHT'
    elif location == 'B':
        return 'LEFT'

def test(states):
    """
    Ejecuta la simulación del agente reflexivo a través de los diferentes estados posibles.

    Args:
        states (list): Lista que contiene el estado inicial de la aspiradora y las habitaciones.
    """
    while True:
        location = states[0]
        # Selecciona el estado correspondiente a la ubicación
        state = states[2] if location == 'A' else states[1]

        estado_visitado = posibles_estados[tuple(states)]
        estado_actual = estado_visitado[0]

        if estado_visitado[1] == 0:
            posibles_estados[tuple(states)][1] += 1
        else:
            # Cambia aleatoriamente el estado de una habitación
            habitacion = random.randint(1, 2)
            states[habitacion] = 'DIRTY'
            action = reflex_agent(location, 'REPEATED')
            print(f"Ubicación: {location} | Acción: {action} | Estado actual: {estado_actual}")
            continue

        action = reflex_agent(location, state)
        print(f"Ubicación: {location} | Acción: {action} | Estado actual: {estado_actual}")

        if action == "CLEAN":
            # Limpia la habitación correspondiente
            if location == 'A':
                states[1] = "CLEAN"
            elif location == 'B':
                states[2] = "CLEAN"
        elif action == "RIGHT":
            states[0] = 'B'
        elif action == "LEFT":
            states[0] = 'A'

        if visito_todos():
            break
        time.sleep(3)

# Inicia la prueba con ambas habitaciones sucias y la aspiradora en la habitación A
test(['A', 'DIRTY', 'DIRTY'])
