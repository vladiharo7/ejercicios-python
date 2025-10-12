'''
Generador de datos aleatorios para pruebas
'''

import random
import datetime

def generar_usuario_aleatorio():
    """Genera datos de usuario aleatorios para pruebas."""
    nombres = ["Ana", "Carlos", "Elena", "David", "Laura", "Miguel", "Sofía", "Pablo"]
    apellidos = ["García", "Rodríguez", "López", "Martínez", "González", "Pérez", "Sánchez"]
    dominios = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "empresa.es"]

    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    edad = random.randint(18, 80)

    # Generar email
    email = f"{nombre.lower()}.{apellido.lower()}@{random.choice(dominios)}"

    # Generar fecha de registro (en los últimos 5 años)
    dias_atras = random.randint(1, 365 * 5)
    fecha_registro = datetime.datetime.now() - datetime.timedelta(days=dias_atras)

    return {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "edad": edad,
        "fecha_registro": fecha_registro.strftime("%Y-%m-%d")
    }

# Generar 5 usuarios aleatorios
usuarios = [generar_usuario_aleatorio() for _ in range(5)]
for i, usuario in enumerate(usuarios, 1):
    print(f"Usuario {i}:")
    for clave, valor in usuario.items():
        print(f"  {clave}: {valor}")
    print()
