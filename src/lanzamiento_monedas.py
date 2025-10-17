'''
Simulación de lanzamientos de monedas usando random con control de semilla
'''
import random

def simular_lanzamientos(n_lanzamientos, semilla=None):
    """Simula n lanzamientos de moneda y devuelve el número de caras."""
    # Establecer la semilla si se proporciona
    if semilla is not None:
        random.seed(semilla)

    # Simular lanzamientos (1: cara, 0: cruz)
    lanzamientos = [random.randint(0, 1) for _ in range(n_lanzamientos)]

    return sum(lanzamientos)  # Número total de caras

# Ejecutar la simulación con una semilla fija
resultado1 = simular_lanzamientos(1000, semilla=42)
print(f"Simulación 1: {resultado1} caras en 1000 lanzamientos")

# Ejecutar de nuevo con la misma semilla
resultado2 = simular_lanzamientos(1000, semilla=42)
print(f"Simulación 2: {resultado2} caras en 1000 lanzamientos")

# Ejecutar con una semilla diferente
resultado3 = simular_lanzamientos(1000, semilla=123)
print(f"Simulación 3: {resultado3} caras en 1000 lanzamientos")

# Ejecutar sin semilla (resultados no reproducibles)
resultado4 = simular_lanzamientos(1000)
print(f"Simulación 4: {resultado4} caras en 1000 lanzamientos")
