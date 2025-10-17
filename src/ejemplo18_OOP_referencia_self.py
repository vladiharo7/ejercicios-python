'''
Crea una clase llamada Libro con los siguientes requisitos:

El constructor debe inicializar tres atributos de instancia: 
titulo, autor y paginas.

Implementa un método llamado describir que devuelva un string 
con el formato: "[Titulo] escrito por [Autor] - [Paginas] páginas".

Implementa un método llamado es_largo que devuelva 
True si el libro tiene más de 300 páginas, y False en caso contrario.

Implementa un método llamado resumir que reciba un 
parámetro longitud y devuelva un string con el 
formato: "[Titulo] - Resumen de [longitud] caracteres". 
Si no se proporciona el parámetro longitud, 
debe usar un valor predeterminado de 50.

Prueba tu clase creando al menos dos instancias 
diferentes de Libro y llamando a todos sus métodos.
'''
class Libro:
    '''
    Clase que representa un libro con título, autor y número de páginas.
    '''

    __slots__ = ['titulo', 'autor', 'paginas']

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def describir(self):
        '''
        Método que devuelve una descripción del libro.
        '''
        return f'"{self.titulo}" escrito por {self.autor} - {self.paginas} páginas.'

    def es_largo(self):
        '''
        Método que determina si el libro es largo (más de 300 páginas).
        '''
        return self.paginas > 300

    def resumir(self, longitud=50):
        '''
        Método que devuelve un resumen del libro con una longitud específica.
        '''
        return f'"{self.titulo}" - Resumen de {longitud} caracteres.'
    
# Crear instancias de la clase Libro
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 417)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)

# Llamar a los métodos de la clase Libro
print(libro1.describir())  # Salida: "Cien Años de Soledad" escrito por Gabriel García Márquez - 417 páginas.
print(libro1.es_largo())   # Salida: True
print(libro1.resumir())    # Salida: "Cien Años de Soledad" - Resumen de 50 caracteres.
print(libro1.resumir(100)) # Salida: "Cien Años de Soledad" - Resumen de 100 caracteres.

print(libro2.describir())  # Salida: "El Principito" escrito por Antoine de Saint-Exupéry - 96 páginas.
print(libro2.es_largo())   # Salida: False
print(libro2.resumir())    # Salida: "El Principito" - Resumen de 50 caracteres.
print(libro2.resumir(30))  # Salida: "El Principito" - Resumen de 30 caracteres.
