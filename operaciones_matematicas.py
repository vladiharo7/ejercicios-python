'''
Crea un módulo llamado operaciones_matematicas.py que contenga las siguientes funciones:

sumar(a, b): Devuelve la suma de dos números
restar(a, b): Devuelve la resta de dos números
multiplicar(a, b): Devuelve el producto de dos números
dividir(a, b): Devuelve la división de a entre b (debe manejar la división por cero devolviendo un mensaje de error)
Además, define una constante PI con el valor 3.14159.
'''
PI = 3.14159
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# Ejemplo de uso
if __name__ == "__main__":
    print("Suma de 10 y 5:", sumar(10, 5))
    print("Resta de 10 y 5:", restar(10, 5))
    print("Multiplicación de 10 y 5:", multiplicar(10, 5))
    print("División de 10 entre 0:", dividir(10, 0))
    print("División de 10 entre 2:", dividir(10, 2))
    print("Valor de PI:", PI)
