import elementos.gestor as g
import ajustes.constantes as const
import ui_ux.prints as p
import elementos.jugador as j
import logica.mecanicas as m

def iniciar_juego_con_jugadores():
    baraja, jugadores = g.inicializar_juego()
    g.repartir_cartas(baraja, jugadores)
    mesa = g.cartas_sobre_mesa(baraja)
        
    for jugador in jugadores:
        print(jugador.toString())
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
            
    # Inicializar las ciegas
    m.raise_bet(jugadores[0], 5)  # Small blind
    m.raise_bet(jugadores[1], 10)  # Big blind
    
    opcion = 0
    ronda = 1  # Ronda de apuestas: 1 = pre-flop, 2 = flop, 3 = turn, 4 = river
    
    while opcion != -1:
        p.print_opciones_juego()
        opcion = int(input(f'Jugador {jugadores[jugador_actual].nombre}, introduce una opción: '))
        if opcion == 1:
            m.check(jugadores[jugador_actual])
        elif opcion == 2:
            m.call(jugadores[jugador_actual])
        elif opcion == 3:
            cantidad = int(input('Introduce la cantidad para raise: '))
            m.raise_bet(jugadores[jugador_actual], cantidad)
        elif opcion == 4:
            m.fold(jugadores[jugador_actual])
        elif opcion == 5:
            print(jugadores[jugador_actual].toString())
        elif opcion == 6:
            for jugador in jugadores:
                if jugador != jugadores[jugador_actual]:
                    print(jugador.toString())  # Imprimir información sobre otros jugadores
        elif opcion == 7:
            print(f'Mesa --> Cartas: {", ".join([carta.toString() for carta in mesa])}')  # Información sobre la mesa
        elif opcion == 8:
            if len(jugadores) < const.num_jugadores_max:
                nombre = input("Introduce el nombre del nuevo jugador: ")
                g.añadir_jugador(j.Jugador(nombre))
                print(f'Jugador {nombre} añadido.')
            else:
                print('No se pueden añadir más jugadores.')
        else:
            print('Opción no válida. Inténtalo de nuevo.')
        
        # Actualizar el turno del jugador
        jugador_actual = (jugador_actual + 1) % len(jugadores)
        
        # Verificar si todos los jugadores han igualado la apuesta o se han retirado
        if all(jugador.ha_igualado_apuesta() for jugador in jugadores):
            if ronda == 1:
                mesa.extend(g.mostrar_flop(g.baraja)) # (Más eficiente que hacer muchos appends dentro de un for)
                ronda += 1
            elif ronda == 2:
                mesa.extend(g.mostrar_turn(g.baraja))
                ronda += 1
            elif ronda == 3:
                mesa.extend(g.mostrar_river(g.baraja))
                ronda += 1
            elif ronda == 4:
                g.mostrar_showdown(jugadores, mesa)
                break

if __name__ == "__main__":
    main()