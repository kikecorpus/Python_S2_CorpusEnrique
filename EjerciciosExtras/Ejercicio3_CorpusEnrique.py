#ejercicio 3 

vocal= ['a','e','i','o','u']

consonante= ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

numeros= ['1','2','3','4','5','6','7','8','9','0']

contadorV= 0 
contadorN= 0
contadorC= 0 

print ('ingresa la cadena de texto y/o numero que desees')
cadena= str(input().lower())

for caracter in cadena:
    if caracter in numeros:
        contadorN+=1 
        
for i in cadena:
    if i in vocal:
        contadorV+=1 
 
for i in cadena:
    if i in consonante:
        contadorC+=1
        

print('la cantidad de vocales encontradas en el texto fue de:', contadorV)
print('la cantidad de consonantes encontradas en el texto fue de:', contadorC)
print('la cantidad de numeros encontrados en el texto fue de:', contadorN)

        

               