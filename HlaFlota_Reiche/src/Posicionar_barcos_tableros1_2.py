### POSICIONAR BARCOS EN TABLEROS 1 Y 2(CPU)

def posicionar():
    """
    Esta función te posiciona los barcos del jugador 1 en el tablero 1 de forma aleatoria.
    Y posiciona los barcos del jugador 2 (CPU) en el tablero 2 de forma aleatoria.

    No se hace uso del tablero 3, que es donde el jugador 1 visualiza los resultados de sus 
    disparos sobre el tablero2. Eso lo miramos en la funcion 'Disparo_jug1'

    No se hace uso del tablero 4, que es donde el jugador 2 (CPU) visualiza los resultados de sus 
    disparos sobre el tablero1. Eso lo miramos en la funcion 'Disparo_jug2   
    
    """
    import numpy as np
    import pandas as pd
    from numpy import random
    tablero3 = np.full(fill_value = ' ', shape = (10, 10)) #Visualiza Ataque de jugado1
    tablero4 = np.full(fill_value = ' ', shape = (10, 10)) #Visualiza Ataque de jugado2

#Tablero_1  ***************************************************
    tablero1 = np.full(fill_value = ' ', shape = (10, 10))
    
    seq=[1,1,1,1,2,2,2,3,3,4]  #Se Comparte la misma lista de secuencia para posicionar los barcos en tablero1 y en 
                               # tablero2 

    for n in seq: 
   
        while True:
            eslora = n
        # 'N' - 'S' - 'E' - 'O'
            orient = random.choice(['N', 'S', 'E', 'O'])

    # Posicion inicial del barco
            current_pos = np.random.randint(10, size = 2)  #Esto me genera un array unidimensional de 2 elementos con mumero aleatorios del 0 al 9
                                                           #Ejemplo [9,5] --> current_pos me da el punto donde quiero insertar el barco
            fila = current_pos[0]                          #Aqui lo que hago es descomponer el punto de insercion en fila y col
            col = current_pos[1]
    
    # Recogemos las eslora=(n=4) posiciones colindantes a current_pos -->CASO PARA 4 POSICIONES!!
            
            coors_posiN = tablero1[fila:fila - eslora:-1, col] #Aquí vamos a colocar el barco de 4 posiciones en POSICION NORTE 
            coors_posiE = tablero1[fila, col: col + eslora]     #Para el caso de [9,5] coors_posiN = tablero[fila:fila - es lora:-1, col] sería:
            coors_posiS = tablero1[fila:fila + eslora, col]     #coors_posiN=tablero[9:9-4:-1,5]-->Fila:'start' en 9 , 'Stop' en 5 y baja de -1 en -1 y
            coors_posiO = tablero1[fila, col: col - eslora:-1]  #la Columna se mantiene fija en 5. El efecto sería como... elegido un punto bajas SUBES en | VERTICAL
                                      
                                                       #ESTE: Efecto.. elige un punto y colocamos el barco hacia la derecha en -- HORIZONTAL
                                                       #SUR: El efecto sería como... elegido un punto bajas BAJAS en | VERTICAL
                                                       #OESTE: Efecto.. elige un punto y colocamos el barco hacia la derecha IZQUIERDA  en -- HORIZONTAL

    # Ahora,Comprobamos si esas posiciones son validas
        # Si no cumple con las dimensiones del tablero, o hay un barco ahí , y se va a producir un solape, entonces:
        # Probamos con otra coordenada  
                          
    # Orientacion Norte
            if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:  # ('O' not in coors_posiN)--> es lo que impide el solape
                tablero1[fila:fila - eslora:-1, col] = 'O'
                break
    # Orientacion Este
            elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                tablero1[fila, col: col + eslora] = 'O'
                break
    # Orientacion Sur
            elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                tablero1[fila:fila + eslora, col] = 'O'
                break
    # Orientacion Oeste
            elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                tablero1[fila, col: col - eslora:-1] = 'O'
                break
            else:
                continue  
    
        tablero1

#Tablero_2_CPU **********************************************
#seq=[1,1,1,1,2,2,2,3,3,4]
    tablero2 = np.full(fill_value = ' ', shape = (10, 10))
    for n in seq: 
   
        while True:
            eslora = n
    # 'N' - 'S' - 'E' - 'O'
            orient = random.choice(['N', 'S', 'E', 'O'])

    # Posicion inicial del barco
            current_pos = np.random.randint(10, size = 2)  #Esto me genera un array unidimensional de 2 elementos con mumero aleatorios del 0 al 9
                                                   #Ejemplo [9,5] --> current_pos me da el punto donde quiero insertar el barco
            fila = current_pos[0]                      #Aqui lo que hago es descomponer el punto de insercion en fila y col
            col = current_pos[1]
    
    # Recogemos las 4 posiciones colindantes a current_pos -->CASO PARA 4 POSICIONES!!
            coors_posiN = tablero2[fila:fila - eslora:-1, col] #Aquí vamos a colocar el barco de 4 posiciones en POSICION NORTE 
            coors_posiE = tablero2[fila, col: col + eslora]     #Para el caso de [9,5] coors_posiN = tablero[fila:fila - es lora:-1, col] sería:
            coors_posiS = tablero2[fila:fila + eslora, col]     #coors_posiN=tablero[9:9-4:-1,5]-->Fila:'start' en 9 , 'Stop' en 5 y baja de -1 en -1 y
            coors_posiO = tablero2[fila, col: col - eslora:-1]  #la Columna se mantiene fija en 5. El efecto sería como... elegido un punto bajas SUBES en | VERTICAL
                                      
                                                       #ESTE: Efecto.. elige un punto y colocamos el barco hacia la derecha en -- HORIZONTAL
                                                       #SUR: El efecto sería como... elegido un punto bajas BAJAS en | VERTICAL
                                                       #OESTE: Efecto.. elige un punto y colocamos el barco hacia la derecha IZQUIERDA  en -- HORIZONTAL

    # Ahora, Comprobamos si esas posiciones son validas
        # Si no cumple con las dimensiones del tablero, o hay un barco ahí , y se va a producir un solape, entonces:
        # Probamos con otra coordenada           

    # Orientacion Norte
            if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                tablero2[fila:fila - eslora:-1, col] = 'O'
                break
    # Orientacion Este
            elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                tablero2[fila, col: col + eslora] = 'O'
                break
    # Orientacion Sur
            elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                tablero2[fila:fila + eslora, col] = 'O'
                break
    # Orientacion Oeste
            elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                tablero2[fila, col: col - eslora:-1] = 'O'
                break
            else:
                continue  
    
        tablero2
    return tablero1,tablero2,tablero3,tablero4

    
