#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

lista = [] # Guarda el Nombre y Score
scr = [] # Solo guarda el indice de Score
seg = [] # Guarda el Segundo valor mas alto

lista2 = []
scr2 = []
score2 = []

lista3 = []
n = 0
e = 0

for i in range(5):
    name = ["Harry","Berry","Tina","Akriti","Harsh"]
    score = [37.21, 37.21, 37.2, 41, 39]
    lista = [["Harry",37.21],["Berry",37.21],["Tina",37.2],["Aktiri",41],["Harsh",39]]
    scr = score

# for i in range(int(input("Cantidad: "))):
#     name = input("Nombre: ")
#     score = float(input("Score: "))
#     lista.append([])
#     lista[i] = [name,score]
#     scr.append(lista[i][1])

for e in lista:
    if e[1] != min(scr):
        lista2.append([])
        lista2[n] = e
        score2.append(e[1])
        n += 1

for k in lista2:
    if k[1] == min(score2):
        lista3.append([k[0]])
        lista3.sort()

print(lista3)
