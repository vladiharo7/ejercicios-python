'''
Crea un diccionario llamado contactos que contenga la información de tres personas.
Para cada persona, almacena su nombre, teléfono y correo electrónico.
Luego, realiza las siguientes operaciones:

Muestra el correo electrónico de la segunda persona que añadiste al diccionario.
Añade un nuevo contacto con la información que prefieras.
Modifica el número de teléfono de la primera persona que añadiste.
Utiliza un bucle para mostrar los nombres de todos los contactos.
Puedes empezar con algo como:
'''

# Crear el diccionario de contactos
contactos = {
    "persona1": {"nombre": "Ana", "telefono": "123456789", "email": "ana@ejemplo.com"},
    "persona2": {"nombre": "Luis", "telefono": "987654321", "email": "luis@ejemplo.com"},
    "persona3": {"nombre": "Marta", "telefono": "555555555", "email": "marta@ejemplo.com"}
}

# Mostrar el correo electrónico de la segunda persona
print("Correo electrónico de la segunda persona:", contactos["persona2"]["email"])

# Añadir un nuevo contacto utilizando update
contactos.update({"persona4": {"nombre": "Carlos", "telefono": "444444444", "email": "carlos@ejemplo.com"}})

# Modificar el número de teléfono de la primera persona
contactos["persona1"]["telefono"] = "111111111"

# Mostrar los nombres de todos los contactos
print("Nombres de todos los contactos:")
for persona in contactos.values():
    print(persona["nombre"])
