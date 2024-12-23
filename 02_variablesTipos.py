"""
Una variable es un contenedor de informacion que dentro guardara un dato,
se puede crear muchas variables y que cada una tenga un dato distinto
"""
# asignando un valor
texto = "Master en Python"
texto2 = "con Gerardo Garduno"
numero = 65
decimal = 7.6

print(texto)
print(texto2)
print(numero)
print(decimal)

print("--------------------------------")

# cambiando el valor del asignado
numero = 767
decimal = 8.9
print(numero)
print(decimal)


print("--------------------------------")

nombre = "Gerardo"
apellido = "Garduno"

print(nombre + " " +apellido)
print(f"{nombre} {apellido}")
print("Mi nombre {} {}".format(nombre, apellido))
print(nombre, apellido) # variables por argumentos 