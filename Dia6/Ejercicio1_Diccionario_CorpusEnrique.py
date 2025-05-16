# ##########################
# #### Clase Dia 6 ######
# ##########################



#Un objeto tiene varios atributos, 
# que pertenecen al mismo objeto. 

##Diccionario con listas

#creacion de un diccionario con una lista de diccionario 
diccionarioRobusto={
    "id":1,
    "nombre":"Pedro",
    "apellido":"Gómez",
    "edad":25,
    "telefonos":[{"codigo":57,"numero":3023019865,"tipo":"trabajo"}
                 ,{"codigo":1,"numero":3983054625,"tipo":"personal"}]
}

#creacion del segundo diccionario 
diccionarioRobusto2={
    "id":2,
    "nombre":"Corpus",
    "apellido":"Bejarano",
    "edad":27,
    "telefonos":[{"codigo":58,"numero":2323057565,"tipo":"trabajo"}
                 ,{"codigo":22,"numero":6857493658,"tipo":"personal"}]
}

#agregando los dos diccionarios en una lista 

listaRobusta=[]
listaRobusta.append(diccionarioRobusto)
listaRobusta.append(diccionarioRobusto2)

'''
#imprimir numero de telefono del diccionario 0 
for i in range(len(listaRobusta[0]["telefonos"])):
    if(listaRobusta[0]["telefonos"][i]['tipo']=="trabajo"):
        print(listaRobusta[0]["telefonos"][i]['numero'])
print("")
print("")
numeroPrimeraPersona=listaRobusta[0]["telefonos"][1]['numero']
tipoNumeroPP=listaRobusta[0]["telefonos"][1]['tipo']
print(str(numeroPrimeraPersona)+ tipoNumeroPP)
'''
#creacion del CRUD


booleanito = True



while(booleanito):
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
   
    opcionUsuario=int(input("Escoja una opción (Numérica):"))
    
    
    
    if(opcionUsuario==1):
        print("#######################")
        print("#### Crear Persona ####")
        print("#######################")
        
       
        print("cuantas personas desea agregar")
        cantidadP = int(input())
        

        
        for p in range(cantidadP):
            diccionarioVacio={}
            print("A continuacion ingrese los datos de la persona #",p+1, " que desea agregar")
            print("")
            print("ingrese el ID de la persona")
            idN= int(input())
            print("")
            print("")   
            print("ingrese el nombre de la persona")
            nombrN =  str(input())
            print("") 
            print("ingrese el apellido de la persona")
            apellidoN= str(input())
            print("") 
            print("ingrese la edad de la persona")
            edadN= int(input())
            print("") 
            print("cuantos numeros de telefono desea agregar de la persona")
            cantT=int(input())
            
            for t in range(cantT):
                telefonoList={}
                listaAgregado=[]
                print("a continuacion ingresa los datos del numero de telefono #",t+1)
                print("")
                print("ingresa codigo del numero  de telefono de la persona")
                codigoT=str(input())
                print("")
                print("ingresa numero de telefono de la persona")
                numeroT = str(input())
                print("")
                print("ingresa tipo del numero telefono de la perso≤na")
                tipoT=str(input())
                telefonoList={"codigo": codigoT,
                            "numero": numeroT,
                            "tipo": tipoT}
            
             
            diccionarioVacio={"id": idN,
                             "nombre": nombrN, 
                             "apellido":apellidoN,
                             "edad":edadN,
                             "telefonos":[telefonoList]}
                                    
            listaRobusta.append(diccionarioVacio)
            listaAgregado.append(diccionarioVacio)
            
            print("A continuacion la informacion agregada")
            print(listaAgregado)
            
        
    

    elif(opcionUsuario==2):
        for i in range(len(listaRobusta)):
            print("#################")
            print("#### Persona #",i+1," ####")
            print("#################")
            print("ID:", listaRobusta[i]["id"])
            print("Nombre:",listaRobusta[i]["nombre"])
            print("Apellido:",listaRobusta[i]["apellido"])
            print("Edad",listaRobusta[i]["edad"])
            
            for q in range(len(listaRobusta[i]["telefonos"])):
                print("---------------------------")
                print("Telefono#",q+1,":")
                print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                if(listaRobusta[i]["telefonos"][q]["tipo"] == "personal"):
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
                
                print("---------------------------")

            
    elif(opcionUsuario==3):
        
        print("Ingrese el ID de la persona que desea consultar")
        buscar = input()
       

        for b in listaRobusta:
            if b["id"] == buscar:
                print(b)
            
                
    
            

        
               
                
            
    elif(opcionUsuario==6):
        print("Chaousssss")
        booleanito=False
    else:
        print("No es una opción válida")

    
    
    
#Desarrollado por Enrique Corpus cc. 1143405301
