print("----------------------------------------------------------------")
# Estructura mixta: diccionario de listas de diccionarios
estudiantes_por_clase = {
    "Matemáticas": [
        {"nombre": "Ana", "calificaciones": [85, 90, 88]},
        {"nombre": "Carlos", "calificaciones": [75, 82, 79]}
    ],
    "Historia": [
        {"nombre": "Elena", "calificaciones": [92, 88, 95]},
        {"nombre": "David", "calificaciones": [78, 85, 80]}
    ]
}

# Recorremos la estructura mixta
for clase, lista_estudiantes in estudiantes_por_clase.items():
    print(f"Clase: {clase}")
    for estudiante in lista_estudiantes:
        nombre = estudiante["nombre"]
        promedio = sum(estudiante["calificaciones"]) / len(estudiante["calificaciones"])
        print(f"  {nombre}: Promedio = {promedio:.1f}")

print("----------------------------------------------------------------")
print("Tabla de multiplicar del 1 al 10")

# Creamos una matriz de multiplicación 10x10
tabla_multiplicar = []

for i in range(1, 11):
    fila = []
    for j in range(1, 11):
        fila.append(i * j)
    tabla_multiplicar.append(fila)

# Imprimimos la tabla de forma ordenada
for fila in tabla_multiplicar:
    # Usamos join para formatear cada fila como una cadena de texto
    print(" ".join(f"{num:3}" for num in fila))


print("----------------------------------------------------------------")

# Creamos la misma matriz de multiplicación con comprensión de listas
tabla_multiplicar = [[i * j for j in range(1, 11)] for i in range(1, 11)]

# Imprimimos la tabla
for fila in tabla_multiplicar:
    print(" ".join(f"{num:3}" for num in fila))

print("----------------------------------------------------------------")

# Estructura 3D: 2 semanas x 3 días x 4 mediciones
datos_clima = [
    # Semana 1
    [
        [15, 17, 19, 16],  # Día 1
        [14, 16, 18, 15],  # Día 2
        [13, 15, 17, 14]   # Día 3
    ],
    # Semana 2
    [
        [16, 18, 20, 17],  # Día 1
        [15, 17, 19, 16],  # Día 2
        [14, 16, 18, 15]   # Día 3
    ]
]

# Recorremos la estructura 3D
for s, semana in enumerate(datos_clima):
    print(f"Semana {s+1}:")
    for d, dia in enumerate(semana):
        print(f"  Día {d+1}:")
        for h, temperatura in enumerate(dia):
            print(f"    Hora {h+1}: {temperatura}°C")

print("----------------------------------------------------------------")
# Matriz de temperaturas diarias (5 días, 3 mediciones por día)
temperaturas = [
    [22, 24, 19],  # Día 1
    [21, 25, 20],  # Día 2
    [23, 28, 21],  # Día 3
    [20, 22, 18],  # Día 4
    [19, 21, 17]   # Día 5
]

# Calculamos la temperatura promedio por día
for i, dia in enumerate(temperaturas):
    promedio = sum(dia) / len(dia)
    print(f"Día {i+1}: Temperatura promedio = {promedio:.1f}°C")

# Encontramos la temperatura máxima de toda la semana
temperatura_maxima = 0
dia_max, medicion_max = 0, 0

for i, dia in enumerate(temperaturas):
    for j, temp in enumerate(dia):
        if temp > temperatura_maxima:
            temperatura_maxima = temp
            dia_max, medicion_max = i+1, j+1

print(f"La temperatura máxima fue {temperatura_maxima}°C en el día {dia_max}, medición {medicion_max}")

print("----------------------------------------------------------------")
# Función para calcular estadísticas de una matriz
def calcular_estadisticas(matriz):
    """Calcula mínimo, máximo y promedio de una matriz."""
    if not matriz or not matriz[0]:
        return None

    minimo = maximo = matriz[0][0]
    suma = 0
    elementos = 0

    for fila in matriz:
        for valor in fila:
            minimo = min(minimo, valor)
            maximo = max(maximo, valor)
            suma += valor
            elementos += 1

    return {
        "mínimo": minimo,
        "máximo": maximo,
        "promedio": suma / elementos
    }

# Ejemplo de uso
datos = [
    [5, 8, 2],
    [3, 7, 1],
    [9, 4, 6]
]

estadisticas = calcular_estadisticas(datos)
print(f"Estadísticas: {estadisticas}")

print("----------------------------------------------------------------")
# Datos de sensores (temperatura, humedad, presión)
datos_sensores = [
    [22.5, 45, 1013],
    [23.1, 42, 1012],
    [22.8, 44, 1014],
    [23.4, 40, 1015],
    [22.9, 43, 1013]
]

# Umbrales para cada medida
umbrales = [23.0, 43, 1014]
etiquetas = ["Temperatura", "Humedad", "Presión"]

# Procesamos los datos por lotes
for i, mediciones in enumerate(datos_sensores):
    alertas = []
    
    # Comparamos cada medición con su umbral correspondiente
    for medida, umbral, etiqueta in zip(mediciones, umbrales, etiquetas):
        if medida > umbral:
            alertas.append(f"{etiqueta} alta: {medida}")
    
    if alertas:
        print(f"Sensor {i+1}: {', '.join(alertas)}")
    else:
        print(f"Sensor {i+1}: Valores normales")
print("----------------------------------------------------------------")

calificaciones = {"Matemáticas": 85, "Historia": 92, "Ciencias": 78}
creditos = [4, 3, 5]  # Créditos correspondientes a cada asignatura

for (asignatura, nota), credito in zip(calificaciones.items(), creditos):
    print(f"{asignatura}: {nota} puntos - {credito} créditos")
print("----------------------------------------------------------------")
# Transponer una matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transponemos la matriz (convertimos filas en columnas)
matriz_transpuesta = list(zip(*matriz))
print(matriz_transpuesta)  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

print("----------------------------------------------------------------")
claves = ["nombre", "edad", "ciudad"]
valores = ["Laura", 29, "Madrid"]

# Creamos un diccionario
persona = dict(zip(claves, valores))
print(persona)  # {'nombre': 'Laura', 'edad': 29, 'ciudad': 'Madrid'}

print("----------------------------------------------------------------")
import itertools

# Parámetros de configuración
tamaños = ['pequeño', 'mediano', 'grande']
colores = ['rojo', 'verde', 'azul']
materiales = ['madera', 'metal', 'plástico']

# Generamos todas las combinaciones posibles
configuraciones = list(itertools.product(tamaños, colores, materiales))

print(f"Total de configuraciones: {len(configuraciones)}")
for i, config in enumerate(configuraciones[:5], 1):  # Mostramos solo las primeras 5
    tamaño, color, material = config
    print(f"Configuración {i}: {tamaño}, {color}, {material}")

print("----------------------------------------------------------------")

# Buscamos combinaciones de números que sumen 10
for a, b, c in itertools.product(range(10), range(10), range(10)):
    if a + b + c == 10 and a <= b <= c:  # Ordenados para evitar duplicados
        print(f"{a} + {b} + {c} = 10")

print("----------------------------------------------------------------")

# Generar todas las combinaciones posibles de 3 dígitos (0-9)
codigos = list(itertools.product(range(10), repeat=3))

print(f"Total de códigos posibles: {len(codigos)}")
print(f"Primeros 5 códigos: {codigos[:5]}")
print(f"Últimos 5 códigos: {codigos[-5:]}")
