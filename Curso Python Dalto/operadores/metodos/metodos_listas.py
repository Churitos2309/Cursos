# LIST = Crea una lista 

# LEN = Cuenta la cantidad de elementos dentro de una lista 

# APPEND = Agrega un elemento a la lista 
# INSERT = Agrega un elemento a la lista en el indice especificado 
# EXTEND = Agrega varios elementos a la lista 

# POP = Elimina un elemento de una lista, pide indice y devuelve el valor 
# REMOVE = Remueve un elemento de la lista, pide valor 
# CLEAR = Elimina todos los elementos de una lista 

# SORT = Ordena una lista de forma ascendente a descendente
# REVERSE = Invierte los elementeos de una lista.





# Creando una lista con list()
lista = list([43 , 23 , 51 , True])

# Devuelve la cantidad de elementos dentro de una lista 
cantidad_elementos =len(lista)

# Agregando un elemento a la lista 
lista.append(33)

# Agregamos un elemento a la lista en un indice especifico
lista.insert(2, 33)

# Agregando varios elementos a la lista 
lista.extend([False,2023])

# Elimiando un elemento de la lista (Por si indice)
# Para eliminar siempre el ultimo elemento de la lista en su especificacion de indice
# Incluimos el -1 y asi sucesivamente, porque lo que hace es eliminar el ultimo con el -1
lista.pop (0) # -1 para eliminar el ultimo -2 para eliminar el ante ultimo y asi suscesivamente 



# Removiendo un elemento de la lista por su valor si encuentra el valor de especificado lo eliminara
# si no encuentra nada, nos lanzara una excepcion.

# lista.remove("x mano no me podes eliminar porque no estoy dentro de tu lista")


# Eliminando todos los elementos de la lista
# lista.clear()


# Ordenando la lista (Si usamos el parametro reverse = True lo ordenara el reversa)
# hay que tener en cuentra que este parametro solo se puede usar si la lista no tiene parametros de texto 
lista.sort()

# Invirtiendo los de una lista 
# Puede estar ordenada o no, solo revertira todo lo que hay dentro de la lista 

lista.reverse()

print (lista)