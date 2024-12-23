"""
conjunto de instrucciones agrupadas en una linea para ser invocado

def nombreFuncion(parametros):
    # bloque de codigo 

nombreFuncion(parametros)
"""

# Funcion sin parametros
def muestraNombre():
    print("Jose")
    print("Luis")
    print("Rosa")
    print("Roka")

muestraNombre()

# funcion con parametro
def saludo(nombre):
    print(f"Hola {nombre}")

saludo("jose")-.

# funcion con dos parametros
def mostrarTuNombreEdad(nombre, edad):
    print(f"Tu nombre es {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")
    else:
        print("Eres menor de edad")

nombre = str(input("Tu nombre es: "))
edad = int(input("Tu edad es: "))
mostrarTuNombreEdad(nombre, edad)