#Registro simple de estudiante
print("---REGISTRO DE ESTUDIANTES---")

#Pedir al alumno datos 
Nombre_Completo = input("Ingrese su nombre completo: ").strip().title()
Edad = int(input("Ingresa tu edad: "))
Escuela = input("Escuela de procedencia: ").upper()
Carrera = input("Ingrese la carrera en la que cursa: ").strip().title()
Localidad = input("Ingrese donde radica actualmente: ").strip().title()
Correo = input("Ingrese su correo electronico: ").lower()

#Crear registro de estudiante a apartir de los datos mostrados 
print("\nREGISTRO EXITOSO DE ESTUDIANTE: ")
print("Nombre:",Nombre_Completo)
print("Edad:", Edad)
print("Escuela de procedencia:", Escuela)
print("Carrera:", Carrera)
print("Localidad:", Localidad)
print("Correo de contacto:", Correo)
