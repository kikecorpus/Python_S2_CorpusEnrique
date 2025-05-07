# Ejercicio1  de Dante 
#hacer un programa en el cual el usuario ingrese un número y se le devuelva la suma de todos los números desde 1 hasta el número q ingresó
#ejemplo: si el usuario ingresa 5 se le retornará 1+2+3+4+5 = 15


print('ingrese el numero el cual desea sumar con su antecesores ')
numero= int(input())

sumatoria=0
for i in range (numero,0,-1):
    sumatoria= sumatoria + i
    
print('el resultadode la suma del', numero, 'es', sumatoria)