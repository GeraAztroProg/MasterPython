"""
Multiples errores 
"""
try:
    numero = int(input("Dime el numero para elevar al cuadrado: "))

    print("El cuadrado es " + str(numero * numero))
except TypeError:
    print("Debes convertir las cadenas a enteros en el codigo ")
except ValueError:
    print("Introduce un numero correcto")
#Permite mandar el mensaje a partir del error y saber 
#cual es.
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error", type(e) __name__)