#En esta función vemos las posiciones que le faltan al jugador 1 para ganar
#Tambien vemos los aciertos efectuados hasta el momento. Sabemos que el primero que llegue a 10 gana
def marcador_jug1(tablero3):
    """
    Esta funcion te pide que le pases el tablero 3 y te dice como está el marcador del juego para el jugador 1
    """
    import config
    counter=0
    secu1=list(range(0,10))
    secu2=list(range(0,10))
    for n in secu1:
        for m in secu2:
            if (tablero3[n,m]=='X'):
                counter=counter+1
            else:
                posiciones=10-counter
    print('Quedan %s posiciones para hundir la flota de jugador2(CPU)'%(posiciones))      
    print('Aciertos efectuados por jugador1:',counter,'de 10')
    return counter

#En esta función vemos las posiciones que le faltan al jugador 1 para ganar
#Tambien vemos los aciertos efectuados hasta el momento. Sabemos que el primero que llegue a 10 gana
def marcador_jug2(tablero4):
    """
    Esta funcion te pide que le pases el tablero 4 y te dice como está el marcador del juego para el jugador2(CPU)
    """
    import config
    counter=0
    secu1=list(range(0,10))
    secu2=list(range(0,10))
    for n in secu1:
        for m in secu2:
            if (tablero4[n,m]=='X'):
                counter=counter+1
            else:
                posiciones=10-counter
    print('Quedan %s posiciones para hundir la flota de jugador1'%(posiciones))      
    print('Aciertos efectuados por jugador2(CPU):',counter,'de 10')
    return counter

def ganador(tablero3,tablero4):
    
    """
    Esta funcion te dice cuando un jugador ha ganado la partida
    """
    import config
    if (marcador_jug1(tablero3)==10)and (marcador_jug2(tablero4)<10):
        print('EL JUGADOR 1 GANA LA PARTIDA ')
        config.salida=True #Variable para salida del juego
    elif(marcador_jug2(tablero4)==10)and (marcador_jug1(tablero3)<10):
        print('EL JUGADOR 2 GANA LA PARTIDA ')
        config.salida=True #Variable para salida del juego
    else:
        print('PARTIDA EN JUEGO')