import elementos.gestor as g
import ajustes.constantes as const

def main():
    baraja, jugadores = g.inicializar_juego()
    
    g.repartir_cartas(baraja, jugadores)
    
    mesa = g.cartas_sobre_mesa(baraja)
    
    print(f'Quedan {const.num_cartas_restantes} cartas en la baraja')
    
    for jugador in jugadores:
        print(jugador.toString())
    print(f'\nMesa --> Cartas: {", ".join([carta.toString() for carta in mesa])}')










if __name__ == "__main__":
    main()