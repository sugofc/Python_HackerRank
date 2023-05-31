#https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

def cadena(n):
    text = str()
    for i in range(1,n+1):
        text += "".join(str(i))
    return text

n = 10 #int(input("Escriba un numero: "))

print(cadena(n))