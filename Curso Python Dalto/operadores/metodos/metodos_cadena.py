# Cual es la estructura para utilizar estos metodos? 
# La estructura es la siguiente 
# DATO . METODO ()



# DIR = devulve una lista de atributos validos del objeto pasado.

# UPPER = Convierte mayusculas 
# LOWER = Convierte a minusculas
# CAPITALIZE = Primera en mayusculas 

# FIND = Metodo encuentra la primera aparicion del valor especificado, sino devuelve 1
# INDEX = Metodo encuentra la primera aparicion del valor especificado, sino devuelve una excepcion.

# ISNUMERIC = Si es numerico devuelve True 
# ISALPHA = Si es alpha numerico devuelve True 

# COUNT = Devuelve el numero de ocurriencias de una subcadena en la cadena dada
# LEN = Encuentra los caracteres de la cadena 

# ENDSWITH = Verifica si una cadena empieza con:
# STARSWITH = Verifica si una cadena termina con: 

# REPLACE = Reemplaza el valor por otro 
# SPLIT = separa el paremetro dado


cadena1 = "Hola Soy Juan"
cadena2 = "bien venido maquina"


# Convierte a mayusculas 
mayus = cadena1.upper()

# Convierte a minusculas 
minusc = cadena1.lower()

# Convierte la primera letra a mayusculas
# lo que hace este metodo es convertir todo a minusculas y luego la primer letra la convierte a mayusculas
primera_letra_mayus = cadena1.capitalize()

# Buscamos una cadena en otra cadena 
# Lo que retorna el metodo FIND es una posicion de donde encontro dicha palabra, o lo que decidimos buscar.
# de 0 al que se le ofrezca 
# Y cuando no se encuentra coincidencias retornara -1, ya que no existe dentro del objeto
busqueda_find = cadena1.find("Hola")


# Buscamos una cadena dentro de otra cadena, si no hay coincidencia lanza una excepcion
busqueda_index = cadena1.index("J")

# Si es numero se devolvera True, sino devolvemos false 
es_numerico = cadena1.isnumeric()

# Si es alpha numerico devolvemos True, se lo contrario devolvemos False.
# Los caracteres alpha numericos solo son desde la A hasta la Z, por ende
# los espacios no son alpha numerico, por lo cual si usted quiere que sea alpha numerico 
# tendra que eliminar los espacios y todos los caracteres especiales.
es_alpha_numerico = cadena1.isalpha()


# Contamos coincidencias de una cadena dentro de otra cadenam devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")


# Cuantos caracteres tiene una cadena 
# len es una funcion no es un metodo    
contar_caracteres = len(cadena1)

# Verificamos si una cadena empieza por otra cadena dada si es asi devuelve True 
empieza_con = cadena1.startswith("H")

# Verificamos si una cadena terina por otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("H")

# Reemplaza una cadena dada por otra cadena dada
# Si encuentra coincidencias las va a cambiar por lo estipulado anteriormente en el la cadena
# Si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace("Juan" , "Ochoa que tal estas?")

# Separar cadenas con la cadena que le pasemos 
cadena_separada = cadena1.split(" ")

print (cadena_separada)
