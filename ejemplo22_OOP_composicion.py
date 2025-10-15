'''
Implementa un sistema básico de biblioteca utilizando composición. 
Crea una clase Libro con atributos para título, autor y año de publicación. 
Luego, crea una clase Biblioteca que contenga una colección de libros (relación "tiene un"). 
La clase Biblioteca debe incluir métodos para:

Agregar un nuevo libro a la colección
Buscar libros por título (devolviendo todos los que contengan la cadena de búsqueda)
Contar cuántos libros hay de un autor específico
No utilices herencia para resolver este ejercicio, solo composición. 
Asegúrate de que la clase Biblioteca delegue apropiadamente en los objetos Libro que contiene.
'''

class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def __str__(self):
        return f'"{self.titulo}" por {self.autor} ({self.anio_publicacion})'

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_por_titulo(self, cadena_busqueda):
        resultados = [libro for libro in self.libros if cadena_busqueda.lower() in libro.titulo.lower()]
        return resultados

    def contar_por_autor(self, autor):
        contador = sum(1 for libro in self.libros if libro.autor.lower() == autor.lower())
        return contador

# Ejemplo de uso
if __name__ == "__main__":

    biblioteca = Biblioteca()

    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)
    libro3 = Libro("La casa de los espíritus", "Isabel Allende", 1982)
    libro4 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985)

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)
    biblioteca.agregar_libro(libro4)

    print("Libros que contienen 'de':")
    for libro in biblioteca.buscar_por_titulo("de"):
        print(libro)

    autor_a_buscar = "Gabriel García Márquez"
    print(f"\nNúmero de libros de {autor_a_buscar}: {biblioteca.contar_por_autor(autor_a_buscar)}")

# Salida esperada:
# Libros que contienen 'de':
# "Cien años de soledad" por Gabriel García Márquez (1967)
# "Don Quijote de la Mancha" por Miguel de Cervantes (1605)
# "La casa de los espíritus" por Isabel Allende (1982)
# "El amor en los tiempos del cólera" por Gabriel García Márquez (1985)
#
# Número de libros de Gabriel García Márquez: 2
