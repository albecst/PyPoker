import carta as c
import random
import constantes as const

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