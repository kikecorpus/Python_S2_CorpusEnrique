#ejercicio 1 restaurante rappid 
# Definir variables
numbHamb = int(input("¿Cuántas hamburguesas deseas ordenar? "))
subtotal = 0
servicio = 0.1  

# bienvenida
print("Bienvenidos al restaurante Custom Rappid")
print("A continuación personaliza tu hamburguesa escribiendo los números que corresponden a tus ingredientes favoritos")

# Repetir la selección de ingredientes por cada hamburguesa
for i in range(1, numbHamb + 1):
    print(f"\nPersonalizando hamburguesa #{i}")

    # Selección de pan
    print("Selecciona el pan que deseas en tu hamburguesa:")
    print("1. Pan de centeno -- $1000 COP")
    print("2. Pan de avena -- $1500 COP")
    ingrediente = int(input())

    while ingrediente not in [1, 2]:
        print("Selecciona una opción válida entre 1 y 2")
        ingrediente = int(input())

    if ingrediente == 1:
        print("Seleccionaste pan de centeno")
        subtotal += 1000
    elif ingrediente == 2:
        print("Seleccionaste pan de avena")
        subtotal += 1500

    # Selección de carne
    print("Selecciona la carne que deseas en tu hamburguesa:")
    print("1. Carne 250g -- $5000 COP")
    print("2. Carne 350g -- $7000 COP")
    print("3. Ninguno")
    ingrediente = int(input())

    while ingrediente not in [1, 2, 3]:
        print("Selecciona una opción válida entre 1, 2 o 3")
        ingrediente = int(input())

    if ingrediente == 1:
        print("Seleccionaste carne 250g")
        subtotal += 5000
    elif ingrediente == 2:
        print("Seleccionaste carne 350g")
        subtotal += 7000
    elif ingrediente == 3:
        print("No incluiste carne en tu hamburguesa")

    # Selección de pollo
    print("Selecciona el pollo que deseas en tu hamburguesa:")
    print("1. Pollo 250g -- $4500 COP")
    print("2. Pollo 350g -- $5500 COP")
    print("3. Ninguno")
    ingrediente = int(input())

    while ingrediente not in [1, 2, 3]:
        print("Selecciona una opción válida entre 1, 2 o 3")
        ingrediente = int(input())

    if ingrediente == 1:
        print("Seleccionaste pollo 250g")
        subtotal += 4500
    elif ingrediente == 2:
        print("Seleccionaste pollo 350g")
        subtotal += 5500
    elif ingrediente == 3:
        print("No incluiste pollo en tu hamburguesa")

    # Selección de pollo desmechado
    print("Selecciona el pollo desmechado que deseas en tu hamburguesa:")
    print("1. Pollo desmechado 250g -- $6500 COP")
    print("2. Pollo desmechado 350g -- $7500 COP")
    print("3. Ninguno")
    ingrediente = int(input())

    while ingrediente not in [1, 2, 3]:
        print("Selecciona una opción válida entre 1, 2 o 3")
        ingrediente = int(input())

    if ingrediente == 1:
        print("Seleccionaste pollo desmechado 250g")
        subtotal += 6500
    elif ingrediente == 2:
        print("Seleccionaste pollo desmechado 350g")
        subtotal += 7500
    elif ingrediente == 3:
        print("No incluiste pollo desmechado en tu hamburguesa")

    # Selección de tocineta
    print("Selecciona la lonja de tocineta que deseas en tu hamburguesa:")
    print("1. Lonja de tocineta -- $1500 COP")
    print("2. Lonjas de tocineta -- $2500 COP")
    print("3. Ninguno")
    ingrediente = int(input())

    while ingrediente not in [1, 2, 3]:
        print("Selecciona una opción válida entre 1, 2 o 3")
        ingrediente = int(input())

    if ingrediente == 1:
        print("Seleccionaste lonja de tocineta")
        subtotal += 1500
    elif ingrediente == 2:
        print("Seleccionaste lonjas de tocineta")
        subtotal += 2500
    elif ingrediente == 3:
        print("No incluiste lonja de tocineta en tu hamburguesa")

    # Selección de papas
    print("Selecciona la porción de papas que deseas en tu hamburguesa:")
    print("1. Papas francesas -- $5000 COP")
    print("2. Papas cascos -- $6000 COP")
    print("3. Ninguno")
    ingrediente = int(input())

    while ingrediente not in [1, 2, 3]:
        print("Selecciona una opción válida entre 1, 2 o 3")
        ingrediente = int(input())

    if ingrediente == 1:
        print("Seleccionaste papas francesas")
        subtotal += 5000
    elif ingrediente == 2:
        print("Seleccionaste papas cascos")
        subtotal += 6000
    elif ingrediente == 3:
        print("No incluiste papas en tu hamburguesa")

    # Selección de bebida
    print("Selecciona la bebida con la que deseas acompañar tu hamburguesa:")
    print("1. Gaseosa -- $5000 COP")
    print("2. Cerveza Club Colombia -- $6000 COP")
    print("3. Naranjada -- $9000 COP")
    print("4. Ninguna")
    ingrediente = int(input())

    while ingrediente not in [1, 2, 3, 4]:
        print("Selecciona una opción válida entre 1, 2, 3 o 4")
        ingrediente = int(input())

    if ingrediente == 1:
        print("Seleccionaste gaseosa")
        subtotal += 5000
    elif ingrediente == 2:
        print("Seleccionaste cerveza Club Colombia")
        subtotal += 6000
    elif ingrediente == 3:
        print("Seleccionaste naranjada")
        subtotal += 9000
    elif ingrediente == 4:
        print("No incluiste bebida para acompañar tu hamburguesa")

# Cálculo del total con servicio 
total = subtotal + (subtotal * servicio)

if numbHamb != 1:
    print(f"\nHaz completado la personalización de tus {numbHamb} hamburguesas.")
    print(f"El valor a pagar es de ${subtotal}")
    print(f"Valor del servicio (10%) es: ${subtotal * servicio}")
    print(f"Total a pagar: ${total}")
else:
    print("\nHaz completado la personalización de tu hamburguesa.")
    print(f"El valor a pagar es de ${subtotal}")
    print(f"Valor del servicio (10%) es: ${subtotal * servicio}")
    print(f"Total a pagar: ${total}")

#Desarrollado por Enrique Corpus - C.C: 1.143.405.301 
#Grupo S2 Campusland - Cajasan