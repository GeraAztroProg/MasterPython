"""
#FOR

FOR VARIABLE IN ELEMENTO_ITERABLE (lista, rango, etc) 
    bloque de instrucciones 

"""
contador = 0
resultado = 0

for contador in range(0, 12):
    print("voy por el " + str(contador))
    resultado += contador

print("El resultado de la suma es " + str(resultado))


print("######### ejemplo ############")

numero = int(input("Ingresa el numero de la tabla \n"))

if numero < 1:
    numero = 1

print(f"##### tabla de multiplicar del numero {numero} ####")

for numero_tabla in range(1, 11):
    if numero == 45:
        print("No se pueden mostrar numeros prohibidos")
        break
    
    print(f" {numero} x {numero_tabla} = {numero*numero_tabla}")
else:
    print("Tabla finalizada")