"""
Algunas funciones predefinidas por el lenguaje
"""

nombre = "Gerardo"

#Imprimir por pantalla 
print(nombre)

# saber el tipo 
print(type(nombre))

# tipado de la variable 
comprobar = isinstance(nombre, int)
if comprobar:
    print(comprobar)
else:
    print("No es una cadena")

# limpiar espacios de un string
frase = "             hoola           "
print(frase.strip()) # limpiar variables 

#eliminar variables 
year = 2000
print(year)
del year # borrar variable

# comprobaciones si son variables
texto = "    ff   "
if len(texto) <= 0: # tamaño del texto
    print("La variable esta vacia")
else:
    print("La variable tiene contenido", len(texto))

# caracteres dentro de un string
frase = "La vida es bella"
print(frase.find("vida")) 

# remplazar palabras en un string
frase2 = frase.replace("vida", "muerte")
print(frase2)

#procesar mayusculas y minusculas
print(nombre.lower) #min
print(nombre.upper) #may