#Detector de casos extraños

#Pedir al usuario su nombre"
nombre = input("ingrese su nombre porfavor:").strip().title()

#Verificador de que tan real es su nombre
if nombre == "":
    print("Ingresa un nombre valido:")
    
else:
    print("Su nombre es",nombre)