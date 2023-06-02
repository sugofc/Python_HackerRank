#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

lista = [] # Guarda el Nombre y Score
scr = [] # Solo guarda el indice de Score
seg = [] # Guarda el Segundo valor mas alto

for i in range(3): #(int(input("Cantidad: "))):
    name = ["A","B","C"] #input("Nombre: ")
    score = [20, 30, 40] #float(input("Score: "))
    #lista.append([])
    #lista[i] = [name, score]
    src = min(score) #scr.append(lista[i][1])

for e in range(len(lista)-1):
    if (lista[e][1] != min(scr)):
        seg.append(lista[e][1])

for j in range(len(seg)):
    if (lista[j][1] == min(seg)):
        print(lista[j])

if len(lista) == 1:
    print(lista[0])