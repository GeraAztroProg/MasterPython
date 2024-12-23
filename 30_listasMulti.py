"""
Creacion de listas multimencionales
"""
contactos =[
    ["antonio", "antonio@gmail.com"],
    ["gerardo", "gerar@gmail.com"],
    ["jose", "jose23@gmail.com"]
]

print(contactos)
print("-------------")
print(contactos[2]) # sacar un valor de lista normal
print("--------------")
print(contactos[2][1]) # sacar el correo


print("---------------")
for contacto in contactos:
    for elemento in contacto:
        print(elemento)