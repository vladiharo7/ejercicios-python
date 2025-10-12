'''
Implementa una función llamada analizar_texto que reciba como parámetro una
cadena de texto y devuelva un diccionario con las siguientes estadísticas:

caracteres_mas_comunes: Una lista con los 3 caracteres más comunes y su frecuencia, 
excluyendo espacios en blanco. El formato debe ser una lista de tuplas (caracter, frecuencia).

total_caracteres: El número total de caracteres en el texto, incluyendo espacios.

total_sin_espacios: El número total de caracteres excluyendo espacios en blanco.

Utiliza la clase Counter del módulo collections para realizar el análisis de frecuencias.

Ejemplo de uso:

resultado = analizar_texto("Hola, mundo! Este es un ejemplo.")
print(resultado)
# Debería imprimir algo como:
# {'caracteres_mas_comunes': [('e', 4), ('o', 3), ('l', 2)], 'total_caracteres': 32, 'total_sin_espacios': 27}
'''

from collections import Counter

def analizar_texto(texto: str) -> dict:

    '''
    Analiza el texto y devuelve estadísticas sobre los caracteres.
    Parameters:
        texto (str): Cadena de texto a analizar.
        Returns:
        dict: Diccionario con las estadísticas solicitadas.
    '''

    # Contar la frecuencia de cada carácter, excluyendo espacios
    contador = Counter(texto.replace(" ", ""))

    # Obtener los 3 caracteres más comunes
    caracteres_mas_comunes = contador.most_common(3)

    # Calcular el total de caracteres y el total sin espacios
    total_caracteres = len(texto)
    total_sin_espacios = len(texto.replace(" ", ""))

    # Crear el diccionario con las estadísticas
    resultado_dic = {
        "caracteres_mas_comunes": caracteres_mas_comunes,
        "total_caracteres": total_caracteres,
        "total_sin_espacios": total_sin_espacios
    }

    return resultado_dic

# Ejemplo de uso
resultado = analizar_texto("Hola, mundo! Este es un ejemplo.")
print(resultado)
