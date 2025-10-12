'''
Crea una tupla llamada contacto que contenga la siguiente información en 
este orden: nombre, correo electrónico y número de teléfono.
 Utiliza los valores "Ana García", "ana@ejemplo.com" y "555-1234".

Luego, realiza las siguientes operaciones:

Desempaqueta la tupla en tres variables llamadas nombre, email y telefono.
Imprime cada variable en líneas separadas.
Crea una nueva tupla llamada contacto_completo que contenga los elementos 
de la tupla original más la ciudad "Madrid" al final.
Recuerda que las tuplas son inmutables, por lo que deberás 
crear una nueva tupla para añadir el elemento adicional.
'''

# Crear la tupla contacto
contacto = ("Ana García", "ana@ejemplo.com", "555-1234")

# Desempaquetar la tupla en variables
nombre, email, telefono = contacto

# Imprimir cada variable en líneas separadas
print(nombre)
print(email)
print(telefono)

# Crear una nueva tupla contacto_completo con la ciudad añadida
contacto_completo = contacto + ("Madrid",)

print(contacto_completo)
