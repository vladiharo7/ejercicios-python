import sys

def calculadora():
    '''
    Una calculadora simple que realiza operaciones básicas (suma, resta, multiplicación, división)
    entre dos números proporcionados como argumentos de línea de comandos.
    '''
    if len(sys.argv) != 4:
        print("Uso: python calculadora.py <número1> <operación> <número2>")
        print("Operaciones disponibles: suma, resta, mult, div")
        sys.exit(1)  # Salir con código de error

    try:
        num1 = float(sys.argv[1])
        operacion = sys.argv[2]
        num2 = float(sys.argv[3])

        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "mult":
            resultado = num1 * num2
        elif operacion == "div":
            if num2 == 0:
                print("Error: División por cero")
                sys.exit(1)
            resultado = num1 / num2
        else:
            print(f"Operación '{operacion}' no reconocida")
            sys.exit(1)

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Error: Los argumentos deben ser números válidos")
        sys.exit(1)

if __name__ == "__main__":
    calculadora()


# Ejemplo de uso:# python calculadora_simple.py 10 suma 5
# Resultado: 15.0
