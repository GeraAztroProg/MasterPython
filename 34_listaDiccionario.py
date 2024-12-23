contactos = [
    {
        "nombre":"gerardo",
        "email": "gerar@gmail.com"
    },
    {
        "nombre": "rosa",
        "email": "rosa12@gmail"
    },
    {
        "nombre": "jose",
        "email": "jose@gmail.com"
    }
]

print(contactos)

# acceder a un valor 
print(contactos[0]["nombre"])

# modificar un valor
contactos[0]["nombre"] = "Gerardito"
print(contactos)

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email contacto: {contacto['email']}")
    print("----------------------------------")