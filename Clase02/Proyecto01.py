#Verificador de usuarios
#El programa debe:
# pedir nombre
# pedir contraseña
# validar ambos 
# o en todo caso Usuario no encontrado

#Pedir nombre al usuario
nombre = input("Ingrese su nombre: ").strip().title()

#Separamos nombre 
partes = nombre.split()

primer_nombre=partes[0]
primer_apellido = partes[-2]

#Pedir Contraseña
password = input("Ingrese su contraseña: ")

#Validamos entradas
if not nombre or not password:
    print("Favor de ingresar un dato valido")

elif primer_nombre == "Johann" and password == "1234":
    print(f"Bienvenido {primer_nombre}")

else:
    print("Usuario no encontrado favor de verificar datos")
