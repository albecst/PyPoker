import baraja as b
import jugador as j
import constantes as const

# Descripción: Función que reparte cartas a los jugadores. Cada jugador recibe dos cartas.
def repartir_cartas(baraja):
    for jugador in j.jugadores:
        while len(jugador.cartas) < const.num_cartas_por_jugador:
            carta = baraja.robar_carta()
            const.num_cartas_restantes -= 1
            print(f'{jugador.nombre} ha recibido la carta {carta.toString()}')
            jugador.cartas.append(carta)

def cartas_sobre_mesa(baraja):
    while const.num_cartas_presentes_en_mesa <= 3:
        carta = baraja.robar_carta()
        print(f'Carta en la mesa: {carta.toString()}')
        const.num_cartas_presentes_en_mesa += 1
        const.num_cartas_restantes -= 1

def main():
    baraja = b.Baraja()
    
    j.añadir_jugador(j.Jugador('Alberto', 1000))
    j.añadir_jugador(j.Jugador('Bot 2', 1000))
    j.añadir_jugador(j.Jugador('Bot 3', 1000))
    j.añadir_jugador(j.Jugador('Bot 4', 1000))
    
    repartir_cartas(baraja)
    
    cartas_sobre_mesa(baraja)
    
    print(f'Quedan {const.num_cartas_restantes} cartas en la baraja')







if __name__ == "__main__":
    main()