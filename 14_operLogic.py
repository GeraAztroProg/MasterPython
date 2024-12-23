edad_minima = 18
edad_maxima = 65
edad_real = 17

if edad_real >= edad_minima and edad_real <= edad_maxima:
    print("Esta en la edad de trabajar")
else:
    print("No esta en edad de trabajar")


print("################# ejemplo6 ##############")

pais = "alemania"

if pais == "mexico" or pais == "alemania" or pais == "colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"No es un pais de habla hispana")

print("################# ejemplo7 ##############")

pais = "colombia"

if not (pais == "mexico" or pais == "alemania" or pais == "colombia"):
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"No es un pais de habla hispana")

print("################# ejemplo8 ##############")

pais = "mexico"

if pais != "mexico" and pais != "alemania" and pais != "colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"No es un pais de habla hispana")