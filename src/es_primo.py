'''
Función para verificar si un número es primo.'''

def es_primo(n):
    """Verifica si un número es primo."""
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

# Filtrar números primos de una lista
numeros = range(1, 20)
primos = list(filter(es_primo, numeros))
print(primos)  # [2, 3, 5, 7, 11, 13, 17, 19]
