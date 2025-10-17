''' 
    write the fibonacci function here with cache to optimize performance in a dictionary
'''

import random

# Caché para la secuencia de Fibonacci
cache_fibonacci = {}

def fibonacci(n) -> int:

    """
    Devuelve el n-ésimo número de la secuencia de Fibonacci usando recursión con memoización.

    Parameters:
        n (int): Índice del número de Fibonacci a calcular.

    Returns:
        int: Valor correspondiente en la secuencia de Fibonacci.

    This function uses a cache (memoization) to avoid redundant calculations,
    making it efficient even for large values of n.
    """


    # Si ya calculamos este valor, lo devolvemos directamente
    if n in cache_fibonacci:
        return cache_fibonacci[n]

    # Calculamos el valor para n
    if n <= 1:
        resultado = n
    else:
        resultado = fibonacci(n-1) + fibonacci(n-2)

    # Guardamos en caché antes de devolver
    cache_fibonacci[n] = resultado
    return resultado

# Ahora las llamadas repetidas son instantáneas
print(fibonacci(30))  # Rápido incluso para valores grandes
print(fibonacci(35))  # Rápido incluso para valores grandes
print(fibonacci(40))  # Rápido incluso para valores grandes
print(fibonacci(50))  # Rápido incluso para valores grandes
print(fibonacci(100)) # Rápido incluso para valores grandes
print(fibonacci(100)) # Rápido incluso para valores grandes
print(fibonacci(100)) # Rápido incluso para valores grandes
print(fibonacci(100)) # Rápido incluso para valores grandes
print(fibonacci(100)) # Rápido incluso para valores grandes
print(fibonacci(100)) # Rápido incluso para valores grandes


# Generamos 10,000 números aleatorios entre 0 y 1000 (puede haber repetidos)
numeros_random = [random.randint(0, 1000) for _ in range(10000)]

# Calculamos la serie de Fibonacci para cada número
resultados = []
for numero in numeros_random:
    resultados.append(fibonacci(numero))

# Ejemplo: mostrar los primeros 10 resultados
for i in range(1000):
    print(f"Fibonacci({numeros_random[i]}) = {resultados[i]}")
