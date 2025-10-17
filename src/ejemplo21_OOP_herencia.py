'''
Crea una jerarquía de clases para modelar vehículos. Debes implementar:

Una clase base Vehiculo con los siguientes atributos y métodos:
Atributos: marca, modelo y año
Un método mostrar_info() que devuelva un string con la información básica del vehículo
Una clase derivada Automovil que herede de Vehiculo y añada:
Un atributo adicional puertas (número de puertas)
Sobrescribe el método mostrar_info() para incluir el número de puertas
Una clase derivada Motocicleta que herede de Vehiculo y añada:
Un atributo adicional cilindrada (en cc)
Sobrescribe el método mostrar_info() para incluir la cilindrada
Finalmente, crea una instancia de cada clase derivada y muestra su información usando el método mostrar_info().
'''
class Vehiculo:
    ''' Clase base Vehiculo '''
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        ''' Muestra la información básica del vehículo '''
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"

class Automovil(Vehiculo):
    ''' Clase Automovil que hereda de Vehiculo '''
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Puertas: {self.puertas}"

class Motocicleta(Vehiculo):
    ''' Clase Motocicleta que hereda de Vehiculo '''
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Cilindrada: {self.cilindrada}cc"

# Crear instancias y mostrar información
auto = Automovil("Toyota", "Corolla", 2020, 4)
moto = Motocicleta("Honda", "CBR500R", 2019, 500)
print(auto.mostrar_info())
print(moto.mostrar_info())
# Salida esperada:
# Marca: Toyota, Modelo: Corolla, Año: 2020, Puertas: 4
# Marca: Honda, Modelo: CBR500R, Año: 2019, Cilindrada: 500cc
