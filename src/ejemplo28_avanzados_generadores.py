'''
Implementa un generador llamado fibonacci_generator que produzca los primeros n números de la secuencia de Fibonacci. 
La secuencia de Fibonacci comienza con 0 y 1, y cada número siguiente es la suma de los dos anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). 
La función debe aceptar un parámetro n que indique cuántos números de la secuencia debe generar. 
Si n es menor o igual a 0, el generador no debe producir ningún valor.
Por ejemplo, si llamamos a fibonacci_generator(6), debería generar los valores: 0, 1, 1, 2, 3, 5.

'''

def fibonacci_generator(n):
    '''Generador que produce los primeros n números de la secuencia de Fibonacci.'''
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Ejemplo de uso:
N = 10

fib_gen = fibonacci_generator(N)
for num in fib_gen:
    print(num)
