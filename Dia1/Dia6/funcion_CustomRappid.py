
#ejercicio 1 restaurante custom rappid con funciones
#crear funciones 
def mensajeBienvenida():
    print('Bienvenidos al restaurante Custom Rappid')
    print('¿Qué cantidad de hamburguesa desea ordenar?')

#crear una funcion para cada seleccion de ingrediente
def seleccionarPan():
    print('Selecciona el pan que deseas en tu hamburguesa')
    print('1. Pan de centeno --  $1000 COP')
    print('2. Pan de avena -- $1500 COP')
    ingrediente = int(input())
    
    while ingrediente not in [1, 2]:
        print('Selecciona una opción válida entre 1 y 2')
        print('1. Pan de centeno --  $1000 COP')
        print('2. Pan de avena -- $1500 COP')
        ingrediente = int(input())
    
    if ingrediente == 1:
        print('Seleccionaste pan de centeno')
        return 1000
    elif ingrediente == 2:
        print('Seleccionaste pan de avena')
        return 1500

def seleccionarCarne():
    print('Selecciona la carne que deseas en tu hamburguesa')
    print('1. Carne 250g --  $5000 COP')
    print('2. Carne 350g -- $7000 COP')
    print('3. Ninguno')
    ingrediente = int(input())
    
    while ingrediente not in [1, 2, 3]:
        print('Selecciona una opción válida entre 1, 2 o 3')
        print('1. Carne 250g --  $5000 COP')
        print('2. Carne 350g -- $7000 COP')
        print('3. Ninguno')
        ingrediente = int(input())
    
    if ingrediente == 1:
        print('Seleccionaste carne 250g')
        return 5000
    elif ingrediente == 2:
        print('Seleccionaste carne 350g')
        return 7000
    else:
        print('No incluiste carne en tu hamburguesa')
        return 0

def seleccionarPollo():
    print('Selecciona el pollo que deseas en tu hamburguesa')
    print('1. Pollo 250g --  $4500 COP')
    print('2. Pollo 350g -- $5500 COP')
    print('3. Ninguno')
    ingrediente = int(input())
    
    while ingrediente not in [1, 2, 3]:
        print('Selecciona una opción válida entre 1, 2 o 3')
        print('1. Pollo 250g --  $4500 COP')
        print('2. Pollo 350g -- $5500 COP')
        print('3. Ninguno')
        ingrediente = int(input())
    
    if ingrediente == 1:
        print('Seleccionaste pollo 250g')
        return 4500
    elif ingrediente == 2:
        print('Seleccionaste pollo 350g')
        return 5500
    else:
        print('No incluiste pollo en tu hamburguesa')
        return 0

def seleccionarPolloDesmechado():
    print('Selecciona el pollo desmechado que deseas en tu hamburguesa')
    print('1. Pollo desmechado 250g --  $6500 COP')
    print('2. Pollo desmechado 350g -- $7500 COP')
    print('3. Ninguno')
    ingrediente = int(input())
    
    while ingrediente not in [1, 2, 3]:
        print('Selecciona una opción válida entre 1, 2 o 3')
        print('1. Pollo desmechado 250g --  $6500 COP')
        print('2. Pollo desmechado 350g -- $7500 COP')
        print('3. Ninguno')
        ingrediente = int(input())
    
    if ingrediente == 1:
        print('Seleccionaste pollo desmechado 250g')
        return 6500
    elif ingrediente == 2:
        print('Seleccionaste pollo desmechado 350g')
        return 7500
    else:
        print('No incluiste pollo desmechado en tu hamburguesa')
        return 0

def seleccionarTocineta():
    print('Selecciona la lonja de tocineta que deseas en tu hamburguesa')
    print('1. Lonja de tocineta --  $1500 COP')
    print('2. Lonjas de tocineta -- $2500 COP')
    print('3. Ninguno')
    ingrediente = int(input())
    
    while ingrediente not in [1, 2, 3]:
        print('Selecciona una opción válida entre 1, 2 o 3')
        print('1. Lonja de tocineta --  $1500 COP')
        print('2. Lonjas de tocineta -- $2500 COP')
        print('3. Ninguno')
        ingrediente = int(input())
    
    if ingrediente == 1:
        print('Seleccionaste lonja de tocineta')
        return 1500
    elif ingrediente == 2:
        print('Seleccionaste lonjas de tocineta')
        return 2500
    else:
        print('No incluiste lonja de tocineta en tu hamburguesa')
        return 0

def seleccionarPapasFritas():
    print('Selecciona la porción de papas que deseas en tu hamburguesa')
    print('1. Papas francesas --  $5000 COP')
    print('2. Papas cascos -- $6000 COP')
    print('3. Ninguno')
    ingrediente = int(input())
    
    while ingrediente not in [1, 2, 3]:
        print('Selecciona una opción válida entre 1, 2 o 3')
        print('1. Papas francesas --  $5000 COP')
        print('2. Papas cascos -- $6000 COP')
        print('3. Ninguno')
        ingrediente = int(input())
    
    if ingrediente == 1:
        print('Seleccionaste papas francesas')
        return 5000
    elif ingrediente == 2:
        print('Seleccionaste papas cascos')
        return 6000
    else:
        print('No incluiste porción de papas en tu hamburguesa')
        return 0

def seleccionarBebida():
    print('Selecciona la bebida con la que deseas acompañar tu hamburguesa')
    print('1. Gaseosa --  $5000 COP')
    print('2. Cerveza club colombia -- $6000 COP')
    print('3. Naranjada -- $9000 COP')
    print('4. Ninguna')
    ingrediente = int(input())
    
    while ingrediente not in [1, 2, 3, 4]:
        print('Selecciona una opción válida entre 1, 2, 3 o 4')
        print('1. Gaseosa --  $5000 COP')
        print('2. Cerveza club colombia -- $6000 COP')
        print('3. Naranjada -- $9000 COP')
        print('4. Ninguna')
        ingrediente = int(input())
    
    if ingrediente == 1:
        print('Seleccionaste gaseosa')
        return 5000
    elif ingrediente == 2:
        print('Seleccionaste cerveza club colombia')
        return 6000
    elif ingrediente == 3:
        print('Seleccionaste Naranjada')
        return 9000
    else:
        print('No incluiste bebida para acompañar tu hamburguesa')
        return 0

#crear una funcion donde se junten todas las funciones y se pueda hacer una personalizacion de la hamburguesa
#y calcular el valor total de la hamburguesa
def funcion_CustomRappid():
    mensajeBienvenida()
    
    numbHamb = int(input())
    
    subtotal = 0
    total = 0
    
    print('A continuación personaliza tu hamburguesa escribiendo los números que corresponden a tus ingredientes favoritos')

    for i in range(numbHamb):
        precioPan = seleccionarPan()
        precioCarne = seleccionarCarne()
        precioPollo = seleccionarPollo()
        precioPollodes = seleccionarPolloDesmechado()
        precioTocineta = seleccionarTocineta()
        precioPapas = seleccionarPapasFritas()
        precioBebida = seleccionarBebida()

        subtotal += precioPan + precioCarne + precioPollo + precioPollodes + precioTocineta + precioPapas + precioBebida

    if numbHamb != 1:
        print(f'Haz completado la personalización de tus {numbHamb} hamburguesas')
        print(f'El valor a pagar es de {subtotal}')
        print(f'Valor del servicio (voluntario) --- {subtotal * 0.1}')
        total = subtotal + (subtotal * 0.1)
        print(f'Total a pagar --- ${total}')
    else:
        print("Haz completado la personalización de tu hamburguesa")
        print(f'El valor a pagar es de {subtotal}')
        print(f'Valor del servicio (voluntario) --- ${subtotal * 0.1}')
        total = subtotal + (subtotal * 0.1)
        print(f'Total a pagar --- ${total}')

funcion_CustomRappid()

#Desarrollado por Enrique Corpus - C.C: 1.143.405.301 
#Grupo S2 Campusland - Cajasan