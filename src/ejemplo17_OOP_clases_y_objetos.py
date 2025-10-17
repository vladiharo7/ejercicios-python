'''
Crea una clase llamada Persona con los siguientes elementos:

Un constructor __init__ que reciba como parámetros nombre y 
edad y los almacene como atributos de instancia.

Un método llamado presentarse que devuelva un string 
con el formato: "Hola, me llamo {nombre} y tengo {edad} años".

Luego, crea una instancia de la clase Persona con tu 
nombre y edad, y llama al método presentarse 
para verificar que funciona correctamente.
'''
class Persona:
    '''
    Clase que representa a una persona con nombre y edad.
    '''

    __slots__ = ['nombre', 'edad']

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        '''
        Método que devuelve una presentación de la persona.
        '''
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

# Crear una instancia de la clase Persona
persona = Persona("Lionel Messi", 38)
# Llamar al método presentarse
print(persona.presentarse())
# Salida esperada: "Hola, me llamo Juan y tengo 30 años."
