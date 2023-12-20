#Disparo_jug1-->(Este es el bueno NO el de las funciones recursivas)
#A esta función le pasas el tablero2 que es donde estan posicionados los barcos de la máquina, y como resultado obtienes si tu disparo ha sido certero o no 
#Para mostrar los resultados del ataque de jugador uno mostramos el estado de tablero 3 que es donde el jugador1(la persona)visualiza su ataque.
#Para ver como le va, en defensa, tienes que imprimir por pantalla el tablero 1

def disparo_jug1(tablero2,tablero3,tablero1):  #tablero1
    """
    Disparo_jug1-->A esta función le pasas el "tablero2" que es donde estan posicionados los barcos de la máquina y 
                   "tablero3" que es donde se ven los resultado de ataque del jugador 1. 
                   Como resultado obtienes el  disparo  del jugador 1(persona), si ha sido certero o no, y te muestra un tablero(tablero3) con 
                   resultados de ataque de jugador1 hasta el momento.      
    """
    import numpy as np
    import config
    from numpy import random
    #global salida
    while True:
            
            salidah=str(input('Quieres salir del juego (S/N)?'))
            if salidah.upper()=='S':
                print("""
                        
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   

                      """)
                #https://patorjk.com/software/taag/#p=testall&v=2&f=3D%20Diagonal&t=Game%20Over
                config.salida=True
                break
            else:
                shoot=str(input('Dime las COORDENADAS DEL PUNTO al que quieres disparar.\nEl FORMATO con el que tienes que introducir los datos presenta el siguiente aspecto 8.1\nPARA-->"Fila 8" "Columna 1"\nBUENA SUERTE!!!! :P    '))
                disp_fila=int(shoot.split('.')[0])
                disp_col=int(shoot.split('.')[1])
                if (0<=disp_fila) and (0<=disp_col)and (disp_fila<=9) and (disp_col<=9):
                    if tablero2[disp_fila,disp_col]=='O':
                        tablero2[disp_fila,disp_col]='X'
                        tablero3[disp_fila,disp_col]='X'
                        print('Disparo acertado vuelve a disparar')
                        print('\nTABLERO DE ATAQUE DE JUGADOR1\n', tablero3,'\n\nTABLERO DEFENSA JUGADOR1\n',tablero1)  #linea entera nueva
                    elif tablero2[disp_fila,disp_col]==' ':
                        print('Agua!!')
                        tablero2[disp_fila,disp_col]='~'
                        tablero3[disp_fila,disp_col]='~'
                        print('\nTABLERO DE ATAQUE DE JUGADOR1\n', tablero3,'\n\nTABLERO DEFENSA JUGADOR1\n',tablero1)  #linea entera nueva
                        break
                    elif tablero2[disp_fila,disp_col]=='~':
                        print('Esas coordenadas ya las habías empleado en un disparo fallido, repite disparo ~~~~')
                    elif tablero2[disp_fila,disp_col]=='X':
                        print('Esas coordenadas ya las habías empleado en un disparo acertado, repite disparo XXXX')
     
                elif (disp_fila>=10) or (disp_fila<=-1) or (disp_col>=10) or (disp_col<=-1):
                    print('Las coordenadas intoducidas exceden del tablero de juego, repite disparo')
                    print('\nTABLERO DE ATAQUE DE JUGADOR1\n', tablero3,'\n\nTABLERO DEFENSA JUGADOR1\n',tablero1) #,'\t\t\t',tablero1) #linea entera nueva
                else: 
                    print('Vuelve a introducir las coordenadas de disparo')   
    return 