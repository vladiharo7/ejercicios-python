from functools import reduce
# Estructura de árbol simple (diccionario anidado)
arbol = {
    "valor": 1,
    "hijos": [
        {
            "valor": 2,
            "hijos": [
                {"valor": 4, "hijos": []},
                {"valor": 5, "hijos": []}
            ]
        },
        {
            "valor": 3,
            "hijos": [
                {"valor": 6, "hijos": []}
            ]
        }
    ]
}


def suma_arbol(nodo):
    '''Función para sumar todos los valores del árbol'''
    # Suma el valor del nodo actual
    valor_actual = nodo["valor"]

    # Si no hay hijos, devuelve solo el valor actual
    if not nodo["hijos"]:
        return valor_actual

    # Suma el valor actual con la suma de todos los hijos
    return valor_actual + reduce(
        lambda acum, hijo: acum + suma_arbol(hijo),
        nodo["hijos"],
        0
    )

print(f"Suma de todos los valores del árbol: {suma_arbol(arbol)}")  # 21

print("\n---\n")

'''Ejemplo adicional: Construcción de una consulta SQL WHERE usando reduce con múltiples condiciones'''

# Construir una consulta SQL WHERE con múltiples condiciones
condiciones = [
    ("nombre", "LIKE", "%Juan%"),
    ("edad", ">", 25),
    ("ciudad", "=", "Madrid"),
    ("activo", "=", True)
]

# Función para formatear una condición
def formatear_condicion(campo, operador, valor):
    if isinstance(valor, str):
        return f"{campo} {operador} '{valor}'"
    else:
        return f"{campo} {operador} {valor}"

# Construir la cláusula WHERE completa
where_clausula = reduce(
    lambda acum, cond: f"{acum} AND {formatear_condicion(*cond)}" if acum else formatear_condicion(*cond),
    condiciones,
    ""
)

# Construir la consulta completa
consulta = f"SELECT * FROM usuarios WHERE {where_clausula}"
print(consulta)
# SELECT * FROM usuarios WHERE nombre LIKE '%Juan%' AND edad > 25 AND ciudad = 'Madrid' AND activo = True

print("\n---\n")
import re

# Texto de ejemplo
texto = """
Python es un lenguaje de programación interpretado cuya filosofía hace 
hincapié en la legibilidad de su código. Se trata de un lenguaje de programación 
multiparadigma, ya que soporta orientación a objetos, programación imperativa y, 
en menor medida, programación funcional. Es un lenguaje interpretado, dinámico 
y multiplataforma.
"""

# Limpiar y dividir el texto en palabras
palabras = re.findall(r'\b\w+\b', texto.lower())

# Contar frecuencia de cada palabra
frecuencia_palabras = reduce(
    lambda acum, palabra: {
        **acum,
        palabra: acum.get(palabra, 0) + 1
    },
    palabras,
    {}
)

# Encontrar las 5 palabras más frecuentes
palabras_ordenadas = sorted(
    frecuencia_palabras.items(),
    key=lambda x: x[1],
    reverse=True
)[:5]

print("Las 5 palabras más frecuentes:")
for palabra, frecuencia in palabras_ordenadas:
    print(f"- '{palabra}': {frecuencia} veces")

