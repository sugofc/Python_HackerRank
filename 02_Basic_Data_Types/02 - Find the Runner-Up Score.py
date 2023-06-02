#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

n = int(input("Ingrese Cantidad Puntajes: "))
arr = list(map(int, input("Ingrese Puntajes separados por 1 espacio: ").split(" ")))


subc = []
for i in arr:
    if i != max(arr):
        subc.append(i)

print(int(max(subc)))