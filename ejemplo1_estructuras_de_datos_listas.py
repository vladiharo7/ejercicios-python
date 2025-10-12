'''
Crea una lista llamada numeros que contenga los valores 10, 20, 30, 40 y 50. A continuación, 
realiza las siguientes operaciones:

Añade el número 60 al final de la lista
Inserta el número 15 entre el 10 y el 20
Elimina el número 30 de la lista
Calcula la suma de todos los números en la lista y guárdala en una variable llamada suma
Calcula el promedio de los números en la lista y guárdalo en una variable llamada promedio
Al final, imprime la lista resultante, la suma y el promedio.

'''

# Crear la lista inicial
numeros = [10, 20, 30, 40, 50]

# Añadir el número 60 al final de la lista
numeros.append(60)

# Insertar el número 15 entre el 10 y el 20
numeros.insert(1, 15)

# Eliminar el número 30 de la lista
numeros.remove(30)

# Calcular la suma de todos los números en la lista
suma = sum(numeros)

# Calcular el promedio de los números en la lista
promedio = suma / len(numeros)

# Imprimir la lista resultante, la suma y el promedio
print("Lista resultante:", numeros)
print("Suma:", suma)
print("Promedio:", promedio)
