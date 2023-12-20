#Disparo_jug2(CPU)-->(Este es el bueno NO el de las funciones recursivas)
#A esta función le pasas el tablero1 que es donde estan posicionados los barcos del jugador1, y como resultado obtienes si tu disparo ha sido certero o no 
#Para mostrar los resultados del ataque de la maquina (CPU o jugador2) mostramos el estado de tablero 4 que es donde la maquina (CPU o jugador2) visualiza su ataque.
#Para ver como le va, en defensa a la , tienes que imprimir por pantalla el tablero2
#Disparo_jug2-->(CPU-Ordenador))
#A esta funcion le pasas el tablero1

def disparo_jug2(tablero1,tablero4,tablero2): #tablero2     
    """
    Disparo_jug2(CPU)-->A esta función le pasas el "tablero1" que es donde estan posicionados los barcos de la máquina y 
                        "tablero4" que es donde se ven los resultado de ataque del jugador 2 (CPU). 
                        Como resultado obtienes el  disparo  del jugador 2(CPU), si ha sido certero o no, y te muestra un tablero(tablero4) con 
                        resultados de ataque de jugador2(CPU) hasta el momento.      
    """
    import numpy as np
    import config
    from numpy import random
    #global salida
    while True:
            #shoot=str(input('Dime las coordenada del punto al que quieres disparar. El formato con el que tienes que introducir los datos presenta el siguiente aspecto 8.1-->"Fila 8" "Columna 1"'))
            shoot_cpu=np.random.randint(10,size=2)
            dcpu_fila=int(shoot_cpu[0])
            dcpu_col=int(shoot_cpu[1])
            if (0<=dcpu_fila) and (0<=dcpu_col)and (dcpu_fila<=9) and (dcpu_col<=9):
                if tablero1[dcpu_fila,dcpu_col]=='O':
                    tablero1[dcpu_fila,dcpu_col]='X'
                    tablero4[dcpu_fila,dcpu_col]='X'
                    print('Disparo acertado vuelve a disparar')
                    print('\nTABLERO DE ATAQUE DE JUGADOR2(CPU)\n',tablero4,'\n\nTABLERO DEFENSA JUGADOR2(CPU)\n',tablero2)
                     
                elif tablero1[dcpu_fila,dcpu_col]==' ':
                    print('Agua!!')
                    tablero1[dcpu_fila,dcpu_col]='~'
                    tablero4[dcpu_fila,dcpu_col]='~'
                    print('\nTABLERO DE ATAQUE DE JUGADOR2(CPU)\n',tablero4,'\n\nTABLERO DEFENSA JUGADOR2(CPU)\n',tablero2)
                    break
                elif tablero1[dcpu_fila,dcpu_col]=='~':
                    print('Esas coordenadas ya las habías empleado en un disparo fallido, repite disparo ~~~~')
                elif tablero1[dcpu_fila,dcpu_col]=='X':
                    print('Esas coordenadas ya las habías empleado en un disparo acertado, repite disparo XXXX')
     
            elif (dcpu_fila>=10) or (dcpu_fila<=-1) or (dcpu_col>=10) or (dcpu_col<=-1):
                print('Las coordenadas introducidas exceden del tablero de juego, repite disparo')
                print('\nTABLERO DE ATAQUE DE JUGADOR2(CPU)\n',tablero4,'\n\nTABLERO DEFENSA JUGADOR2(CPU)\n',tablero2)
            else: 
                print('Vuelve a introducir las coordenadas de disparo')
    return 

