'''
Crea una función llamada suma_pares que reciba dos parámetros: inicio y fin.
La función debe calcular y devolver la suma de todos los números pares que se 
encuentran en el rango desde inicio hasta fin (ambos inclusive).

Por ejemplo:

Si llamamos suma_pares(1, 10) debe devolver 30 (2+4+6+8+10)
Si llamamos suma_pares(5, 15) debe devolver 50 (6+8+10+12+14)
Utiliza un bucle for con la función range() para iterar sobre el 
rango de números y suma solo aquellos que sean pares (pista: puedes usar 
el operador módulo % para verificar si un número es par).
'''

def suma_pares(inicio, fin):
    '''
    Calcula la suma de todos los números pares en el rango desde inicio hasta fin (ambos inclusive).
    '''
    suma = 0
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            suma += numero
    return suma

# Ejemplos de uso
print(suma_pares(1, 10))  # Debería devolver 30
print(suma_pares(5, 15))  # Debería devolver 50
print(suma_pares(0, 20))  # Debería devolver 110
