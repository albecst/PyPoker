import ajustes.constantes as const

def check(jugador):
    print(f'{jugador.nombre} ha hecho check.')

def call(jugador):
    cantidad_a_igualar = const.apuesta_actual - jugador.apuesta_actual
    if cantidad_a_igualar > 0:
        print(f'{jugador.nombre} ha hecho call de {cantidad_a_igualar} créditos.')
        raise_bet(jugador, cantidad_a_igualar)
    else:
        print(f'{jugador.nombre} ya está igualado con la apuesta actual.')

def raise_bet(jugador, cantidad):
    print()
    print(f'{jugador.nombre} ha hecho raise de {cantidad} créditos.')
    total_apostado = 0
    monedas_apostadas = {}

    for denominacion in sorted(const.denominaciones, reverse=True):
        if total_apostado < cantidad:
            max_monedas = (cantidad - total_apostado) // denominacion
            num_monedas = min(max_monedas, jugador.monedas[denominacion])
            monedas_apostadas[denominacion] = num_monedas
            total_apostado += num_monedas * denominacion
            if total_apostado >= 5:
                print(f'Llevas apostados {total_apostado} créditos.\n')

    if total_apostado >= cantidad:
        for denominacion, num_monedas in monedas_apostadas.items():
            jugador.eliminar_fichas(denominacion, num_monedas)
        jugador.apuesta_actual += cantidad
        const.apuesta_actual = max(const.apuesta_actual, jugador.apuesta_actual)
    else:
        print(f'No se pudo completar la apuesta de {cantidad} créditos. Solo se apostaron {total_apostado} créditos.')

def fold(jugador):
    print(f'{jugador.nombre} ha hecho fold.')

def añadir_creditos(jugador, cantidad):
    jugador.sumar_dinero(cantidad)
    print(f'{jugador.nombre} ha añadido {cantidad} créditos.')

def all_in(jugador):
    cantidad = jugador.dinero
    raise_bet(jugador, cantidad)