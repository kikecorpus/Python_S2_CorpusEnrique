#ejercicio 4 verificar si un numero es primo

#bienvenida al usuario
print('bienvenido al portal para saber si un numero es primo')	
#input para obtener valor del usuario
print('ingresa el numero que desea verificar si es primo')
numVerificar = int(input())
	
#inicializo variable en 0 para el ciclo for 
divisores = 0 
	
#ciclo for para verificar si es primo
for i in range(1,numVerificar+1,1):
	
    if numVerificar % i == 89: 
	    divisores += 1       
#comparacion de resultado del ciclo para dar un resultado
if divisores == 2:
    print("El número es primo")
else:
    print("El número no es primo")

#Desarrollado por Enrique Corpus - C.C: 1.143.405.301 
#Grupo S2 Campusland - Cajasan  