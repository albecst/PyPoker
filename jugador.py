import constantes as const

class Jugador:
    def __init__(self, nombre, dinero):
        self.nombre = nombre
        self.dinero = dinero
        self.cartas = []

    def toString(self):
        return f'{self.nombre} --> {self.dinero}, Cartas: {", ".join([carta.toString() for carta in self.cartas])}'

    def sumar_dinero(self, dinero_ganado):
        self.dinero += dinero_ganado

    def set_dinero(self, dinero):
        self.dinero = dinero

    def robar_carta(self, carta):
        self.cartas.append(carta)

    def conseguir_cartas(self, cartas):
        self.cartas = cartas

jugadores = []

def añadir_jugador(jugador):
    jugadores.append(jugador)
    const.num_jugadores += 1