##################################
# Ejercico 2, mayor de 3 numeros #
##################################

#bienvenida e indicacion al usuario 
print ('Bienvenido al portal para comparar 3 numeros')
print('A continuacion escribe los 3 numero a comparar')

#ingreso input para obetener valores del usuario
print('Ingresa el primer numero')
print('')
numero1= float(input())
print('ingresa el segundo numero')
numero2= float(input())
print('')
print('ingresa el tercer numero')
numero3= float(input())

#codicional if para comparar el mayor
if numero1 > numero2 and numero1 > numero3:
    print('El numero mayor es ', numero1 )
elif numero2 > numero1 and numero2 > numero3:
    print('El numero mayor es ', numero2)
else: 
    print('El numero mayor es ', numero3)
    
#Desarrollado por Enrique Corpus - C.C: 1.143.405.301 
#Grupo S2 Campusland - Cajasan