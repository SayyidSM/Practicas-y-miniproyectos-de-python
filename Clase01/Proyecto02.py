#Generador de firma profesional con limpieza de datos 
print("---Generador de firmas profesionales---")

#Pedir al usuario datos para poder crear su firma y normalizar textos

Nombre_Completo = input("Ingrese su nombre completo: ").strip().title()
Carrera = input("Ingrese la carrera en la que cursa: ").strip().title()
Localidad = input("Ingrese donde radica actualmente: ").strip().title()
Correo = input("Ingrese su correo electronico: ")

#Imprimir presentacion de firma profesiona

print("------------------------")
print("Nombre: ", Nombre_Completo)
print("Estudiante en: ", Carrera)
print("Correo: ", Correo)
print("Viviendo actualmente en: ", Localidad)
print("------------------------")

