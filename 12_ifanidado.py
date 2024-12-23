nombre = "gerardo garduno"
ciudad = 'mexico'
conteninte = 'americano'
edad = 37
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f'{nombre} es mayor de edad')

    if conteninte != 'americano':
        print('el usuario no es americano')

        if ciudad == 'mexico':
            print('el usuario es mexicano')
        else:
            print('el usuario no es mexicano')
    else:
        print('el usuario es americano')
else:
    print(f'{nombre} NO ES MAYOR DE EDAD')