# Funciones van arriba de todo

def mi_funcion(apellido):
    return "Hola que tal " + apellido

# las funciones simpre deven devolver un valor

def mi_segunda_funcion(nombre):
    return "Hola que tal dos " + nombre

# las variables globales se pueden acceder en cualquier lado

nombre = "Gerardo"
apellido = "Garduño"

print("Hola mundo")
print(f"Bienvenido {nombre}")

# Despues de crear las variables se puede invocar la funcion

print(mi_funcion("Lopez"))
print(mi_segunda_funcion("Jose"))
