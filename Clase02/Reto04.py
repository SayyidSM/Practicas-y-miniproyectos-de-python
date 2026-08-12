#Sistema de calificaciones 

#Definimos la funcion que retorna su nota

def Evaluacion(c):
    if 100 > c >= 60:
        return "Aprobado"
    elif 60 > c >= 0:
        return "Reprobado"
    else:
        return "Ingrese un numero valido entre 0-100"

def Recomendaciones(Evaluacion):
    if estado == "Aprobado":
        return "Vas muy bien sigue asi"
    else:
        return "Sigue estudiando, pasaras"

try:
    #Pedir al usuario su calificacion
    c = int(input("Ingrese su calificacion: "))

    estado = Evaluacion(c)
    frase = Recomendaciones(estado)

    print(f"Usted esta {estado}, {frase} ")

except ValueError:
    print("Error: favor de ingresar un numero valido")