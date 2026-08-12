#ver si un numero es impar o par usando condicionales

#Pedir al usuario el numero a evaluar
Numero = int(input("Ingrese un numero para evaluar si es par o impar: "))

if Numero % 2 == 0:
    print("Este numero es impar")

else:
    print("Este numero es par")