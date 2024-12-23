# modulo de fechas 
import datetime

# uso de metodos para la fecha actual
print(datetime.date.today())

#Impresion de una fecha completa
fechaCompleta = datetime.datetime.now()
print(fechaCompleta)

# puedo mostrar otros valores por ejemplo el año
print(fechaCompleta.year)
print(fechaCompleta.month)
print(fechaCompleta.day)

#Se puede personalizar 
# %d -> dia 
# %m -> mes
# %y -> año
# %H -> horas %M -> minutos %S -> SEGUNDOS
fechaPersonalizada = fechaCompleta.strftime("%d/%m/%Y --- %H:%M:%S")
print("Mi fecha personalizada " + fechaPersonalizada)

#toda la fecha completa en tiempo en UNIX
print(datetime.datetime.now().timestamp())

#SACAR EL TIEMPO 
print(datetime.datetime.now().time())


# MODULO DE MATEMATICAS 
import math

#Raiz cuadrada
print("La raiz cuadrada ", math.sqrt(10))

#Sacar el numero pi
print("pi vale", float(math.pi))

#redondear hacia arriba
print("Redondear ", math.ceil(6.54545185418518))

#redondear hacia abajo
print("Redondear ", math.floor(6.54545185418518))

import random

# un numero aleatorio
print("Numero aleatorio ", random.randint(15,67))

