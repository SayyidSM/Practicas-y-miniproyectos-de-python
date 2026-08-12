#Pedir al usuario nombre completo y modificarlo con mi programa
User = input("Ingrese su nombre completo:").strip().title() 

#Separar nombre en 1r y ultimo 
Separado = User.split()
Pnombre = Separado[0] 
Uapellido = Separado[-1]

#Decirle al usuario cual es su primer nombre y su ultimo apellido 
print(f"Tu primer nombre es {Pnombre} y tu ultimo apellido {Uapellido}")

#Mas bonito 
print("="*15)
print("Tu primer nombre es:",Pnombre )
print("Tu ultimo apellido es:",Uapellido)
print("="*15)



