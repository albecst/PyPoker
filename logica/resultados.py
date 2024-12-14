import elementos.gestor as g
import ajustes.constantes as const
import ui_ux.prints as p
import elementos.jugador as j
import logica.mecanicas as m

def iniciar_juego_con_jugadores():
    baraja, jugadores = g.inicializar_juego()
    g.repartir_cartas(baraja, jugadores)
    mesa = g.cartas_sobre_mesa(baraja)
    
    # print("\nJuego iniciado. A continuación puede ver la información sobre los jugadores y la mesa:")    DEBUG
    # for jugador in jugadores:                                                                            DEBUG                     
    #     print()                                                                                          DEBUG
    #     print(jugador.toString1())                                                                       DEBUG
    
    print(f'\nMesa --> Cartas: {", ".join([carta.toString() for carta in mesa])}')
    return jugadores, mesa

def main():
    opcion = 0
    jugador_actual = 0
    opcion = int(input('Introduce una opción: '))

    while opcion != -1:
        p.print_opciones_inicio()
        if opcion == 1:
            jugadores, mesa = iniciar_juego_con_jugadores()
            break
        elif opcion == 3:
            opcion = -1
        else:
            print('Opción no válida. Inténtalo de nuevo.')
            
    m.raise_bet(jugadores[0], 5)  # Small blind
    m.raise_bet(jugadores[1], 10)  # Big blind
    
    opcion = 0
    ronda = 1  # Ronda de apuestas: 1 = pre-flop, 2 = flop, 3 = turn, 4 = river
    print(jugadores[jugador_actual].toString1())

    p.print_opciones_juego()
    while opcion != -1:
        opcion = int(input(f'Jugador {jugadores[jugador_actual].nombre}, introduce una opción: '))
        print()
        if opcion == 1:
            print('Check') # Hacer check
            jugador_actual = (jugador_actual + 1) % len(jugadores)
            print(jugadores[jugador_actual].toString1())

        elif opcion == 2:
            print('Call') # Hacer call
            jugador_actual = (jugador_actual + 1) % len(jugadores)
            print(jugadores[jugador_actual].toString1())
        elif opcion == 3:
            opcion = 0
            p.print_opciones_apuestas()
            while opcion != 11:
                opcion = int(input('Introduce una opción: '))
                if opcion == 1:
                    print('Añadir 5 créditos')
                elif opcion == 2:
                    print('Añadir 10 créditos')
                elif opcion == 3:
                    print('Añadir 25 créditos')
                elif opcion == 4:
                    print('Añadir 50 créditos')
                elif opcion == 5:
                    print('Añadir 100 créditos')
                elif opcion == 6:
                    opcion = 0
                    p.print_all_in()
                    while opcion != -1:
                        opcion = int(input('Introduce una opción: '))
                        if opcion == 11:
                            p.print_all_in_suerte()
                            break
                        elif opcion == 2:
                            print('No ALL IN')
                            p.print_opciones_apuestas()
                            break
                        else:
                            print('Opción no válida. Inténtalo de nuevo.')
                elif opcion == 7:
                    print('No quiero añadir más créditos')
                    break
                else:
                    print('Opción no válida. Inténtalo de nuevo.')
            jugador_actual = (jugador_actual + 1) % len(jugadores)
            print(jugadores[jugador_actual].toString1())
        elif opcion == 4:
            print('Fold') # Hacer fold
            jugador_actual = (jugador_actual + 1) % len(jugadores)
            print(jugadores[jugador_actual].toString1())
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