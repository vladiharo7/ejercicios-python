'''
Al sobrescribir métodos, es importante tener en cuenta algunas consideraciones:

Firma del método: Idealmente, el método sobrescrito debería mantener la misma firma (parámetros) 
que el método original para evitar confusiones.

Principio de sustitución de Liskov: Una instancia de una clase derivada debería poder usarse 
en cualquier lugar donde se espera una instancia de la clase base sin alterar el comportamiento esperado.

Documentación: Si el comportamiento del método sobrescrito difiere significativamente del original, 
es importante documentarlo claramente.

No olvidar super(): Cuando sea apropiado, asegúrate de llamar al método de la clase base usando 
super() para mantener el comportamiento base.

class Base:
'''
class Notificacion:
    '''Clase base para notificaciones'''
    def __init__(self, destinatario, mensaje):
        self.destinatario = destinatario
        self.mensaje = mensaje
        self.enviada = False

    def enviar(self):
        ''' Lógica genérica de envío '''
        print(f"Enviando mensaje a {self.destinatario}")
        self.enviada = True
        return True

    def obtener_estado(self):
        ''' Retorna el estado de la notificación'''
        return "Enviada" if self.enviada else "Pendiente"

class NotificacionEmail(Notificacion):
    '''Clase para notificaciones vía email'''
    def __init__(self, destinatario, mensaje, asunto):
        super().__init__(destinatario, mensaje)
        self.asunto = asunto

    def enviar(self):
        ''' Verificamos que el destinatario tenga formato de email'''
        if "@" not in self.destinatario:
            print(f"Error: {self.destinatario} no es un email válido")
            return False

        # Si es válido, llamamos al método de la clase base
        print(f"Enviando email con asunto: {self.asunto}")
        return super().enviar()

class NotificacionSMS(Notificacion):
    '''Clase para notificaciones vía SMS'''
    def __init__(self, destinatario, mensaje):
        # Aseguramos que el destinatario sea un número
        destinatario_limpio = ''.join(c for c in destinatario if c.isdigit())
        super().__init__(destinatario_limpio, mensaje)

    def enviar(self):
        # Verificamos la longitud del mensaje para SMS
        if len(self.mensaje) > 160:
            print("Advertencia: El mensaje excede los 160 caracteres y se enviará truncado")
            self.mensaje = self.mensaje[:157] + "..."

        # Llamamos al método de la clase base
        return super().enviar()

    def obtener_estado(self):
        estado_base = super().obtener_estado()
        return f"SMS {estado_base}"

# Notificación por email
email = NotificacionEmail("usuario@ejemplo.com", "Tu pedido ha sido procesado", "Estado de pedido")
email.enviar()
print(email.obtener_estado())  # Enviada

# Notificación por SMS
sms = NotificacionSMS("555-123-4567", "Tu código de verificación es 123456")
sms.enviar()
print(sms.obtener_estado())  # SMS Enviada

# Email con dirección inválida
email_invalido = NotificacionEmail("usuario_sin_arroba", "Mensaje importante", "Urgente")
email_invalido.enviar()  # Mostrará error y no enviará
print(email_invalido.obtener_estado())  # Pendiente

# SMS con mensaje largo
sms_largo = NotificacionSMS("555-987-6543", "Este es un mensaje muy largo que excede el límite de caracteres permitido para un SMS estándar. Los mensajes SMS normalmente tienen un límite de 160 caracteres.")
sms_largo.enviar()  # Mostrará advertencia y truncará el mensaje
print(sms_largo.obtener_estado())  # SMS Enviada
