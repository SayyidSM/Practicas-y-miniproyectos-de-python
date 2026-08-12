#Codigo que clasifica si un numero es negativo o positivo

#Pedir al usuario el numero
n = int(input("Ingrese el numero que quiere conocer: "))
#Clasificar numero 
def num_pno():
    if n > 0:
        print("Tu numero es un numero positivo")
    elif n < 0:
        print("Tu numero es un numero negativo")
    else:
        print("Tu numero es un 0")


#Ver si el numero es impar o par

def num_poi():
    if n % 2 == 0:
        print("Su numero es un numero par")
    else: 
        print("Su numero es un numero impar")

num_pno()
num_poi()
    
