# Definiendo variables

a = 2
b = 3
c = a + b
print (c)

# Definiendo una variable con camelCase
#Camel case es mas usado en JavaScript 

nombreCompletoDeTuTioMaster = "tio completo master"

#Definiendo una variable con snake_case
nombre_completo_de_tu_tio_master = "tio completo master"

# Tipos para concatenar
# 1) Concatenar con el signo mas + Despues de cada cierre de comillas
 
nombre = "Juan"
bienvenida = "Hola " + nombre + " ¿Como estas?"
print (bienvenida)


#2) Concatenar con el "f" antes de el String y las comillas, y se pone unas llaves donde se quiere que se vea lo que queremos mostrar
#2.1) Concatenar con f-string

Apellido = "Ochoa"
Consulta = f"Tu apellido es {Apellido} Es correcto?"
print (Consulta)

# Operadores de pertenencia (in / not in)
# Esto lo que hace es mirar si lo que esta en comillas esta dentro de consulta, que es la consulta en la que deseamos averiguar si esta o no el algo.
# los operadores de pertenencia solo rebotan un True o un False

print ("Eduardo" in Consulta) # Esta Eduardo dentro de Consulta?
print ("Juan" not in Consulta) # No esta Juan dentro de Consulta?