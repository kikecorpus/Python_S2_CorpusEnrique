# Ejercicio2_FiltroIntro_CorpusEnrique

# Definir variables
suma = 0
resta = 0
division = 0
multiplicacion = 0

# Entrada de datos
print('Bienvenido a realizar tu operacion matematica')
print('¿Cual operacion desea realizar?')
print('1. suma')
print('2. resta')
print('3. multiplicacion')
print('4. division')
operacion = int(input())

print("")
print('ingresa el primer numero')
num1 = int(input())

print("")
print('ingresa el segundo numero')
num2 = int(input())

print("")

# Operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

# Selección según la operación
if operacion == 1:
    print('el resultado de la suma es', suma)
elif operacion == 2:
    print('el resultado de la resta es', resta)
elif operacion == 3:
    print('el  resultado de la mmultiplicacion es', multiplicacion)
elif operacion == 4:
    print('el resultado de la divisiona es', division)
