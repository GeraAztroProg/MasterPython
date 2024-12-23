"""

While -> controlar el contador para poder salir del bucle

contador
while condicion:
    bucle de instrucciones
    contador actualizado
"""

contador = 1

while contador <= 100:
    print(f"El contadador esta {contador}")
    contador += 1

print("####### ejemplo1 ########")

contador1 = 1
muestrame = str(0)

while contador1 <= 100:
    muestrame = muestrame + ", " + str(contador1)
    contador1 = contador1 + 1

print(muestrame)

print("####### ejemplo2 ########")

numero  = int(input("Que tabla requieres \n"))

if numero < 1:
    numero = 1

print("###### tabla del usuarios #########")

contador2 = 1
while contador2 <= 10:
    print(f"{numero} x {contador2} = {numero * contador2} ")
    contador2 += 1
