"""
Parametros opcionales 
"""

#Dar un valor por defecto para que sea opcional
def getEmpoleado(nombre, dni = False):
    print("Empleado")

    print(f"Nombre: {nombre}")

    if dni == False:
        print(f"DNI: {dni}")

getEmpoleado("Gerardo", "154655626")