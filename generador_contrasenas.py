import random
import string

def generar_contrasena(longitud=12, incluir_mayusculas=True, 
                       incluir_numeros=True, incluir_simbolos=True):
    """Genera una contraseña aleatoria con los criterios especificados."""
    # Definir los conjuntos de caracteres
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase if incluir_mayusculas else ""
    numeros = string.digits if incluir_numeros else ""
    simbolos = string.punctuation if incluir_simbolos else ""

    # Combinar todos los caracteres disponibles
    todos_caracteres = minusculas + mayusculas + numeros + simbolos

    # Asegurar que al menos un carácter de cada tipo requerido esté presente
    caracteres_requeridos = []
    if minusculas:
        caracteres_requeridos.append(random.choice(minusculas))
    if mayusculas:
        caracteres_requeridos.append(random.choice(mayusculas))
    if numeros:
        caracteres_requeridos.append(random.choice(numeros))
    if simbolos:
        caracteres_requeridos.append(random.choice(simbolos))

    # Completar el resto de la contraseña
    longitud_restante = longitud - len(caracteres_requeridos)
    if longitud_restante > 0:
        caracteres_aleatorios = [random.choice(todos_caracteres) for _ in range(longitud_restante)]
    else:
        caracteres_aleatorios = []

    # Combinar y mezclar todos los caracteres
    todos_los_caracteres = caracteres_requeridos + caracteres_aleatorios
    random.shuffle(todos_los_caracteres)

    # Convertir la lista de caracteres a una cadena
    contrasena = ''.join(todos_los_caracteres)
    return contrasena

# Generar diferentes tipos de contraseñas
contrasena_segura = generar_contrasena(15)
contrasena_sin_simbolos = generar_contrasena(10, incluir_simbolos=False)
contrasena_solo_letras = generar_contrasena(8, incluir_numeros=False, incluir_simbolos=False)

print(f"Contraseña segura: {contrasena_segura}")
print(f"Contraseña sin símbolos: {contrasena_sin_simbolos}")
print(f"Contraseña solo con letras: {contrasena_solo_letras}")
