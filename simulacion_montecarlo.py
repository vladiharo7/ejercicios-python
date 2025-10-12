import random
import matplotlib.pyplot as plt

def estimar_pi(num_puntos):
    """Estima el valor de π usando el método de Monte Carlo."""
    puntos_dentro = 0
    puntos_x = []
    puntos_y = []
    colores = []
    
    for _ in range(num_puntos):
        # Generar coordenadas aleatorias entre -1 y 1
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        
        puntos_x.append(x)
        puntos_y.append(y)
        
        # Comprobar si el punto está dentro del círculo unitario
        if x**2 + y**2 <= 1:
            puntos_dentro += 1
            colores.append('blue')
        else:
            colores.append('red')
    
    # La proporción de puntos dentro del círculo nos da π/4
    pi_estimado = 4 * puntos_dentro / num_puntos
    
    # Visualización (opcional)
    plt.figure(figsize=(6, 6))
    plt.scatter(puntos_x, puntos_y, c=colores, alpha=0.5, s=10)
    plt.axis('equal')
    plt.title(f'Estimación de π: {pi_estimado:.6f}')
    plt.show()
    
    return pi_estimado

# Estimar π con 10,000 puntos
estimacion = estimar_pi(10000)
print(f"Valor estimado de π: {estimacion}")
print(f"Valor real de π: {3.141592653589793}")
