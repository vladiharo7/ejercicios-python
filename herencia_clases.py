'''
'''

class Empleado:
    '''Clase base para empleados'''
    def __init__(self, nombre, id_empleado):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.activo = True
    
    def registrar_entrada(self):
        return f"{self.nombre} ha registrado su entrada"
    
    def registrar_salida(self):
        return f"{self.nombre} ha registrado su salida"
    
    def obtener_datos(self):
        return f"Empleado: {self.nombre}, ID: {self.id_empleado}"

class Desarrollador(Empleado):
    '''Clase derivada para desarrolladores'''
    def __init__(self, nombre, id_empleado, lenguajes):
        # Inicializamos la clase base
        super().__init__(nombre, id_empleado)
        # Añadimos atributos específicos
        self.lenguajes = lenguajes
        self.proyectos = []
    
    def asignar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
        return f"{self.nombre} asignado al proyecto {proyecto}"
    
    def obtener_datos(self):
        datos_base = super().obtener_datos()
        return f"{datos_base}, Lenguajes: {', '.join(self.lenguajes)}"

class GerenteProyecto(Empleado):
    def __init__(self, nombre, id_empleado):
        super().__init__(nombre, id_empleado)
        self.equipo = []
    
    def añadir_miembro(self, empleado):
        self.equipo.append(empleado)
        return f"{empleado.nombre} añadido al equipo de {self.nombre}"
    
    def listar_equipo(self):
        return [miembro.nombre for miembro in self.equipo]


# Creamos instancias
dev1 = Desarrollador("Ana García", "DEV001", ["Python", "JavaScript"])
dev2 = Desarrollador("Carlos López", "DEV002", ["Java", "C#"])
gerente = GerenteProyecto("Laura Martínez", "PM001")

# Usamos métodos heredados
print(dev1.registrar_entrada())  # Ana García ha registrado su entrada

# Usamos métodos específicos
print(dev1.asignar_proyecto("Sistema de Inventario"))
print(gerente.añadir_miembro(dev1))
print(gerente.añadir_miembro(dev2))

# Usamos métodos sobrescritos
print(dev1.obtener_datos())  # Empleado: Ana García, ID: DEV001, Lenguajes: Python, JavaScript

# Verificamos el equipo del gerente
print(gerente.listar_equipo())  # ['Ana García', 'Carlos López']


'''
A menudo queremos mantener el comportamiento del método de la clase base y 
añadir funcionalidad adicional. Para esto usamos super():
'''

class Estudiante:
    '''Clase base para estudiantes'''
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.conocimientos = []

    def estudiar(self, tema):
        '''Método para estudiar un tema'''
        self.conocimientos.append(tema)
        return f"{self.nombre} está estudiando {tema}"

class EstudianteGraduado(Estudiante):
    '''Clase derivada para estudiantes graduados'''
    def __init__(self, nombre, edad, titulo):
        '''Inicializamos la clase base y añadimos un nuevo atributo'''
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
        self.titulo = titulo  # Añadimos un nuevo atributo

    def estudiar(self, tema):
        # Extendemos el método estudiar
        mensaje_base = super().estudiar(tema)  # Llamamos al método de la clase base
        return f"{mensaje_base} a nivel avanzado para su investigación de {self.titulo}"

graduado = EstudianteGraduado("María", 24, "Inteligencia Artificial")
print(graduado.estudiar("Redes Neuronales"))
# María está estudiando Redes Neuronales a nivel avanzado para su investigación de Inteligencia Artificial

'''
La función super() es una herramienta fundamental para trabajar con herencia en Python. 
Permite acceder a métodos y propiedades de la clase base desde la clase derivada.
'''
class Dispositivo:
    '''Clase base para dispositivos'''
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
    
    def encender(self):
        '''Método para encender el dispositivo'''
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido"
        return f"{self.marca} {self.modelo} ya estaba encendido"

class Smartphone(Dispositivo):
    '''Clase derivada para smartphones'''
    def __init__(self, marca, modelo, sistema_operativo):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.sistema_operativo = sistema_operativo
        self.apps_abiertas = []

    def encender(self):
        '''Extendemos el método encender'''
        resultado_base = super().encender()  # Llamada al método de la clase base
        if self.encendido:  # Solo si realmente se encendió
            return f"{resultado_base}. Iniciando {self.sistema_operativo}..."
        return resultado_base

telefono = Smartphone("Apple", "iPhone 14", "iOS")
print(telefono.encender())  # Apple iPhone 14 encendido. Iniciando iOS...
print(telefono.encender())  # Apple iPhone 14 ya estaba encendido

# Verificar si una clase hereda de otra
print(issubclass(Smartphone, Dispositivo))  # True

# Verificar si un objeto es instancia de una clase
mi_telefono = Smartphone("Samsung", "Galaxy S21", "Android")
print(f"Instance of Smartphone: {isinstance(mi_telefono, Smartphone)}")  # True
print(f"Instance of Dispositivo: {isinstance(mi_telefono, Dispositivo)}")  # True


'''
Existen tres patrones comunes para manejar constructores en herencia:
Reemplazar completamente: No llamar a super().__init__() y definir todo desde cero (no recomendado).
Extender: Llamar a super().__init__() y añadir nuevos atributos.
Modificar parámetros: Procesar parámetros antes de pasarlos a super().__init__().
'''
class Producto:
    '''Clase base para productos'''
    def __init__(self, nombre, precio, codigo):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
        self.en_stock = True

class ProductoDigital(Producto):
    '''Clase derivada para productos digitales'''
    def __init__(self, nombre, precio, codigo, formato, tamaño_mb):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, precio, codigo)
        # Añadimos atributos específicos
        self.formato = formato
        self.tamaño_mb = tamaño_mb
        self.descargado = False

    def descargar(self):
        '''Método para descargar el producto digital'''
        self.descargado = True
        return f"Descargando {self.nombre} ({self.tamaño_mb}MB) en formato {self.formato}"

class ProductoConDescuento(Producto):
    '''Clase derivada para productos con descuento'''
    def __init__(self, nombre, precio, codigo, porcentaje_descuento):
        # Calculamos el precio con descuento
        precio_final = precio * (1 - porcentaje_descuento / 100)
        # Pasamos el precio modificado al constructor base
        super().__init__(nombre, precio_final, codigo)
        # Guardamos información adicional
        self.precio_original = precio
        self.porcentaje_descuento = porcentaje_descuento


# Creamos instancias
producto_fisico = Producto("Camiseta", 20.0, "C001")
producto_digital = ProductoDigital("E-book Python", 15.0, "D001", "PDF", 5)
producto_descuento = ProductoConDescuento("Auriculares", 50.0, "C002", 10)

# Usamos métodos y atributos
# Descargando E-book Python (5MB) en formato PDF
print(producto_digital.descargar())

 # Precio original: 50.0, Precio con descuento: 45.0
print(f"Precio original: {producto_descuento.precio_original}, Precio con descuento: {producto_descuento.precio}")
# Camiseta, 20.0, C001
print(f"{producto_fisico.nombre}, {producto_fisico.precio}, {producto_fisico.codigo}")
# E-book Python, 15.0, D001, PDF, 5
print(f"{producto_digital.nombre}, {producto_digital.precio}, {producto_digital.codigo}, {producto_digital.formato}, {producto_digital.tamaño_mb}")
# Auriculares, 45.0, C002, 10
print(f"{producto_descuento.nombre}, {producto_descuento.precio}, {producto_descuento.codigo}, {producto_descuento.porcentaje_descuento}")
