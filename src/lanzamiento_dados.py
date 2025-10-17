'''
Simulación de lanzamiento de un dado cargado usando random.choices
'''
import random

# Simulación de lanzamiento de dado cargado
# El 6 tiene el doble de probabilidad que los demás números
caras_dado = [1, 2, 3, 4, 5, 6]
pesos = [1, 1, 1, 1, 1, 2]  # El 6 tiene peso 2, los demás peso 1

# Simular 20 lanzamientos del dado cargado
lanzamientos = random.choices(caras_dado, weights=pesos, k=20)
print(f"Resultados de 20 lanzamientos: {lanzamientos}")

# Contar frecuencias
frecuencias = {cara: lanzamientos.count(cara) for cara in caras_dado}
print(f"Frecuencias: {frecuencias}")
