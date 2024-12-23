"""
Tabla de multiplicar con funcion
"""

def tabla(numero_tabla):
    print(f"Tabla del multiplicar del numero {numero_tabla}")

    for contador in range(0, 11):
        operacion = numero_tabla * contador
        print(f"{numero_tabla} * {contador} = {numero_tabla * contador}")

    print("\n")

tabla(2)
tabla(7)
tabla(12)

for ntabla in range(1,11):
    tabla(ntabla)
