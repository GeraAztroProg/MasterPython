"""
funciones dentro de otra funcion
"""

def getNombre(nombre):
    texto = f"El nombre es {nombre}"
    return texto

def getApellido(apellido):
    texto2 = f"Los apellidos son {apellido}"
    return texto2

print(getNombre("Gerardo"), getApellido("Garduño Rosas"))

def imprimirTodo(nombre, apellido):
    texto3 = getNombre(nombre) + "\n" + getApellido(apellido)
    return texto3

print(imprimirTodo("Jose", "Gonzalez"))
