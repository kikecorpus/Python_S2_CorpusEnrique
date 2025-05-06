######################################
# Ejercico 1, factorial de un numero##
######################################

#bienvenida al usuario
print('Bienvenido al portal para calcular el factorial de un numero')

#input para obtener valor del usuario
print('Ingresa el numero el cual deseas calcular el factorial')
numero= int(input())

#inicializo factorial en 1 para calcular su valor en el For
factorial= 1

#ciclo for con iterador de 1 hasta la variable numero con paso 1 
for i in range (1,numero+1,1):

#operacion para calcular el factorial multiplicando el iterador por el factorial 
    factorial *= i

#imprimo resultado
print('el factorial es', factorial) 

#Desarrollado por Enrique Corpus - C.C: 1.143.405.301 
#Grupo S2 Campusland - Cajasan