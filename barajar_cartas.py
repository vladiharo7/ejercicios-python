import random

def crear_baraja():
    """Crea una baraja estándar de 52 cartas."""
    palos = ["♠", "♥", "♦", "♣"]
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return [f"{valor}{palo}" for palo in palos for valor in valores]

def barajar(mazo):
    """Baraja un mazo de cartas y devuelve el mazo mezclado."""
    return random.sample(mazo, len(mazo))

def repartir_mano(mazo, num_cartas):
    """Reparte una mano de cartas del mazo."""
    return random.sample(mazo, num_cartas)

# Crear y barajar una baraja
baraja = crear_baraja()
baraja_barajada = barajar(baraja)

# Repartir manos a dos jugadores
mano_jugador1 = repartir_mano(baraja_barajada, 5)
# Eliminamos las cartas ya repartidas para el segundo jugador
baraja_restante = [carta for carta in baraja_barajada if carta not in mano_jugador1]
mano_jugador2 = repartir_mano(baraja_restante, 5)

print(f"Mano del Jugador 1: {mano_jugador1}")
print(f"Mano del Jugador 2: {mano_jugador2}")
