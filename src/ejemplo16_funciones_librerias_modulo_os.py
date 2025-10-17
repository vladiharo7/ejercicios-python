'''
Crea un script en Python que utilice el módulo os para listar todos los 
archivos (no directorios) en el directorio actual, ordenados 
por tamaño (de mayor a menor). Para cada archivo, muestra su nombre y tamaño en bytes.

El script debe:

Obtener la lista de todos los elementos en el directorio actual
Filtrar solo los archivos (no directorios)
Obtener el tamaño de cada archivo usando las funciones apropiadas
Ordenar la lista de archivos por tamaño de forma descendente
Mostrar el nombre y tamaño de cada archivo
Puedes empezar importando el módulo os y utilizando os.listdir() para obtener los elementos del directorio actual.
'''
import os
from os import path
from operator import itemgetter
from pprint import pprint

# Obtener la lista de todos los elementos en el directorio actual
elementos = os.listdir('.')

# Filtrar solo los archivos y obtener su tamaño
archivos_con_tamano = []
for elemento in elementos:
    if path.isfile(elemento):
        tamano = path.getsize(elemento)
        archivos_con_tamano.append((elemento, tamano))

# Ordenar la lista de archivos por tamaño de forma descendente
archivos_ordenados = sorted(archivos_con_tamano, key=itemgetter(1), reverse=True)

# Mostrar el nombre y tamaño de cada archivo
pprint(archivos_ordenados)

# Alternativamente, usando list comprehension
archivos_con_tamano_lc = [(f, path.getsize(f)) for f in elementos if path.isfile(f)]
archivos_ordenados_lc = sorted(archivos_con_tamano_lc, key=itemgetter(1), reverse=True)
pprint(archivos_ordenados_lc)

# Otra alternativa usando lambda
archivos_ordenados_lambda = sorted(archivos_con_tamano, key=lambda x: x[1], reverse=True)
pprint(archivos_ordenados_lambda)
