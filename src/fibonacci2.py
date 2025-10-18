def fibonacci():
    '''Generador infinito de números de Fibonacci.'''
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Obtener los primeros 10 números de Fibonacci
fib_gen = fibonacci()
primeros_diez = [next(fib_gen) for _ in range(10)]
print(primeros_diez)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
