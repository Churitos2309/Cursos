
# Creando una lista (Se pueden modificar)
lista = ["Juan Ochoa", "Churitos", True, 1.75]
print (lista[1])

# Creando una tupla (No se puede modificar)
tupla = ("Juan Ochoa", "Churitos", True, 1.75)
print (tupla[1])

# Creando un conjunto (Set)
# Se puede redefinir, pero no se puede modificar con otra variable.
# En un conjunto no puede haber datos repetidos o iguales.
# No se puede llamar a sus elementos por su indice [valor indice] y no almacena datos duplicados, es buena practica para eliminar datos duplicados.
# y son datos desordenados.


conjunto = {"Juan Ochoa", "Churitos", True, 1.75}


# Creado un diccionario (dict)
# La estructura es Key: Value y separamos con comas

diccionario = {
    'nombre' : 'Juan',
    'canal' : 'Churitos',
    'esta emocionado?' : True,
    'Altura' : 1.75,
    'dato_duplicado' : 'Churitos'
}
print (diccionario['nombre'])