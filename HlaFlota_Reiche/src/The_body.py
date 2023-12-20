import numpy as np
from numpy import random
import config
from Posicionar_barcos_tableros1_2 import *
from Disparo_jug1 import *
from Disparo_jug2_CPU import *
from Marcador import *
print("""
  ___ ___                   .___.__         .__             _____.__          __          
 /   |   \ __ __  ____    __| _/|__|______  |  | _____    _/ ____\  |   _____/  |______   
/    ~    \  |  \/    \  / __ | |  \_  __ \ |  | \__  \   \   __\|  |  /  _ \   __\__  \  
\    Y    /  |  /   |  \/ /_/ | |  ||  | \/ |  |__/ __ \_  |  |  |  |_(  <_> )  |  / __ \_
 \___|_  /|____/|___|  /\____ | |__||__|    |____(____  /  |__|  |____/\____/|__| (____  /
       \/            \/      \/                       \/                               \/ 
""")
print('Hola!! he preparado para tu diversion este entretenido juego de hundir la flota. El tablero en el que se desarrolla el juego es de (0,9)x(0,9)')
inicio =input("¿Quieres jugar una partida ('S'/'N'?)")
if inicio.lower()=='s':
    tablero1,tablero2,tablero3,tablero4=posicionar()
    while config.salida==False:
        disparo_jug1(tablero2,tablero3,tablero1)
        if config.salida:
            break
        disparo_jug2(tablero1,tablero4,tablero2)
        if config.salida:
            break
        marcador_jug1(tablero3)
        marcador_jug2(tablero4)
        ganador(tablero3,tablero4)
        if config.salida: 
            break
elif inicio.lower()=='n':
    print('Muchas gracias, nos vemos pronto')
else: 
    print('Has introducido mal la letra para inicializar o rechazar el juego')

