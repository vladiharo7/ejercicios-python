'''
Ejemplo de uso de la función filter() para filtrar elementos en una lista.
'''

# Lista de productos
productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 5},
    {"nombre": "Teléfono", "precio": 800, "stock": 0},
    {"nombre": "Tablet", "precio": 350, "stock": 10},
    {"nombre": "Auriculares", "precio": 150, "stock": 0},
    {"nombre": "Monitor", "precio": 400, "stock": 3}
]

# Filtrar productos en stock
en_stock = list(filter(lambda p: p["stock"] > 0, productos))
print("Productos en stock:")
for producto in en_stock:
    print(f"- {producto['nombre']} (${producto['precio']})")

# Filtrar productos premium (precio > 500)
premium = list(filter(lambda p: p["precio"] > 500, productos))
print("\nProductos premium:")
for producto in premium:
    print(f"- {producto['nombre']} (${producto['precio']})")
# --- IGNORE ---

print('--------------------------------------------------')

# Eliminar valores nulos o vacíos de una lista de datos
datos_usuario = ["Ana", "", None, "Carlos", "", "Elena", None]
datos_limpios = list(filter(None, datos_usuario))
print(datos_limpios)  # ['Ana', 'Carlos', 'Elena']

print('--------------------------------------------------')

# Filtrar valores numéricos válidos
def es_numero(valor):
    '''Verifica si el valor puede convertirse a float.'''
    try:
        float(valor)
        return True
    except (ValueError, TypeError):
        return False

entradas = ["42", "abc", "7.5", None, "100", "", "3,5"]
numeros_validos = list(filter(es_numero, entradas))
print(numeros_validos)  # ['42', '7.5', '100']
# --- END IGNORE ---

print('--------------------------------------------------')
'''
Ejemplo avanzado: Filtrar días con condiciones múltiples.
'''

# Datos de temperatura diaria durante un mes
temperaturas = [
    {"dia": 1, "temp": 22.5, "lluvia": False},
    {"dia": 2, "temp": 19.8, "lluvia": True},
    {"dia": 3, "temp": 25.1, "lluvia": False},
    {"dia": 4, "temp": 28.4, "lluvia": False},
    {"dia": 5, "temp": 18.9, "lluvia": True},
    # ... más datos
]

# Días calurosos (temperatura > 25°C)
dias_calurosos = list(filter(lambda d: d["temp"] > 25, temperaturas))
print(f"Días con temperatura > 25°C: {len(dias_calurosos)}")

# Días sin lluvia
dias_sin_lluvia = list(filter(lambda d: not d["lluvia"], temperaturas))
print(f"Días sin lluvia: {len(dias_sin_lluvia)}")

# Días calurosos sin lluvia (combinando condiciones)
dias_ideales = list(filter(
    lambda d: d["temp"] > 25 and not d["lluvia"], 
    temperaturas
))
print(f"Días ideales: {len(dias_ideales)}")

print('--------------------------------------------------')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Primero filtrar números pares, luego calcular sus cuadrados
pares_al_cuadrado = list(map(
    lambda x: x**2,
    filter(lambda x: x % 2 == 0, numeros)
))
print(pares_al_cuadrado)  # [4, 16, 36, 64, 100]

# Filtrar palabras que contienen 'a' y convertirlas a mayúsculas
palabras = ["casa", "perro", "gato", "elefante", "ratón"]
con_a_mayusculas = list(map(
    lambda p: p.upper(),
    filter(lambda p: 'a' in p, palabras)
))
print(con_a_mayusculas)  # ['CASA', 'GATO', 'ELEFANTE', 'RATÓN']

print('--------------------------------------------------')

import re

# Lista de correos electrónicos
correos = [
    "usuario@ejemplo.com",
    "nombre.apellido@empresa.es",
    "contacto@sitio.co.uk",
    "no-es-un-correo",
    "otro@dominio",
    "correo@valido.org"
]

# Patrón simple para validar correos electrónicos
patron = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

# Filtrar correos válidos
correos_validos = list(filter(
    lambda c: patron.match(c) is not None,
    correos
))
print(correos_validos)
# ['usuario@ejemplo.com', 'nombre.apellido@empresa.es', 'contacto@sitio.co.uk', 'correo@valido.org']

print('--------------------------------------------------')

from itertools import count

# Generar números primos usando filter con una secuencia infinita
def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Crear un iterador de números primos
# count() genera números infinitamente, filter selecciona solo los primos
primos = filter(es_primo, count(1))

# Obtener los primeros 10 números primos
primeros_primos = []
for _ in range(10):
    primeros_primos.append(next(primos))

print(primeros_primos)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

