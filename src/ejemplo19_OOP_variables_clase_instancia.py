'''
Crea una clase llamada Biblioteca que gestione libros utilizando variables 
de clase e instancia adecuadamente.

La clase debe tener:

Una variable de clase total_libros inicializada en 0 que lleve
la cuenta de todos los libros en el sistema.
Una variable de clase nombre_biblioteca con el valor "Biblioteca Central".
En el método __init__, recibe el parámetro nombre_seccion 
(por ejemplo "Ficción", "Historia", etc.) y crea una variable 
de instancia para almacenarlo.
En el método __init__, inicializa una variable de instancia 
libros como una lista vacía para almacenar los libros de esa sección.
Un método agregar_libro(self, titulo) que añada el título a 
la lista de libros de la sección e incremente la variable 
de clase total_libros.
Un método obtener_informe(self) que devuelva un string con 
el formato: "Sección [nombre_seccion] de [nombre_biblioteca]: [cantidad] libros".
Finalmente, crea dos instancias de la clase con diferentes 
secciones, agrega algunos libros a cada una y muestra sus 
informes para verificar que la variable de clase se comparte correctamente.
'''
class Biblioteca:
    '''Clase que gestiona libros en una biblioteca con variables de clase e instancia.'''
    total_libros = 0
    nombre_biblioteca = "Biblioteca Central"

    def __init__(self, nombre_seccion):
        self.nombre_seccion = nombre_seccion
        self.libros = []

    def agregar_libro(self, titulo):
        '''Agrega un libro a la sección y actualiza el total de libros.'''
        self.libros.append(titulo)
        Biblioteca.total_libros += 1

    def obtener_informe(self):
        '''Devuelve un informe de la sección y la cantidad de libros.'''
        cantidad = len(self.libros)
        return f"Sección {self.nombre_seccion} de {Biblioteca.nombre_biblioteca}: {cantidad} libros"

# Crear instancias de la clase Biblioteca
seccion_ficcion = Biblioteca("Ficción")
seccion_historia = Biblioteca("Historia")
# Agregar libros a la sección de Ficción
seccion_ficcion.agregar_libro("Cien Años de Soledad")
seccion_ficcion.agregar_libro("Don Quijote de la Mancha")
# Agregar libros a la sección de Historia
seccion_historia.agregar_libro("Sapiens: De Animales a Dioses")
seccion_historia.agregar_libro("Guns, Germs, and Steel")
seccion_historia.agregar_libro("The Silk Roads")
# Mostrar informes de ambas secciones
print(seccion_ficcion.obtener_informe())
print(seccion_historia.obtener_informe())
# Mostrar el total de libros en la biblioteca
print(f"Total de libros en la biblioteca: {Biblioteca.total_libros}")
# Salida esperada:
# Sección Ficción de Biblioteca Central: 2 libros
# Sección Historia de Biblioteca Central: 3 libros
# Total de libros en la biblioteca: 5
