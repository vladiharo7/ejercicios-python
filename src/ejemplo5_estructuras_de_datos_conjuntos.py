'''
Crea un programa que trabaje con dos listas de números enteros.
Debes convertir estas listas a conjuntos y realizar las siguientes operaciones:

Encuentra los elementos que aparecen en ambas listas (intersección)
Encuentra los elementos que solo aparecen en la primera lista (diferencia)
Encuentra los elementos que solo aparecen en la segunda lista (diferencia)
Encuentra todos los elementos únicos que aparecen en cualquiera de las dos listas (unión)
Utiliza las siguientes listas para tu programa:

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]
Imprime el resultado de cada operación en líneas separadas.
'''

# Definir las listas
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

# Convertir las listas a conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Encontrar la intersección (elementos en ambas listas)
interseccion = conjunto1.intersection(conjunto2)
print("Intersección:", interseccion)

# Encontrar los elementos que solo aparecen en la primera lista (diferencia)
diferencia1 = conjunto1.difference(conjunto2)
print(f"Elementos solo en la primera lista: {diferencia1}")

# Encontrar los elementos que solo aparecen en la segunda lista (diferencia)
diferencia2 = conjunto2.difference(conjunto1)
print(f"Elementos solo en la segunda lista: {diferencia2}")

# Encontrar todos los elementos únicos que aparecen en cualquiera de las dos listas (unión)
union = conjunto1.union(conjunto2)
print(f"Unión: {union}")
