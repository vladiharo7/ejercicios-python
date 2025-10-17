import random

def juego_adivinanza():
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    
    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100.")
    
    while not adivinado and intentos < 7:
        try:
            # Solicitar al usuario que adivine
            intento = int(input("Tu intento: "))
            intentos += 1
            
            # Comprobar el intento
            if intento < numero_secreto:
                print("Demasiado bajo. Intenta un número más alto.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta un número más bajo.")
            else:
                adivinado = True
                print(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    if not adivinado:
        print(f"Lo siento, has agotado tus intentos. El número era {numero_secreto}.")

# Ejecutar el juego
if __name__ == "__main__":
    juego_adivinanza()
# --- IGNORE ---
