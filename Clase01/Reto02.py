#CREAR UNA TARJETA DE PRESENTACION CON NOMBRE, APELLIDO, CIUDAD Y CARRERA

#Pedir al usuario datos para poder presentarlo
nombre = input("Ingrese su nombre: ").strip().title() 
apellido = input("Ingrese su apellido: ").strip().title()
ciudad = input("ingrese la ciudad a la que pertenece: ").strip().title()
carrera = input("ingrese la carrera que estudia: ").strip().title()

#Realizar una tarjeta de presentacion para el usuario 
print(f"Hola mi nombre es {nombre}, pertenezco a la familia {apellido} \nActualmente vivo en {ciudad} y estoy estudiando {carrera}.")