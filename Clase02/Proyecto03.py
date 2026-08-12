# Proyecto 3: Filtro de registro

# Pide:
# edad
# nombre
# país

# Reglas:
# menor de 18 → acceso denegado
# si no es de México → acceso restringido
# si todo correcto → registro exitoso

#Pedimos al usuario datos necesarios
def datos():
    nombre = input("Ingresa tu nombre completo iniciando por apellidos: ").strip().title()
    edad = int(input("Ingresa tu edad: "))
    pais = input("Ingresa el pais donde vives: ").title().strip()
    return nombre,edad,pais 

#Organizams el nombre 
def organizar_nombre(nombre):
    partes = nombre.split()
    primer_nombre = partes[-1]
    primer_apellido = partes[1]
    return primer_apellido,primer_nombre

#asignamos los datos a variables
nombre, edad, pais = datos()
primer_apellido, primer_nombre = organizar_nombre(nombre)

#Oragnizamos datos con mensaje de bienvenida
print(f"Bienvenido señor {primer_nombre}_{primer_apellido}")

if edad >= 18 and pais == 'Mexico':
    print("Usted ha sido asigando a lo mas cabron del mundo")
else:
    print("Lo sentimos, no cumples con los requisitos para entrar a este sitio")



