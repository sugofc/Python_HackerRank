"""
El blackjack es un juego de cartas, propio de los casinos con una barajas inglesas de 52 cartas sin los comodines, que consiste en sumar un valor lo más próximo a 21 pero sin pasarse. Gana si el jugador que se acercó más a 21, sin pasarse.

Para eso, deberá recibir las cartas del jugador hasta que diga STOP. Luego, deberá recibir las cartas de la mesa, el primer número recibido dirá la cantidad de cartas a recibir por la mesa, luego obtienes esa cantidad de cartas.

En caso de haber empate, la mesa gana.

#* Input Format
Cartas de jugador
...
Cartas de jugador
STOP
N° de Cartas de la mesa
Cartas de la mesa
...
Cartas de la mesa

#* Constraints
Cartas posibles: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

#* Output Format
Gana el jugador
Gana la mesa

#* Sample Input 0
10
11
STOP
3
10
6
4
#* Sample Output 0
Gana el jugador
#* Explanation 0
El jugador posee: 21 La mesa posee: 20 Gana el jugador

#* Sample Input 1
10
10
STOP
3
10
6
5
#* Sample Output 1
Gana la mesa
#* Explanation 1
El jugador posee: 20 La mesa posee: 21

#* Sample Input 2
10
8
STOP
4
10
6
1
6
#* Sample Output 2
Gana el jugador
#* Explanation 2
El jugador posee: 18 La mesa posee: 23 El jugador gana

#* Sample Input 3
10
8
7
STOP
3
9
8
9
#* Sample Output 3
Gana la mesa
#* Explanation 3
El judador tiene: 25 La casa tiene: 26 La mesa gana (Porque hay un empate)
"""