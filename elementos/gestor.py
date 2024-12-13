import elementos.carta as c
import random
import ajustes.constantes as const
import elementos.jugador as j

# Descripción: Clase que representa una baraja de cartas. Cada baraja tiene 52 cartas.
class Baraja:
    def __init__(self):
        self.cartas = [c.Carta(palo, valor) for palo in c.Carta.getPalos() for valor in c.Carta.getValores()]
        random.shuffle(self.cartas)
    
    def robar_carta(self):
        carta = self.cartas.pop(0)
        return carta
        
    def __str__(self):
        return ', \n'.join([carta.toString() for carta in self.cartas])

# Función para inicializar la baraja y los jugadores
def inicializar_juego():
    baraja = Baraja()
    
    num_jugadores = int(input("Introduce el número de jugadores (máximo 4): "))
    if num_jugadores > const.num_jugadores_max:
        num_jugadores = const.num_jugadores_max
    
    for i in range(num_jugadores):
        nombre = input(f"Introduce el nombre del jugador {i + 1}: ")
        j.añadir_jugador(j.Jugador(nombre))
    
    return baraja, j.jugadores

# Descripción: Función que reparte cartas a los jugadores. Cada jugador recibe dos cartas.
def repartir_cartas(baraja, jugadores):
    for jugador in jugadores:
        while len(jugador.cartas) < const.num_cartas_por_jugador:
            carta = baraja.robar_carta()
            const.num_cartas_restantes -= 1
            jugador.cartas.append(carta)

# Descripción: Función que coloca cartas sobre la mesa. Inicialmente coloca tres cartas.
def cartas_sobre_mesa(baraja):
    mesa = []
    while const.num_cartas_presentes_en_mesa < 3:
        carta = baraja.robar_carta()
        mesa.append(carta)
        const.num_cartas_presentes_en_mesa += 1
        const.num_cartas_restantes -= 1
    return mesa