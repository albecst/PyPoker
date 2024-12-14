import ajustes.constantes as const

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cartas = []
        self.monedas = {
            5: const.monedas_de_5_iniciales,
            10: const.monedas_de_10_iniciales,
            25: const.monedas_de_25_iniciales,
            50: const.monedas_de_50_iniciales,
            100: const.monedas_de_100_iniciales
        }
        self.dinero = self.calcular_dinero_total()
        self.apuesta_actual = 0

    def toString(self):
        fichas_str = ', '.join([f'{cantidad} fichas de {denominacion} créditos' for denominacion, cantidad in self.monedas.items()])
        return f'{self.nombre} --> {self.dinero} créditos ({fichas_str}), Cartas: {", ".join([carta.toString() for carta in self.cartas])}'

    def sumar_dinero(self, dinero_ganado):
        self.dinero += dinero_ganado
        self.monedas = self.convertir_a_monedas(self.dinero)

    def set_dinero(self, dinero):
        self.dinero = dinero
        self.monedas = self.convertir_a_monedas(dinero)

    def robar_carta(self, carta):
        self.cartas.append(carta)

    def calcular_dinero_total(self):
        return sum([denominacion * cantidad for denominacion, cantidad in self.monedas.items()])

    def convertir_a_monedas(self, dinero):
        monedas = {}
        for denominacion in sorted(const.denominaciones, reverse=True):
            monedas[denominacion], dinero = divmod(dinero, denominacion)
        return monedas

    def conseguir_cartas(self, cartas):
        self.cartas = cartas

    def ha_igualado_apuesta(self):
        return self.apuesta_actual >= const.apuesta_actual

jugadores = []

def añadir_jugador(jugador):
    jugadores.append(jugador)
    const.num_jugadores += 1