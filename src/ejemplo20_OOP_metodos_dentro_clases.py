'''
Crea una clase llamada Contador que gestione un valor numérico. La clase debe implementar:

Un atributo de clase contadores_creados que lleve la cuenta de cuántas instancias se han creado.

Un método de instancia incrementar() que aumente el valor del contador en 1 y devuelva el nuevo valor.

Un método de instancia decrementar() que disminuya el valor del contador en 1 y devuelva el nuevo valor. El contador nunca debe ser negativo.

Un método de clase @classmethod llamado reiniciar_contador_global() que ponga a cero el contador de instancias creadas.

Un método estático @staticmethod llamado es_par(numero) que devuelva True si el número proporcionado es par, o False en caso contrario.

Puedes empezar con este esquema:

class Contador:
    # Atributo de clase para contar instancias
    contadores_creados = 0
    
    def __init__(self, valor_inicial=0):
        # Completa el constructor
        pass
        
    # Implementa los métodos requeridos
'''

class Contador:
    '''Clase que gestiona un valor numérico con métodos de instancia, clase y estáticos.'''
    contadores_creados = 0

    def __init__(self, valor_inicial=0):
        self.valor = max(0, valor_inicial)  # Asegura que el valor inicial no sea negativo
        Contador.contadores_creados += 1

    def incrementar(self):
        '''Incrementa el valor del contador en 1 y devuelve el nuevo valor.'''
        self.valor += 1
        return self.valor

    def decrementar(self):
        '''
        Disminuye el valor del contador en 1 y devuelve el nuevo valor. El contador nunca es negativo.
        '''
        if self.valor > 0:
            self.valor -= 1
        return self.valor

    @classmethod
    def reiniciar_contador_global(cls):
        '''Reinicia el contador de instancias creadas a cero.'''
        cls.contadores_creados = 0

    @staticmethod
    def es_par(numero):
        '''Devuelve True si el número es par, False en caso contrario.'''
        return numero % 2 == 0


# Ejemplo de uso
contador1 = Contador(5)
contador2 = Contador(10)
print(contador1.incrementar())  # Salida: 6
print(contador1.decrementar())  # Salida: 5
print(contador1.decrementar())  # Salida: 4
print(contador1.decrementar())  # Salida: 3
print(contador1.decrementar())  # Salida: 2
print(contador1.decrementar())  # Salida: 1
print(contador1.decrementar())  # Salida: 0
print(contador1.decrementar())  # Salida: 0 (no puede ser negativo)
print(Contador.contadores_creados)  # Salida: 2
Contador.reiniciar_contador_global()
print(Contador.contadores_creados)  # Salida: 0
print(Contador.es_par(4))  # Salida: True
print(Contador.es_par(7))  # Salida: False
