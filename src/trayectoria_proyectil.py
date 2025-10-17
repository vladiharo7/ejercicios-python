'''
Calcula la trayectoria de un proyectil lanzado con una velocidad inicial y un ángulo dado.
'''
import math

def calcular_trayectoria(velocidad_inicial, angulo_grados, altura_inicial=0):
    """Calcula la distancia máxima y altura máxima de un proyectil."""
    # Convertir ángulo a radianes
    angulo_rad = math.radians(angulo_grados)

    # Constantes
    g = 9.8  # Aceleración debido a la gravedad (m/s²)

    # Componentes de la velocidad
    v0x = velocidad_inicial * math.cos(angulo_rad)
    v0y = velocidad_inicial * math.sin(angulo_rad)

    # Tiempo de vuelo
    tiempo_vuelo = (v0y + math.sqrt(v0y**2 + 2*g*altura_inicial)) / g

    # Distancia máxima
    distancia_maxima = v0x * tiempo_vuelo

    # Altura máxima
    altura_maxima = altura_inicial + (v0y**2) / (2*g)

    return distancia_maxima, altura_maxima

# Ejemplo de uso
velocidad = 20  # m/s
angulo = 45     # grados
altura = 1.5    # metros

distancia, altura_max = calcular_trayectoria(velocidad, angulo, altura)

print(f"Un proyectil lanzado a {velocidad} m/s con un ángulo de {angulo}° desde {altura} m de altura:")
print(f"- Alcanzará una distancia máxima de {distancia:.2f} metros")
print(f"- Llegará a una altura máxima de {altura_max:.2f} metros")
