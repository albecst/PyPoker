import elementos.gestor as g
import ajustes.constantes as const
import ui_ux.prints as p
import elementos.jugador as j

def iniciar_juego_con_jugadores():
    baraja, jugadores = g.inicializar_juego()
    g.repartir_cartas(baraja, jugadores)
    mesa = g.cartas_sobre_mesa(baraja)
        
    for jugador in jugadores:
        print(jugador.toString1())
    print(f'\nMesa --> Cartas: {", ".join([carta.toString() for carta in mesa])}')
    return jugadores, mesa

def main():
    opcion = 0
    jugador_actual = 0
    
    while opcion != -1:
        p.print_opciones_inicio()
        opcion = int(input('Introduce una opción: '))
        if opcion == 1:
            jugadores, mesa = iniciar_juego_con_jugadores()
            break
        elif opcion == 3:
            opcion = -1
        else:
            print('Opción no válida. Inténtalo de nuevo.')
            
    opcion = 0
    
    while opcion != -1:
        p.print_opciones_juego()
        opcion = int(input(f'Jugador {jugadores[jugador_actual].nombre}, introduce una opción: '))
        if opcion == 1:
            print('Check') # Hacer check
            jugador_actual = (jugador_actual + 1) % len(jugadores)
        elif opcion == 2:
            print('Call') # Hacer call
            jugador_actual = (jugador_actual + 1) % len(jugadores)
        elif opcion == 3:
            print('Raise') # Hacer raise
            jugador_actual = (jugador_actual + 1) % len(jugadores)
        elif opcion == 4:
            print('Fold') # Hacer fold
            jugador_actual = (jugador_actual + 1) % len(jugadores)
        elif opcion == 5:
            print(jugadores[jugador_actual].toString1())
        elif opcion == 6:
            for jugador in jugadores:
                if jugador != jugadores[jugador_actual]:
                    print(jugador.toString2())  # Imprimir información sobre otros jugadores
        elif opcion == 7:
            print(f'Mesa --> Cartas: {", ".join([carta.toString() for carta in mesa])}')  # Información sobre la mesa
        elif opcion == 8:
            if len(jugadores) < const.num_jugadores_max:
                nombre = input("Introduce el nombre del nuevo jugador: ")
                j.añadir_jugador(j.Jugador(nombre))
                print(f'Jugador {nombre} añadido.')
            else:
                print('No se pueden añadir más jugadores.')
        else:
            print('Opción no válida. Inténtalo de nuevo.')
        
if __name__ == "__main__":
    main()