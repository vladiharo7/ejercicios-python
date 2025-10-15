'''
Crea un módulo llamado operaciones_matematicas.py que contenga las siguientes funciones:

sumar(a, b): Devuelve la suma de dos números
restar(a, b): Devuelve la resta de dos números
multiplicar(a, b): Devuelve el producto de dos números
dividir(a, b): Devuelve la división de a entre b (debe manejar la división por cero devolviendo un mensaje de error)
Además, define una constante PI con el valor 3.14159.

Luego, crea un archivo principal llamado calculadora.py que importe el módulo que has creado y realice las siguientes operaciones:

Importa todas las funciones y la constante PI del módulo
Calcula y muestra el resultado de sumar 15 y 7
Calcula y muestra el resultado de multiplicar 3.5 por 2
Calcula y muestra el área de un círculo con radio 5 utilizando la constante PI
Puedes empezar creando primero el archivo operaciones_matematicas.py con las funciones solicitadas, 
y luego el archivo calculadora.py que importa y usa esas funciones.
'''

from operaciones_matematicas import sumar, restar, multiplicar, dividir, PI
import math

# Realiza las operaciones solicitadas
print("Suma de 15 y 7:", sumar(15, 7))
print("Multiplicación de 3.5 por 2:", multiplicar(3.5, 2))
radio = 5
area_circulo = PI * multiplicar(radio, radio)
print("Área de un círculo con radio 5:", area_circulo)
# Alternativamente, usando math.pi para mayor precisión
area_circulo_preciso = math.pi * multiplicar(radio, radio)
print("Área de un círculo con radio 5 (usando math.pi):", area_circulo_preciso)
# Ejemplo de uso de las demás funciones
print("Resta de 20 y 8:", restar(20, 8))
print("División de 20 entre 4:", dividir(20, 4))
print("División de 20 entre 0:", dividir(20, 0))
# Fin del archivo calculadora.py
