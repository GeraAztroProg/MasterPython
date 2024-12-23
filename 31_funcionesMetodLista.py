cantantes = [
    "Jenifer Lopez", "Cartel de santa", "C-kan", "2pac" ]

numeros = [ 1, 2, 38, 41, 52, 6, 7, 15, 15 ]

print(numeros)
# Metodos -> Ordenar los numeros
numeros.sort()
print(numeros)

# agregar un elemento
cantantes.append("natos y kraos")
print(cantantes)

# agregar en el indice x
cantantes.insert(2, "david bisbal")
print(cantantes)

# eliminar elementos de una lista por indez
cantantes.pop(0)
print(cantantes)

# eliminar elmento de una lista por nombre
cantantes.remove("2pac")
print(cantantes)

# voltear la lista 
print(numeros)
numeros.reverse()
print(numeros)

# buscar un elemento dentro de la lista 
print("natos y kraos" in cantantes)

# contar elementos
print(len(numeros))

# veces aparace elementos en lista
print(numeros.count(15))

# conseguir el indice
print(cantantes.index('C-kan'))

# unir dos listas 
cantantes.extend(numeros)
print(cantantes)