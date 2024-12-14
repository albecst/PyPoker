import ajustes.constantes as const

def check(jugador):
    print(f'{jugador.nombre} ha hecho check.')

def call(jugador):
    print(f'{jugador.nombre} ha hecho call.')

def raise_bet(jugador, cantidad):
    print(f'{jugador.nombre} ha hecho raise de {cantidad} créditos.')
    jugador.sumar_dinero(-cantidad)

def fold(jugador):
    print(f'{jugador.nombre} ha hecho fold.')

def añadir_creditos(jugador, cantidad):
    jugador.sumar_dinero(cantidad)
    print(f'{jugador.nombre} ha añadido {cantidad} créditos.')