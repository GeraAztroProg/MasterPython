
"""
Errores-> Controlar los errores que salen dentro 
de un algoritmo cuando este tenga problemas
"""

#Capturar excepciones y manejar errores en codigos
# suceptibles a fallos y errores


try:
    nombre = input("Cual es tu nombre: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre de usuarios es " + nombre
            
    print(nombre_usuario)
except:
    print("Ha ocurrido un error mete bien el nombre")
else:
    print("Todo ha funcionado correctamente")
finally:
    #DETECTAR CUANDO HAN TERMINADO TODOS LOS CASOS 
    print("Fin de la iteracion")