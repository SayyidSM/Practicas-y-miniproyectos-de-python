#Normalizador de nombres con usuario sugerido 
print("-----NORMALIZADOR DE NOMBRES------")
#Pedir al usuario su nombre y normalizarlo 

Ncompleto = input("Ingrese su nombre completo: ").strip().title()

print(f"Su nombre completo es {Ncompleto}")
print("Esta prueba es:", Ncompleto)

nombre, apellido = Ncompleto.split()

print(f"Su nombre es {nombre} y su apellido es {apellido}")

#Hacer nueva variable usuario y darle un usuario sugerido 

Usuario = nombre.upper() + '_' + apellido.lower()
print("Sugerimos usar el siguiente usuario: ", Usuario)


#Dar las iniciales del nombre 

print("Sus iniciales son: ", nombre[0] + '.' + apellido[0])