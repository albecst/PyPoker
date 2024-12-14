import elementos.gestor as g
import ajustes.constantes as const
import ui_ux.prints as p
import elementos.jugador as j
import logica.mecanicas as m
import ui_ux.sysWOW as os

def iniciar_juego_con_jugadores():
    baraja, jugadores = g.inicializar_juego()
    g.repartir_cartas(baraja, jugadores)
    mesa = g.cartas_sobre_mesa(baraja)
    
    # print("\nJuego iniciado. A continuación puede ver la información sobre los jugadores y la mesa:")    DEBUG
    # for jugador in jugadores:                                                                            DEBUG                     
    #     print()                                                                                          DEBUG
    #     print(jugador.toString1())                                                                       DEBUG
    
    return baraja, jugadores, mesa

def main():
    os.clear_console()
    p.print_opciones_inicio()
    opcion = 0
    jugador_actual = 0
    opcion = int(input('Introduce una opción: '))

    while opcion != -1:
        if opcion == 1:
            baraja, jugadores, mesa = iniciar_juego_con_jugadores()
            break
        elif opcion == 3:
            opcion = -1
        else:
            print('Opción no válida. Inténtalo de nuevo.')
            
    opcion = 0
    ronda = 1 # Ronda de apuestas: 1 = preflop, 2 = flop, 3 = turn, 4 = river
    jugadores_activos = len(jugadores)
    num_jugadores_restantes_por_preguntar = len(jugadores)
    os.clear_console()

    print(jugadores[jugador_actual].toString1())
    # Inicializar las ciegas
    m.raise_bet(jugadores[0], 5)  # Small blind
    m.raise_bet(jugadores[1], 10)  # Big blind
    jugador_actual = 2 % len(jugadores)

    while opcion != -1:
        print(f'\n*** Ronda: {ronda} ***')
        p.print_opciones_juego()

        opcion = int(input(f'Jugador {jugadores[jugador_actual].nombre}, introduce una opción: '))
        print()
        if opcion == 1 and jugadores[jugador_actual].apuesta_actual >= const.apuesta_actual:
            os.clear_console()
            m.check(jugadores[jugador_actual])
            jugador_actual = (jugador_actual + 1) % len(jugadores)
            print(jugadores[jugador_actual].toString1())
            num_jugadores_restantes_por_preguntar -= 1

        elif opcion == 1 and jugadores[jugador_actual].apuesta_actual < const.apuesta_actual:
            os.clear_console()
            print('No puedes hacer check si no has igualado o superado la apuesta.')

        elif opcion == 2:
            os.clear_console()
            m.call(jugadores[jugador_actual])
            jugador_actual = (jugador_actual + 1) % len(jugadores)
            print(jugadores[jugador_actual].toString1())
            num_jugadores_restantes_por_preguntar -= 1
        
        elif opcion == 3:
            opcion = 0
            while opcion != 11:
                p.print_opciones_apuestas()
                opcion = int(input('Introduce una opción: '))
                if opcion == 1:
                    print('Añadir 5 créditos')
                    m.raise_bet(jugadores[jugador_actual], 5)
                elif opcion == 2:
                    print('Añadir 10 créditos')
                    m.raise_bet(jugadores[jugador_actual], 10)
                elif opcion == 3:
                    print('Añadir 25 créditos')
                    m.raise_bet(jugadores[jugador_actual], 25)
                elif opcion == 4:
                    print('Añadir 50 créditos')
                    m.raise_bet(jugadores[jugador_actual], 50)
                elif opcion == 5:
                    print('Añadir 100 créditos')
                    m.raise_bet(jugadores[jugador_actual], 100)
                elif opcion == 6:
                    opcion = 0
                    p.print_all_in()
                    while opcion != -1:
                        opcion = int(input('Introduce una opción: '))
                        if opcion == 11:
                            p.print_all_in_suerte()
                            m.all_in(jugadores[jugador_actual])
                            break
                        elif opcion == 2:
                            print('No ALL IN')
                            p.print_opciones_apuestas()
                            break
                        else:
                            print('Opción no válida. Inténtalo de nuevo.')
                elif opcion == 7 and jugadores[jugador_actual].apuesta_actual > 0:
                    os.clear_console()
                    print(f'Has añadido {jugadores[jugador_actual].apuesta_actual} créditos.')
                    break
                elif opcion == 7 and jugadores[jugador_actual].apuesta_actual == 0:
                    print('No has añadido créditos. Tienes que añadir al menos 5 créditos.')
                else:
                    print('Opción no válida. Inténtalo de nuevo.')
            if not jugadores[jugador_actual].ha_igualado_apuesta():
                num_jugadores_restantes_por_preguntar = jugadores_activos - 1
            else:
                num_jugadores_restantes_por_preguntar -= 1
                
            jugador_actual = (jugador_actual + 1) % len(jugadores)
            print(jugadores[jugador_actual].toString1())
        
        elif opcion == 4:
            os.clear_console()
            m.fold(jugadores[jugador_actual])
            jugadores_activos -= 1
            jugador_actual = (jugador_actual + 1) % len(jugadores)
            print(jugadores[jugador_actual].toString1())
        
        elif opcion == 5:
            os.clear_console()
            print(jugadores[jugador_actual].toString1())
        
        elif opcion == 6:
            os.clear_console()
            for jugador in jugadores:
                if jugador != jugadores[jugador_actual]:
                    print(jugador.toString2())  # Imprimir información sobre otros jugadores
        
        elif opcion == 7 and ronda > 1:
            os.clear_console()
            print(f'Mesa --> Cartas: {", ".join([carta.toString() for carta in mesa])}')  # Información sobre la mesa
        
        elif opcion == 7 and ronda == 1:
            os.clear_console()
            print('No se pueden mostrar las cartas de la mesa antes del flop.\nMesa --> Cartas: ? ? ?')
        
        elif opcion == 8:
            if len(jugadores) < const.num_jugadores_max:
                nombre = input("Introduce el nombre del nuevo jugador: ")
                j.añadir_jugador(j.Jugador(nombre))
                print(f'Jugador {nombre} añadido.')
            else:
                print('No se pueden añadir más jugadores.')
        
        elif opcion == 9:
            os.clear_console()
        
        else:
            print('Opción no válida. Inténtalo de nuevo.')
        
        # Verificar si todos los jugadores han igualado la apuesta o se han retirado
        if all(jugador.ha_igualado_apuesta() or jugador.apuesta_actual == 0 for jugador in jugadores if jugador.apuesta_actual > 0) and opcion in (1, 2, 3, 4) and num_jugadores_restantes_por_preguntar == 0:
            if ronda == 1:
                ronda += 1
                os.clear_console()
                print(f'Mesa --> Cartas: {", ".join([carta.toString() for carta in mesa])}')  # Información sobre la mesa
            elif ronda == 2:
                mesa.append(g.mostrar_turn(baraja))
                ronda += 1
            elif ronda == 3:
                mesa.append(g.mostrar_river(baraja))
                ronda += 1
            elif ronda == 4:
                g.mostrar_showdown(jugadores, mesa)
                break 
            
        # Si solo queda un jugador activo, termina la ronda (por si hacen todos check o fold)
        if jugadores_activos == 1:
            g.mostrar_showdown(jugadores, mesa)
            break
        
        
        
        
if __name__ == "__main__":
    main()