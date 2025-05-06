# Definición de funciones

def Funcionsuma(num1, num2):
    return num1 + num2

def Funcionresta(num1, num2):
    return num1 - num2

def FuncionMultiplicacion(num1, num2):
    return num1 * num2

def FuncionDivision(num1, num2):
    return num1 / num2


# Programa principal

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

# Lógica de selección
if operacion == 1:
    print('el resultado de la suma es', Funcionsuma(num1, num2))
elif operacion == 2:
    print('el resultado de la resta es', Funcionresta(num1, num2))
elif operacion == 3:
    print('el  resultado de la mmultiplicacion es', FuncionMultiplicacion(num1, num2))
elif operacion == 4:
    print('el resultado de la division es', FuncionDivision(num1, num2))
