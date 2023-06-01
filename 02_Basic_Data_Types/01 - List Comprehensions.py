#https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

x = 1 #int(input())
y = 1 #int(input())
z = 1 #int(input())
n = 2 #int(input())


# perm = [[x2,y2, z2] for x2 in range(x+1) for y2 in range(y+1) for z2 in range(z+1) if x2+y2+z2 != n]
# print(perm)



lista = []
p = 0
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                lista.append([])
                lista[p] = [i, j, k]
                p += 1

print(lista)