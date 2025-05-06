#ejercicio 2 empresa acme con funciones

#definir funciones que voy a utilizar 

def mensaje_bienvenida():
    print("Bienvenido al portal de nómina de la empresa ACME")
    print("") 
    print("¿De cuántos empleados deseas calcular la nómina?")

def calcular_sueldo_bruto(horas_trabajadas):
    return horas_trabajadas * 20000 

def calcular_pension(sueldo_bruto):
    return sueldo_bruto * 0.04 

def calcular_eps(sueldo_bruto):
    return sueldo_bruto * 0.04

def calcular_sueldo_neto(sueldo_bruto, eps, pension):
    return sueldo_bruto - (eps + pension)

def calcular_total_bruto(total_bruto, sueldo_bruto):
    return total_bruto + sueldo_bruto

def calcular_total_neto(total_neto, sueldo_neto):
    return total_neto + sueldo_neto

def calcular_total_eps(total_eps, eps):
    return total_eps + eps

def calcular_total_pension(total_pension, pension):
    return total_pension + pension

def actualizar_mayor_y_menor(nombre_empleado, sueldo_neto, mayor_sueldo_neto, nombre_mayor_sueldo, menor_sueldo_neto, nombre_menor_sueldo):
    if mayor_sueldo_neto == 0 or sueldo_neto > mayor_sueldo_neto:
        mayor_sueldo_neto = sueldo_neto
        nombre_mayor_sueldo = nombre_empleado
    
    if menor_sueldo_neto == 0 or sueldo_neto < menor_sueldo_neto:
        menor_sueldo_neto = sueldo_neto
        nombre_menor_sueldo = nombre_empleado
    
    return mayor_sueldo_neto, nombre_mayor_sueldo, menor_sueldo_neto, nombre_menor_sueldo

#definir una funcion donde utilizo la funciones anteriores 
def funcion_empresa_acme():
    n_empleados = int(input("¿Cuántos empleados deseas calcular la nómina? "))
    
    total_bruto = 0
    total_eps = 0
    total_pension = 0
    total_neto = 0
    
    mayor_sueldo_neto = 0
    nombre_mayor_sueldo = ""
    
    menor_sueldo_neto = 0
    nombre_menor_sueldo = ""
    
    for i in range(1, n_empleados + 1):
        nombre_empleado = input(f"¿Cuál es el nombre del empleado #{i}? ")
        horas_trabajadas = int(input(f"¿Cuántas horas trabajó el empleado #{i}? "))
        
        sueldo_bruto = calcular_sueldo_bruto(horas_trabajadas)
        pension = calcular_pension(sueldo_bruto)
        eps = calcular_eps(sueldo_bruto)
        sueldo_neto = calcular_sueldo_neto(sueldo_bruto, eps, pension)
        
        print(f"El sueldo bruto del empleado #{i} es de ${sueldo_bruto}")
        print(f"El descuento de EPS del empleado #{i} es de ${eps}")
        print(f"El descuento de pensión del empleado #{i} es de ${pension}")
        print(f"El sueldo neto del empleado #{i} es de ${sueldo_neto}")
        
        total_bruto = calcular_total_bruto(total_bruto, sueldo_bruto)
        total_neto = calcular_total_neto(total_neto, sueldo_neto)
        total_eps = calcular_total_eps(total_eps, eps)
        total_pension = calcular_total_pension(total_pension, pension)
        
        mayor_sueldo_neto, nombre_mayor_sueldo, menor_sueldo_neto, nombre_menor_sueldo = actualizar_mayor_y_menor(
            nombre_empleado, sueldo_neto, mayor_sueldo_neto, nombre_mayor_sueldo, menor_sueldo_neto, nombre_menor_sueldo)
    
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print(f"Estadísticas de totales de la nómina de {n_empleados} empleados:")
    print(f"Total sueldos brutos: ${total_bruto}")
    print(f"Total descuentos EPS: ${total_eps}")
    print(f"Total descuentos pensión: ${total_pension}")
    print(f"Total sueldos netos: ${total_neto}")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    
    promedio_bruto = total_bruto / n_empleados
    promedio_neto = total_neto / n_empleados
    
    print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
    print(f"El promedio de cada sueldo es:")
    print(f"Promedio de sueldos brutos: ${promedio_bruto}")
    print(f"Promedio de sueldos netos: ${promedio_neto}")
    print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
    
    print("======================================")
    print(f"Empleado que más gana:")
    print(f"Nombre: {nombre_mayor_sueldo}")
    print(f"Sueldo Neto: ${mayor_sueldo_neto}")
    print("")
    print(f"Empleado que menos gana:")
    print(f"Nombre: {nombre_menor_sueldo}")
    print(f"Sueldo Neto: ${menor_sueldo_neto}")
    print("======================================")

# Llamar a la función principal
funcion_empresa_acme()
#Desarrollado por Enrique Corpus - C.C: 1.143.405.301 
#Grupo S2 Campusland - Cajasan