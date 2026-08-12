#Proyecto CV 
##Crear un programa que:
# reciba datos del candidato
# valide información
# tome decisiones
# responda dinámicamente

##Debe pedir:
# nombre completo
# edad
# experiencia en años
# lenguaje favorito

#Diccionarios de lenguajes
lenguajes = {'Python','C','Java','Javascript','Sql' }


#Pedir datos al usuario 
nombre = input("Ingresa tu nombre: ").strip().title()
apellido = input("Ingresa tu apellido: ").strip().title()
edad = int(input("Ingresa tu edad: "))
sexo = input("Ingresa tu sexo H o M: ")
experiencia = int(input("Ingresa tu experiencia laboral en años: "))
lenguaje_favorito = input("Cual es tu lenguaje favorito: ").strip().title()

print("\n")

#FILTROS DE VALIDACION
if nombre == 'Johann':
    print("===Bienvenido de nuevo administrador===")
elif nombre == 'Eliel':
    print("Bienvenido Chacatito")
else:
    print(f"Eres un usuario cualquiera bienvenido {nombre}")

if edad >= 18 and nombre == 'Johann':
    print("Eres admnistrador y tienes acceso a todo el contenido")
elif edad >= 18:
    print("Eres mayor de edad y un usuario cualquiera")
else:
    print("No eres mayor de edad")

try: 
    if 2 < experiencia <= 5:
        print("Seras asignado al grupo Junior")
    elif 5 < experiencia <= 10:
        print("Seras asignado al grupo Senior")
    else:
        print("No puedes ser asignado a ningun grupo")
except ValueError:
    print("ERROR: Ingrese un valor valido en su experiencia validar 1-10")

if lenguaje_favorito in lenguajes:
    print("Cumples con al menos 1 lenguaje requerido para el puesto")
else:
    print("Manejas lenguajes que no requerimos lo sentimos")


if edad >= 18 and 0 < experiencia <= 10 and nombre != 'Johann' and lenguaje_favorito in lenguajes :
    print("Usted ha sido elegido para este puesto de trabajo !FELICIDADES¡")
elif nombre == 'Johann':
    print("Tu no necesitas trabajo, eres el dueño")
else: 
    print("Usted no es apto para este puesto de trabajo aunque cumpla algunos requisitos")








