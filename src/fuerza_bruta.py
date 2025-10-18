'''
Ejemplo de ataque de fuerza bruta para encontrar una contraseña simple.
'''
import itertools
import time

def verificar_contrasenia(intento, contrasenia_real):
    return intento == contrasenia_real

def fuerza_bruta(caracteres, longitud, contrasenia_real):
    inicio = time.time()
    intentos = 0

    for combinacion in itertools.product(caracteres, repeat=longitud):
        intentos += 1
        contrasenia = ''.join(combinacion)

        if verificar_contrasenia(contrasenia, contrasenia_real):
            fin = time.time()
            return {
                'contraseña': contrasenia,
                'intentos': intentos,
                'tiempo': fin - inicio
            }

    return None

# Ejemplo de uso
CARACTERES = 'abcdefghijklmnopqrstuvwxyz'
CONTRASENIA_REAL = 'xmx'

resultado = fuerza_bruta(CARACTERES, len(CONTRASENIA_REAL), CONTRASENIA_REAL)
print(f"Contraseña encontrada: {resultado['contraseña']}")
print(f"Intentos realizados: {resultado['intentos']}")
print(f"Tiempo empleado: {resultado['tiempo']:.4f} segundos")
