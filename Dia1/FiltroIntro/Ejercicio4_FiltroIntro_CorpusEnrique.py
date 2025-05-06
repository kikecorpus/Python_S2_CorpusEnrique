# Función para convertir binario a decimal
def BinarioADecimal(binario):
    Decimal = 0
    base = 0
    
    while binario > 0:
        residuo = binario % 10
        Decimal = Decimal + residuo * (2 ** base)
        base = base + 1
        binario = binario // 10

    print(Decimal)
    return Decimal


# Función para convertir decimal a binario
def convertirDecimalABinario(Decimal):
    binario = 0
    base = 0

    while Decimal > 0:
        residuo = Decimal % 2
        binario = binario + residuo * (10 ** base)
        base = base + 1
        Decimal = Decimal // 2

    return binario


# Programa principal
def Ejercicio4_FiltroIntro_CorpusEnrique():
    conversion = 0

    print("bienvenido a convertir decimal y binario\n")

    while conversion < 3:
        print("¿Cual conversion desea realizar?")
        print("1. Decimal a Binario")
        print("2. Binario a Decimal")
        print("3. Salir")
        conversion = int(input())

        if conversion == 1:
            print("Ingrese decimal")
            Decimal = int(input())
            print("La conversion de decimal a binario es", convertirDecimalABinario(Decimal))
        
        else:
            if conversion == 2:
                print("Escribir binario")
                binario = int(input())
                print("La conversion de binario a decimal es", BinarioADecimal(binario))

    print("Saliste del programa")


# Llamar al programa principal
Ejercicio4_FiltroIntro_CorpusEnrique()
