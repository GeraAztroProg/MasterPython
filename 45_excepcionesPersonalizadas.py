"""
Excepciones personalizadas 
"""
nombre = input("Introduce el nombre")
edad = int(input("Introduce la edad: "))

try:
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al master en python {nombre}")
except ValueError:
    print("introduce los datos correctamente")
except Exception as e:
    print("Existe un error", e)