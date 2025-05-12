#ejercicios simples de listas de comprension 
#imprimir los dobles de cada numero de 1 al 10 
dobles = [i * 2 for i in range(1, 11)]
print(dobles)

#imprimir modulos de cada numero de 1 al 10
modulos = [i % 2 for i in range(1, 11)]
print(modulos)

#imprimir los impares de 1 al 10
impares = [i for i in range(1, 11) if i % 2 != 0]
print(impares)       

#imprimir los numeros primos de 1 al 10
primos = [i for i in range(1, 11) if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1))]
print(primos)

#imprimir numeros binarios de 1 al 10
binarios = [bin(i)[2:] for i in range(1, 11)]
print(binarios)

#crear  una lista por compresion de una cadena de texto que tenga de 1 a 5 '*'
cadena = ['*' * i for i in range(1, 6)]
print(cadena)
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

#ejercicios con porciones de una lista 

#crea una lista con las iniciales de la lista [Casa, Mesa, Silla Cuarto ]

lista1 = ['Casa', 'Mesa', 'Silla', 'Cuarto']
n=0
lista2 = [p[0] for p in lista1]
print(lista2)

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

#Listas solo con condicional 

#crea una lista con las palabras de la  lista dada, pero solo con las que tengan mas de 7 letras

listaDada= ['mesa', 'interuptor', 'silla', 'microscopio', 'cubo', '1234567', '123456']

lista7P= [p for p in listaDada if len(p) >= 7  ]
print(lista7P)

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

#Listas con condicionales y else 

#imprimir una lista de numeros pares, y en los impartes rempzamaos el valor por un 0 
#lista por comprensiom con bloque else, el if tiene que ir antes del for 

impares0= [n if n % 2 == 0 else 0 for n in range(1,21)]
print(impares0)

#crea una lista con el tipo de datos de cada elemento 
# si son str , cadena 
# si son int o float, numerico 

datos = [7, 'h', 2.5, 'm', 8.2, 24, 'p']

tipos=[ 'cadena' if type(t)== str 
       else 'numerico' 
       for t in datos]
print(tipos)
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

#listas por compresion a partir de listas anidadas 

#la lista persona contiene listas anidadas que da nombre y edad 
#crear una lista  por comprension con edades mayores a 18

personas = [['pedro', 25], ['kike',27], ['sharick',17], ['nicol',18]]

mayores= [e  for e in personas if e[1] > 18]
print(mayores)

#la lista persona contiene listas anidadas que da nombre y edad 
#crear una lista  por comprension 
#si es mayor, mayores
#si es menor . menores 

personas = [['pedro', 25], ['kike',27], ['sharick',17], ['nicol',18]]
mayorMenor= [ 'menores' if e[1]< 18 else 'mayores' for e in personas ]
print(mayorMenor)
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

#listas por compresion a partir de diccionarios 


# crea una lista que contenga los articulos del inventario cuyas unidades sean menor de 100 
inventario={'puntas': 120,
            'clavos':200,
            'tuercas': 50, 
            'tornillos': 80}

pedido=[articulo for articulo in inventario if inventario[articulo] < 100]
print(pedido)
#crea una listas con cuyos alummnos hayan aprobado, se aprueba con mas de 5 

alummnos=[{'nombre': 'enrique', 'nota': 6, 'grupo': 'A'},
            {'nombre': 'sharick', 'nota': 8, 'grupo': 'A'},
            {'nombre': 'juan', 'nota': 4, 'grupo': 'b'},
            {'nombre': 'heyder', 'nota': 2, 'grupo': 'c'}]

aprobados=[a['nombre'] for a in alummnos if a['nota']>=5]

print(aprobados)

#listas de diccionarios con diccionarios 

#crear una lista con los alumnos que hayan aprobado castellano

alummnos= {'claudia': {'matematica': 5, 'castellano': 3, 'artes': 5},
           'nicol': {'matematica': 8, 'castellano': 8, 'artes': 8},
           'sharik': {'matematica': 7, 'castellano': 6, 'artes': 10},
           'kike': {'matematica': 3, 'castellano': 3, 'artes': 3},
           'jose': {'matematica': 1, 'castellano': 7, 'artes': 2},
           }

aprobados=[  a for a in alummnos if alummnos[a]['castellano']>5 ]
print(aprobados)

#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------

#listas a partir de funciones 

