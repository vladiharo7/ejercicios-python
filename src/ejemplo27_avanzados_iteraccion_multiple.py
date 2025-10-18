'''
Crea una matriz de multiplicación de 5x5 utilizando bucles anidados. 
La matriz debe contener el resultado de multiplicar el número de fila por el número de columna. 
Por ejemplo, en la posición [2][3] debe estar el valor 6 (2×3). 
Después de crear la matriz, muestra su contenido en la consola con un formato de tabla, 
donde cada fila aparezca en una línea diferente y los números estén separados por espacios.
'''

# Crear la matriz de multiplicación
matriz = []
START_RANGE = 1
END_RANGE = 6
for i in range(START_RANGE,END_RANGE):
    fila = []
    for j in range(START_RANGE, END_RANGE):
        fila.append(i * j)
    matriz.append(fila)

# Mostrar la matriz en formato de tabla
for fila in matriz:
    print(' '.join(f'{num:2}' for num in fila))
