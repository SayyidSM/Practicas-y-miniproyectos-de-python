
#Practicamos condicionales
#Pedir al usuario su edad
Edad = int(input("Ingresa tu edad: "))

#Evaluamos 
if Edad >=18:
    print("Eres un mayor de edad muy prro")

else:
    print("Eres un menor de edad, no puedes entrar a este sitio")

#tambien asignamos casa como en harry potter

nombre = input("Ingresa solo tu nombre: ").strip().title()

Griffyndor = {"Harry", "Ron", "Hermanione"}
Slythering= {"Draco", "Snape"}

if nombre in Griffyndor:
    casa = "Griffyndor"
elif nombre in Slythering:
    casa = "Slythering"
else:
    casa = "Ravenclaw"
    
print(f"Tu casa es {casa}")