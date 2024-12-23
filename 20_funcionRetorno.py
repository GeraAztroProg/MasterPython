"""
Generar una calculadora para devolver un string

return -> tendra un valor de retorno
"""

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

dato = saludame("Gerardo")
print(dato)


#Calculadora
def calculadora(num1, num2, basicas = False):
    suma = num1 + num2
    resta = num1 - num2
    mul = num1 * num2
    div = num1 / num2

    cadena = ""

    cadena += "Suma: " + str(suma) + "\n" + "Resta: " + str(resta) + "\n"
    cadena += "Multiplicacion: " + str(mul) + "\n" + "Division: " + str(div) + "\n"

    return cadena

resultado = calculadora(5, 3)
print(resultado)