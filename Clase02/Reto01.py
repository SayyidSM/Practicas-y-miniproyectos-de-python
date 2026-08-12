#Ingresar nombre y edad y si no es mayor de edad denegarle el acceso

#Pedir nombre 
nombre = input("Ingrese su nombre completo iniciando por apellido: ").strip().title()

#Separamos nombre
partes = nombre.split()
primer_nombre = partes[-2]
primer_apellido = partes [0]

#Creador de usuario 
usuario = primer_nombre.lower() + '_'+ primer_apellido.upper()

#Pedir edad 
edad= int(input("Ingrese su edad: "))

#Evaluar edad del consultante 
if edad >= 18:
    print(f"Bienvenido a este sistema {primer_nombre}")
    print(f"Su acceso ha sido autorizado y se le asigno el usuario de {usuario}")
else:
    print(f"Acceso denegado, favor de checar en unos años joven {primer_nombre}")

