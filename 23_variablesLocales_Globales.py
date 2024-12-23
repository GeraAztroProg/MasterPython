"""
VARIABLES 
-> LOCALES : DEFINE DENTRO DE LA FUNCION 
-> GLOBAL : FUERA DE LA FUNCION Y ESTAN DISPONIBLES EN TODO

"""

# variable global 
frase = "Ni los genios son tan genis"
print(frase)

def holaMundo():
    # variable local
    frase = "hola mundo"
    print("Dentro de la funcion")
    print(frase)

    year = 2024
    print(year)

    global web
    web = "hhhhhhhh"

holaMundo()
# print(year) // no existe fuera ..

web = " ......." 
print(web)