"""
Piedra, papel o tijeras es un juego infantil, un juego de manos en el que existen tres elementos: la piedra que vence a la tijera rompiéndola, la tijera que vence al papel cortándolo y el papel que vence a la piedra envolviéndola, dando lugar a un círculo o ciclo cerrado, que caracteriza al juego. Se utiliza con mucha frecuencia para decidir quién de dos personas hará algo, tal y como se hace a veces usando una moneda, o para dirimir algún asunto.

#* Input Format
Jugada del jugador 1 Jugada del jugador 2

#* Constraints
Solo ingresaran los siguientes inputs:
Piedra
Papel
Tijeras

#* Output Format
Resultados:
Gano el jugador 1
Gano el jugador 2
Empate

#* Sample Input 0
Piedra
Tijeras
#*Sample Output 0
Gano el jugador 1

#* Sample Input 1
Papel
Piedra
#* Sample Output 1
Gano el jugador 1

#* Sample Input 2
Tijeras
Tijeras
#* Sample Output 2
Empate
"""

j1 = input("Jugada del jugador 1:")
j2 = input("Jugada del jugador 2:")

if j1 == "Piedra" or j1 == "Papel" or j1 == "Tijeras":
    if j2 == "Piedra" or j2 == "Papel" or j2 == "Tijeras":
        if j1 == j2:
            print(f"{j1}")
            print(f"{j2}")
            print("Empate")
        elif (j1 == "Piedra" and j2 == "Tijeras") or (j1 == "Papel" and j2 == "Piedra") or (j1 == "Tijeras" and j2 == "Papel"):
                print(f"{j1}")
                print(f"{j2}")
                print("Gano el jugador 1")
        else:
            print(f"{j1}")
            print(f"{j2}")
            print("Gano el jugador 2")
    else:
        print("Valor no permitido")
else:
    print("Valor no permitido")