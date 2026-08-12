#Menu interactivo 
# 1. Saludar
# 2. Mostrar usuario
# 3. Salir

#Pedir datos al usuario 
def datos_usuario():
    nombre = input("Ingresa tu nombre completo: ").strip().title()
    edad = int(input("Ingresa tu edad: "))
    sexo = input("Ingresa tu sexo H o M: ").strip().upper()
    return nombre,edad,sexo

#separador de nombre
def separador(nombre):
    partes = nombre.split()
    primer_nombre = partes[0]
    primer_apellido = partes[-2]
    return primer_nombre,primer_apellido

# Ejecutar las funciones y guardar los resultados
nombre, edad, sexo = datos_usuario()
primer_nombre, primer_apellido = separador(nombre)

#Fabricar el saludo 
def saludo():
    print(f"Bienvenido {primer_nombre}, veo que tienes {edad} y eres {sexo}.\nEste es un saludo de prueba para ver como funciona esto")

#Creamos menu interactivo 
print("="*30)
print("\n1.Saludo\n2.Mostrar Usuario\n3.Salir ")
opcion = int(input("Ingresa la opcion deseada: "))

if opcion == 1:
    saludo()
elif opcion == 2:
    print(f"Su usuario es: {primer_nombre}_{primer_apellido}")
elif opcion == 3:
    print("Gracias por usar este programa")
else:
    print("No elegiste una opcion valida, por lo tanto este programa se cerro")

print("="*30)





