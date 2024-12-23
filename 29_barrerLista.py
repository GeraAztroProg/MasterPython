"""
Recorrer elemenots de lista 
"""
numeros = [12,15,16]

#agregar un numero
numero_nuevo = " "
while numero_nuevo != 0 :
    numero_nuevo = int(input("Introduce un numero nuevo \n"))
    
    if numero_nuevo != 0:
        numeros.append(numero_nuevo)

for numero in numeros:
    print(f"{numeros.index(numero) + 1}. {numero}")