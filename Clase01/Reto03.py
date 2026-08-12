#SEPARAR NOMBRES USANDO SPLIT 

#pedir al usuario un nombre con un apellido 
Ncompleto = input("ingrese su nombre y apellido: ").strip().title()

#separar nombre y apellido en variables independientes 
nombre, apellido = Ncompleto.split() 

#decirle al usuario que su nombre es x y su apellido y 
print(f"Su nombre es {nombre} y su apellido es {apellido}")

#prueba usuario sugerido 
usuario = nombre.upper() + '_'+ apellido.lower()
print(f"Su usuario sugerido es: {usuario}")