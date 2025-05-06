#ejercicio 2 empresa acme 

# Mensaje de bienvenida
print("Bienvenido al portal de nómina de la empresa ACME\n")

# Entrada del número de empleados
nEmpleados = int(input("¿De cuántos empleados deseas calcular la nómina? "))

# Inicializar variables acumuladoras
totalBruto = 0
totalEPS = 0
totalPension = 0
totalNeto = 0

mayorSueldoNeto = 0
nombreMayorSueldo = ""

menorSueldoNeto = 0
nombreMenorSueldo = ""

#Cilo para ingresar datos de cada empleado
for i in range(1, nEmpleados + 1):
    print(f"\n¿Cuál es el nombre del empleado #{i}?")
    nombreEmpleado = input("Nombre: ")

    HorasTrabajadas = float(input("¿Cuántas horas trabajó el empleado? "))

    # Cálculos de salario
    sueldoBruto = HorasTrabajadas * 20000
    eps = sueldoBruto * 0.04
    pension = sueldoBruto * 0.04
    sueldoNeto = sueldoBruto - (eps + pension)

    # Mostrar resultados individuales
    print(f"El sueldo bruto del empleado #{i} es: ${sueldoBruto}")
    print(f"El descuento de EPS del empleado #{i} es: ${eps}")
    print(f"El descuento de pensión del empleado #{i} es: ${pension}")
    print(f"El sueldo neto del empleado #{i} es: ${sueldoNeto}")

    # Acumular totales
    totalBruto += sueldoBruto
    totalEPS += eps
    totalPension += pension
    totalNeto += sueldoNeto

    # Evaluar mayor sueldo neto
    if mayorSueldoNeto == 0 or sueldoNeto > mayorSueldoNeto:
        mayorSueldoNeto = sueldoNeto
        nombreMayorSueldo = nombreEmpleado

    # Evaluar menor sueldo neto
    if menorSueldoNeto == 0 or sueldoNeto < menorSueldoNeto:
        menorSueldoNeto = sueldoNeto
        nombreMenorSueldo = nombreEmpleado

# Mostrar estadísticas finales
print("\n++++++++++++++++++++++++++++++++++++++++++++")
print(f"Estadística de totales de la nómina de {nEmpleados}:")
print(f"Total sueldos brutos: ${totalBruto}")
print(f"Total descuentos EPS: ${totalEPS}")
print(f"Total descuentos pensión: ${totalPension}")
print(f"Total sueldos netos: ${totalNeto}")
print("++++++++++++++++++++++++++++++++++++++++++++")

# Promedios
promedioBruto = totalBruto / nEmpleados
promedioNeto = totalNeto / nEmpleados

print("\n;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
print("El promedio de cada sueldo es:")
print(f"Promedio de sueldos brutos: ${promedioBruto}")
print(f"Promedio de sueldos netos: ${promedioNeto}")
print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")

# Mostrar mayor y menor sueldo
print("\n======================================")
print("Empleado que más gana:")
print("Nombre:", nombreMayorSueldo)
print(f"Sueldo Neto: ${mayorSueldoNeto}")

print("\nEmpleado que menos gana:")
print("Nombre:", nombreMenorSueldo)
print(f"Sueldo Neto: ${menorSueldoNeto}")
print("======================================")

#Desarrollado por Enrique Corpus - C.C: 1.143.405.301 
#Grupo S2 Campusland - Cajasan