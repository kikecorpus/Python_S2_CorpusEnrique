#ejericio 8 serie fibonacci

#defino los dos primeros digitos de la serie 
primerTermino= 0
segundoTermino= 1

#input para obtener valores del usuario
print('ingrese la cantidad de numeros que desea ver de la serie Fibonacci')
cantidadTerminos= int(input())
print('')
print('la serie es:')
#imprimo los dos primeros digitos preestablecidos
print(primerTermino)
print(segundoTermino)


#ciclo for para calcular e imprimir los demas digitos de la serie
for i in range(2,cantidadTerminos,1):
    
    tercerTermino= primerTermino + segundoTermino
    print(tercerTermino) 
		
    primerTermino = segundoTermino
    segundoTermino = tercerTermino

#Desarrollado por Enrique Corpus - C.C: 1.143.405.301 
#Grupo S2 Campusland - Cajasan