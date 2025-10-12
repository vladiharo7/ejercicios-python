'''
Crea una función llamada extraer_info que reciba como parámetro una cadena de 
texto representando un correo electrónico con el formato nombre@dominio.extension. 
La función debe devolver un diccionario con tres claves:

nombre_usuario: la parte del correo antes del símbolo @
dominio: la parte entre @ y el último punto
extension: la parte después del último punto
Por ejemplo, si la entrada es "usuario@ejemplo.com", la función debe devolver:

{
    "nombre_usuario": "usuario",
    "dominio": "ejemplo",
    "extension": "com"
}
Si la cadena no contiene el símbolo @ o no tiene extensión (un punto después del @), la función debe devolver un diccionario vacío.

Utiliza los métodos de cadenas y técnicas de slicing que has aprendido para resolver este ejercicio.
'''

def extraer_info(correo):
    """
    Extrae la información de un correo electrónico en un diccionario.

    Parameters:
        correo (str): Cadena de texto representando un correo electrónico.

    Returns:
        dict: Diccionario con las claves 'nombre_usuario', 'dominio' y 'extension'.
              Si el formato es incorrecto, devuelve un diccionario vacío.
    """
    # Verificar si el correo contiene '@'
    if '@' not in correo:
        return {}

    # Dividir el correo en nombre de usuario y resto
    nombre_usuario, resto = correo.split('@', 1)

    # Verificar si el resto contiene un punto para la extensión
    if '.' not in resto:
        return {}

    # Dividir el resto en dominio y extensión
    dominio, extension = resto.rsplit('.', 1)

    # Construir el diccionario con la información extraída
    info = {
        "nombre_usuario": nombre_usuario,
        "dominio": dominio,
        "extension": extension
    }

    return info

# Ejemplos de uso
print(extraer_info(""))  # Debería devolver {}
print(extraer_info("email_sin_arroba.com"))  # Debería devolver {}
print(extraer_info("usuario@dominio_sin_extension"))  # Debería devolver {}
print(extraer_info("email_sin_uso@dominio.com"))  # Debería devolver {'nombre_usuario': 'email_sin_uso', 'dominio': 'dominio', 'extension': 'com'}
