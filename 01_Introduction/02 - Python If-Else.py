#https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true

n = 3 #int(input("Numero: "))
    
# Si "n" es impar  
if n%2 != 0:
    print("Weird")
# si "n" es par y está en el rango inclusivo de 2 a 5
elif n % 2 == 0 and n >= 2 and n <= 5:
    print("Not Weird")
# si "n" es par y está en el rango inclusivo de 6 a 20
elif n % 2 == 0 and n >= 6 and n <= 20:
    print("Weird")
# si "n" es par y es mayor a 20
else:
    print("Not Weird")