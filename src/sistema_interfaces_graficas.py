'''

'''
class Widget:
    def __init__(self, x=0, y=0, visible=True, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.visible = visible

    def dibujar(self):
        if self.visible:
            return f"Dibujando widget en ({self.x}, {self.y})"
        return ""

class Clickable:
    def __init__(self, on_click=None, **kwargs):
        super().__init__(**kwargs)
        self.on_click = on_click or (lambda: None)

    def click(self):
        return self.on_click()

class Draggable:
    def __init__(self, dragging=False, **kwargs):
        super().__init__(**kwargs)
        self.dragging = dragging

    def iniciar_arrastre(self):
        self.dragging = True
        return "Iniciando arrastre"

    def finalizar_arrastre(self):
        self.dragging = False
        return "Finalizando arrastre"

class Boton(Widget, Clickable):
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.texto = texto

    def dibujar(self):
        base = super().dibujar()
        if base:
            return f"{base} - Botón: {self.texto}"
        return ""

class IconoArrastrable(Widget, Clickable, Draggable):
    def __init__(self, icono, **kwargs):
        super().__init__(**kwargs)
        self.icono = icono

    def dibujar(self):
        base = super().dibujar()
        if base:
            estado = "arrastrándose" if self.dragging else "estático"
            return f"{base} - Icono: {self.icono} ({estado})"
        return ""

# Ejemplo de uso

def accion_boton():
    return "Botón pulsado!"

boton = Boton(
    texto="Aceptar",
    x=100, 
    y=200,
    on_click=accion_boton
)

icono = IconoArrastrable(
    icono="📁",
    x=50,
    y=50
)

print(boton.dibujar())        # Dibujando widget en (100, 200) - Botón: Aceptar
print(boton.click())          # Botón pulsado!

print(icono.dibujar())        # Dibujando widget en (50, 50) - Icono: 📁 (estático)
print(icono.iniciar_arrastre())
print(icono.dibujar())        # Dibujando widget en (50, 50) - Icono: 📁 (arrastrándose)
