#Crear un clasificador de administrador y usuario comun

#Pedir el nombre para poder clasificar quien es

nombre = input("Ingrese su nombre completo iniciando por apellido: ").strip().title()

#Separamos nombre
partes = nombre.split()
primer_nombre = partes[-2]
primer_apellido = partes [0]

#Crear usuario
usuario = primer_nombre.title() + '_'+ primer_apellido.title()

if usuario == "Johann_Sanchez":
    print(f"Bienvenido de nuevo administrador {usuario}")
else: 
    print(f"Bienvenido usuario, tu nombre de pila es {usuario}")

