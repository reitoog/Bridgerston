
<img style="float: left;" src=".\Fotobarcos.png"">

## Nombre del desarrollador:

### **Reiche Javier Torao Ogayar**


## Introducción
En este ejercicio vas a crear tu propio juego de **Hundir la flota** en Python. Para el desarrollo del programa necesitarás conocimientos de la librería `numpy`, módulos, bucles, funciones y colecciones de Python. Se recomienda desarrollar el programa en un IDE como Pycharm, Visual Studio Code o Spyder. **Por lo que la entrega deberá constar de uno o varios scripts de Python (archivos .py), los que necesite el alumno**.

## ¿Cómo funciona el juego?
Vamos a realizar una versión que tiene algunas particularidades respecto al juego original, de manera que sea más sencillo el desarrollo. Veamos cómo funciona:

1. Hay dos jugadores: la máquina y tú
2. Un **tablero de 10 x 10** posiciones donde irán los barcos.
3. Lo primero que se hace es colocar los barcos. Para este juego **los barcos se colocan de manera aleatoria. Ahora bien, puedes empezar colocando los barcos en unas posiciones fijas, que no cambien con cada partida, y después implementarlo aleatoriamente, ya que es más complejo. Los barcos son:**
    * 4 barcos de 1 posición de eslora
    * 3 barcos de 2 posiciones de eslora
    * 2 barcos de 3 posiciones de eslora
    * 1 barco de 4 posiciones de eslora

4. Tanto la máquina como tú tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.
5. Funciona por turnos y empiezas tú.
6. En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la máquina.
7. En los turnos de la máquina, si acierta, también le vuelve a tocar. ¿Dónde dispara la máquina? A un punto aleatorio en tu tablero.
8. Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.
9. Por norma del juego no puede haber espacios entre barcos. Ignora esta norma


## Librerías empleadas 
   numpy

## Scripts empleados 
    Los scripts empleados son los siguientes
        **config**: donde se han puesto las variables globales empleadas 
        **The_body**: que es el script principal 
        **Disparo_jug1**: Donde se muestra la lógica aplicada en la realizacion de cada uno de los disparo efectuados por el jugador 1  y como afecta a cada uno de los tableros involucrados
        **Disparo_jug2**: Donde se muestra la lógica aplicada en la realizacion de cada uno de los disparo efectuados por el jugador 2  y como afecta a cada uno de los tableros involucrados
        **Marcador**: Regula el tanteo del juego y cuando este se acaba porque uno de los 2 jugadores ha ganado
        **Posicionar_barcos_tableros1_2**: En este script se describe la manera elegida para posicionar de manera aleatoria los barcos de jugador 1 y jugador 2

