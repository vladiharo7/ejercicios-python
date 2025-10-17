'''
Crea una calculadora básica que realice las cuatro operaciones aritméticas 
fundamentales (suma, resta, multiplicación y división) entre dos números.

Debes solicitar al usuario que introduzca dos números y luego mostrar 
el resultado de las cuatro operaciones con estos números.

Para cada operación, muestra el resultado con el siguiente formato:

"La suma de X y Y es: Z"
"La resta de X y Y es: Z"
"La multiplicación de X y Y es: Z"
"La división de X y Y es: Z"
Recuerda manejar el caso especial de división por cero mostrando un mensaje apropiado.

Pista: Utiliza los operadores +, -, *, / y controla la división por cero con una estructura condicional.
'''

# Solicitar al usuario que introduzca dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Realizar las operaciones aritméticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = None
if num2 != 0:
    division = num1 / num2
else:
    division = "Indefinida (no se puede dividir por cero)"

# Mostrar los resultados con el formato especificado
print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
print(f"La división de {num1} y {num2} es: {division}")
