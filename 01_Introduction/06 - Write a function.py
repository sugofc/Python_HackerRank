#https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def is_leap(year):
    leap = False
    
    # Si el año es divisible por 4 puede ser bisiesto, a menos que...
    if year % 4 == 0:
        # Si el año es divisible por 100, NO es bisiesto, a menos que...
        if year % 100 == 0:
            # El año sea divisible por 400.
            if year % 400 == 0:
                leap = True
        # Si el año NO es divisible por 100, es bisietso.
        else:
            leap = True

    return leap

year = 1992 #int(input("Escribir año: "))
print(is_leap(year))