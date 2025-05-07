#ejercicio 2 

# hacer un programa en el cual se envíen dos cadenas de texto y el programa retorne las dos cadenas con los caracteres entrelazados alternativamente así:
#cadena 1: hola; cadena 2: banano; lo q el programa deberá retornar: hboalnaano

print('ingrese la primera cadena de texto que desea combinar')
cadena1=str(input())

print('ingrese la segunda cadena de texto que desea combinar')
cadena2=str(input())

longitudC1= len(cadena1) 
longitudC2= len(cadena2)
combinacion= ''
n=0
    
for i in range (longitudC1):
    #cree la variable n para que cumpla papel de iterador o como  un contador, que comience en 0 y termine con el valor que tiene la  longitud de la cadena 2 
    n = longitudC2 - (longitudC2-i)

    combinacion = combinacion + cadena1[i] + cadena2[n]


print('el resultado es', combinacion)
   