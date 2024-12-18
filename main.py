import elementos.gestor as g
import ajustes.constantes as const
import ui_ux.prints as p
import elementos.jugador as j
import logica.mecanicas as m
import ui_ux.sysWOW as os
from time import sleep

def iniciar_juego_con_jugadores():
    baraja, jugadores = g.inicializar_juego()
    g.repartir_cartas(baraja, jugadores)
    mesa = g.cartas_sobre_mesa(baraja)
    return baraja, jugadores, mesa

def reiniciar_partida(jugadores, dealer):
    baraja = g.Baraja()
    g.repartir_cartas(baraja, jugadores)
    mesa = []
    mesa = g.cartas_sobre_mesa(baraja)
    dealer = (dealer + 1) % len(jugadores)
    return baraja, jugadores, mesa, dealer

def main():
    partida = 1
    opcion = 0
    jugador_actual = 0
    dinero_en_juego = 0
    dealer = 0
    
    os.clear_console()

    while opcion != -1:
        p.print_opciones_inicio()
        try:
            opcion = int(input('Introduce una opción: '))
        except ValueError:
            os.clear_console()
            print('Opción no válida. Inténtalo de nuevo.')
            continue

        if opcion == 1:
            os.clear_console()
            baraja, jugadores, mesa = iniciar_juego_con_jugadores()
            modo = 1
            break
        elif opcion == 2:
            os.clear_console()
            print('Opción aún no disponible.')
            modo = 2
        elif opcion == 3:
            os.clear_console()
            print('Saliendo del juego...')
            break
        else:
            os.clear_console()
            print('Opción no válida. Inténtalo de nuevo.')

    while modo == 1:
        os.clear_console()

        opcion = 0
        ronda = 1 # Ronda de apuestas: 1 = preflop, 2 = flop, 3 = turn, 4 = river
        jugadores_activos = len(jugadores)
        num_jugadores_restantes_por_preguntar = len(jugadores)
        os.clear_console()

        # Inicializar las ciegas
        sleep(1)
        small_blind = (dealer) % len(jugadores)
        big_blind = (dealer + 1) % len(jugadores)
        m.raise_bet(jugadores[small_blind], 5)  # Small blind
        sleep(1)
        m.raise_bet(jugadores[big_blind], 10)  # Big blind
        jugador_actual = (dealer + 2) % len(jugadores)
        print('Cargando', end = '', flush=True)
        for i in range(0, 4):
            sleep(0.5)
            print('.', end='', flush=True)
        print()
        os.clear_console()
        
        print(f'Partida {partida}')

        while opcion != -1 or ronda <= 4:
            print(f'\n*** Ronda: {ronda} ***')
            print(f'Jugadores activos: {len(j.jugadores)}')
            cantidad_a_igualar = const.apuesta_actual - jugadores[jugador_actual].apuesta_actual
            dinero_en_juego = sum(jugador.apuesta_actual for jugador in jugadores)

            print(f'Jugadores restantes por preguntar: {num_jugadores_restantes_por_preguntar}')
            print(f'\n| Dinero en juego: {dinero_en_juego} créditos. |')
            if cantidad_a_igualar > 0:
                print(f'\n| Jugador {jugadores[jugador_actual].nombre}, necesitas añadir {cantidad_a_igualar} créditos para igualar la apuesta. |')
            if cantidad_a_igualar == 0:
                print(f'\n| Jugador {jugadores[jugador_actual].nombre}, puedes hacer check. |')
            
            p.print_opciones_juego()

            try:
                opcion = int(input(f'Jugador {jugadores[jugador_actual].nombre}, introduce una opción: '))
            except ValueError:
                os.clear_console()
                print('Opción no válida. Inténtalo de nuevo.')
                continue
            print()
            
            if opcion == 1:
                if jugadores[jugador_actual].apuesta_actual >= const.apuesta_actual:
                    os.clear_console()
                    m.check(jugadores[jugador_actual])
                    jugador_actual = (jugador_actual + 1) % len(jugadores)
                    num_jugadores_restantes_por_preguntar -= 1
                elif ronda > 1 and const.apuesta_actual == 0:
                    os.clear_console()
                    m.check(jugadores[jugador_actual])
                    jugador_actual = (jugador_actual + 1) % len(jugadores)
                    num_jugadores_restantes_por_preguntar -= 1
                else:
                    os.clear_console()
                    print('No puedes hacer check si no has igualado o superado la apuesta.')
            
            elif opcion == 2:
                os.clear_console()
                m.call(jugadores[jugador_actual])
                jugador_actual = (jugador_actual + 1) % len(jugadores)
                num_jugadores_restantes_por_preguntar -= 1
                sleep(2.5)
                os.clear_console()
            
            elif opcion == 3:
                opcion = 0
                while opcion != 11:
                    os.clear_console()
                    print(f'Apuesta actual: {const.apuesta_actual} créditos.\n')
                    p.print_opciones_apuestas()
                    try:
                        opcion = int(input('Introduce una opción: '))
                    except ValueError:
                        os.clear_console()
                        print('Opción no válida. Inténtalo de nuevo.')
                        continue

                    if opcion == 1:
                        m.raise_bet(jugadores[jugador_actual], 5)
                        num_jugadores_restantes_por_preguntar = jugadores_activos - 1
                    elif opcion == 2:
                        m.raise_bet(jugadores[jugador_actual], 10)
                        num_jugadores_restantes_por_preguntar = jugadores_activos - 1
                    elif opcion == 3:
                        m.raise_bet(jugadores[jugador_actual], 25)
                        num_jugadores_restantes_por_preguntar = jugadores_activos - 1
                    elif opcion == 4:
                        m.raise_bet(jugadores[jugador_actual], 50)
                        num_jugadores_restantes_por_preguntar = jugadores_activos - 1
                    elif opcion == 5:
                        m.raise_bet(jugadores[jugador_actual], 100)
                        num_jugadores_restantes_por_preguntar = jugadores_activos - 1
                    elif opcion == 6:
                        opcion = 0
                        p.print_all_in()
                        while opcion != -1:
                            try:
                                opcion = int(input('Introduce una opción: '))
                            except ValueError:
                                os.clear_console()
                                print('Opción no válida. Inténtalo de nuevo.')
                                continue

                            if opcion == 11:
                                p.print_all_in_suerte()
                                m.all_in(jugadores[jugador_actual])
                                num_jugadores_restantes_por_preguntar = jugadores_activos - 1
                                jugadores_activos -= 1
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
                    
                jugador_actual = (jugador_actual + 1) % len(jugadores)
            
            elif opcion == 4:
                os.clear_console()
                m.fold(jugadores[jugador_actual])
                jugadores_activos -= 1
                num_jugadores_restantes_por_preguntar -= 1
                jugador_actual = (jugador_actual + 1) % len(jugadores)
            
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
            
            elif opcion == 9 and ronda > 1:
                os.clear_console()
                os.clear_console()
                print(jugadores[jugador_actual].toString1())
                print(f'\nMesa --> Cartas: {", ".join([carta.toString() for carta in mesa])}')
            
            elif opcion == 9 and ronda == 1:
                os.clear_console()
                print(jugadores[jugador_actual].toString1())
                print('\nMesa --> Cartas: ? ? ?')
            
            else:
                os.clear_console()
                print('Opción no válida. Inténtalo de nuevo.')
            
            # Verificar si todos los jugadores han igualado la apuesta o se han retirado
            if all(jugador.ha_igualado_apuesta() or jugador.apuesta_actual == 0 for jugador in jugadores if jugador.apuesta_actual > 0) and num_jugadores_restantes_por_preguntar == 0:
                if ronda == 1:
                    ronda += 1
                    os.clear_console()
                    print(f'Mesa --> Cartas: {", ".join([carta.toString() for carta in mesa])}')  # Información sobre la mesa
                    num_jugadores_restantes_por_preguntar = jugadores_activos
                elif ronda == 2:
                    mesa.append(g.mostrar_turn(baraja))
                    ronda += 1
                    num_jugadores_restantes_por_preguntar = jugadores_activos
                elif ronda == 3:
                    mesa.append(g.mostrar_river(baraja))
                    num_jugadores_restantes_por_preguntar = jugadores_activos
                    ronda += 1
                elif ronda == 4:
                    os.clear_console()
                    g.mostrar_showdown(jugadores, mesa)
                    input("Enter para pasar a la siguiente partida...")
                    break 
                
            # Si solo queda un jugador activo, termina la ronda (por si hacen todos check o fold)
            if jugadores_activos == 1:
                os.clear_console()
                g.mostrar_showdown(jugadores, mesa)
                input("Enter para pasar a la siguiente partida...")
                break 
        
        # Incrementar el número de la partida y reiniciar la partida
        partida += 1
        baraja, jugadores, mesa, dealer = reiniciar_partida(jugadores, dealer)

if __name__ == "__main__":
    main()