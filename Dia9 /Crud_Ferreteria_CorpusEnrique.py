listaSencilla = [
  {
    "id": 1,
    "nombre": "Martillo",
    "categoria": "Herramientas manuales",
    "precio": 8.50,
    "stock": 25,
    "unidad_medida": "unidad"
  },
  {
    "id": 2,
    "nombre": "Destornillador plano",
    "categoria": "Herramientas manuales",
    "precio": 3.00,
    "stock": 40,
    "unidad_medida": "unidad"
  },
  {
    "id": 3,
    "nombre": "Destornillador de cruz",
    "categoria": "Herramientas manuales",
    "precio": 3.20,
    "stock": 35,
    "unidad_medida": "unidad"
  },
  {
    "id": 4,
    "nombre": "Llave inglesa",
    "categoria": "Herramientas manuales",
    "precio": 6.75,
    "stock": 20,
    "unidad_medida": "unidad"
  },
  {
    "id": 5,
    "nombre": "Alicates",
    "categoria": "Herramientas manuales",
    "precio": 5.50,
    "stock": 30,
    "unidad_medida": "unidad"
  },
  {
    "id": 6,
    "nombre": "Taladro eléctrico",
    "categoria": "Herramientas eléctricas",
    "precio": 45.00,
    "stock": 10,
    "unidad_medida": "unidad"
  },
  {
    "id": 7,
    "nombre": "Tornillos",
    "categoria": "Fijaciones",
    "precio": 0.10,
    "stock": 1000,
    "unidad_medida": "pieza"
  },
  {
    "id": 8,
    "nombre": "Clavos",
    "categoria": "Fijaciones",
    "precio": 0.05,
    "stock": 1500,
    "unidad_medida": "pieza"
  },
  {
    "id": 9,
    "nombre": "Tuercas y arandelas",
    "categoria": "Fijaciones",
    "precio": 0.08,
    "stock": 1200,
    "unidad_medida": "pieza"
  },
  {
    "id": 10,
    "nombre": "Cinta métrica",
    "categoria": "Medición",
    "precio": 4.50,
    "stock": 18,
    "unidad_medida": "unidad"
  },
  {
    "id": 11,
    "nombre": "Nivel de burbuja",
    "categoria": "Medición",
    "precio": 7.00,
    "stock": 12,
    "unidad_medida": "unidad"
  },
  {
    "id": 12,
    "nombre": "Sierra manual",
    "categoria": "Herramientas manuales",
    "precio": 9.25,
    "stock": 14,
    "unidad_medida": "unidad"
  },
  {
    "id": 13,
    "nombre": "Lijas",
    "categoria": "Abrasivos",
    "precio": 0.75,
    "stock": 200,
    "unidad_medida": "hoja"
  },
  {
    "id": 14,
    "nombre": "Pintura",
    "categoria": "Pinturas y acabados",
    "precio": 18.00,
    "stock": 50,
    "unidad_medida": "litro"
  },
  {
    "id": 15,
    "nombre": "Brochas",
    "categoria": "Pinturas y acabados",
    "precio": 2.50,
    "stock": 60,
    "unidad_medida": "unidad"
  },
  {
    "id": 16,
    "nombre": "Rodillos de pintura",
    "categoria": "Pinturas y acabados",
    "precio": 4.00,
    "stock": 40,
    "unidad_medida": "unidad"
  },
  {
    "id": 17,
    "nombre": "Silicona selladora",
    "categoria": "Selladores y adhesivos",
    "precio": 3.80,
    "stock": 25,
    "unidad_medida": "tubo"
  },
  {
    "id": 18,
    "nombre": "Cinta aislante",
    "categoria": "Eléctrico",
    "precio": 1.20,
    "stock": 100,
    "unidad_medida": "rollo"
  },
  {
    "id": 19,
    "nombre": "Tubos de PVC",
    "categoria": "Plomería",
    "precio": 2.00,
    "stock": 75,
    "unidad_medida": "metro"
  },
  {
    "id": 20,
    "nombre": "Cemento de contacto",
    "categoria": "Adhesivos",
    "precio": 6.00,
    "stock": 22,
    "unidad_medida": "litro"
  },
  {
    "id": 21,
    "nombre": "Guantes de trabajo",
    "categoria": "Seguridad",
    "precio": 2.80,
    "stock": 80,
    "unidad_medida": "par"
  },
  {
    "id": 22,
    "nombre": "Linterna portátil",
    "categoria": "Iluminación",
    "precio": 5.50,
    "stock": 15,
    "unidad_medida": "unidad"
  }
]

# Print listaSencilla
booleanito = True
while(booleanito):
    print("1. Crear")
    print("2. Ver todo")
    print("3. Ver uno")
    print("4. ACtualizar uno")
    print("5. Eliminar uno.")
    print("6. Salir del programa")
    opcionUsuario=int(input("¿Qué quieres hacer?"))

    # Establecemos condiciones según opción escogida
    if (opcionUsuario==1):
        nombreNuevo = input('Ingresa el nombre nuevo: ')
        categoriaNueva = input('Ingresa la nueva categoría: ')
        precioNuevo = float(input('Ingresa el nuevo precio: '))
        stockNuevo = int(input('Ingresa el nuevo stock: '))
        unidadNueva = input('Ingresa la unidad nueva: ')
        diccionarioNuevo = {
            "id":listaSencilla[len(listaSencilla)-1]["id"]+1,
            "nombre":nombreNuevo,
            "categoria":categoriaNueva,
            "precio":precioNuevo,
            "stock":stockNuevo,
            "unidad_medida":unidadNueva,
        }
        listaSencilla.append(diccionarioNuevo)
        print('Producto creado!!!!')

    elif(opcionUsuario==2):
        for i in range(len(listaSencilla)):
            print("Persona #", i+1 )
            print("ID",listaSencilla[i]["id"])
            print("Nombre",listaSencilla[i]["nombre"])
            print("Categoria:", listaSencilla[i]["categoria"])
            print("Precio:",listaSencilla[i]["precio"])
            print("Stock:", listaSencilla[i]["stock"])
            print("Unidad de Medida:",listaSencilla[i]["unidad_medida"])
    
    elif(opcionUsuario==3):
        opcionProducto= int(input("Ingresa el numero del producto"))
        print("##################")
        print("Producto # ", opcionProducto)
        print("ID", listaSencilla[opcionProducto-1]["id"])
        print("Nombre", listaSencilla[opcionProducto-1]["nombre"])
        print("Categoria", listaSencilla[opcionProducto-1]["categoria"])
        print("Precio", listaSencilla[opcionProducto-1]["precio"])
        print("Stock", listaSencilla[opcionProducto-1]["stock"])
        print("Unidad de Medida",listaSencilla[opcionProducto-1]["unidad_medida"])

    elif(opcionUsuario==4):
        print("##################")
        print("actualizar articulo")
        print("##################")
       
        actualizarArticulo=int(input("Ingresa el numero del producto"))
        print("##################")
        print("Producto # ", actualizarArticulo)
        print("ID", listaSencilla[actualizarArticulo-1]["id"])
        print("Nombre", listaSencilla[actualizarArticulo-1]["nombre"])
        print("Categoria", listaSencilla[actualizarArticulo-1]["categoria"])
        print("Precio", listaSencilla[actualizarArticulo-1]["precio"])
        print("Stock", listaSencilla[actualizarArticulo-1]["stock"])
        print("Unidad de Medida",listaSencilla[actualizarArticulo-1]["unidad_medida"])

        nombreActualizado = input('Ingresa el nombre nuevo: ')
        categoriaActualizada = input('Ingresa la nueva categoría: ')
        precioActualizado = float(input('Ingresa el nuevo precio: '))
        stockActualizado = int(input('Ingresa el nuevo stock: '))
        unidadActualizada = input('Ingresa la unidad nueva: ')
        
        diccionariActualizado={
                          "nombre": nombreActualizado,
                          "categoria": categoriaActualizada,
                          "precio": precioActualizado,
                          "stock": stockActualizado,
                          "unidad_medida": unidadActualizada
        }

        listaSencilla[actualizarArticulo-1]["nombre"] = nombreActualizado
        listaSencilla[actualizarArticulo-1]["categoria"] = categoriaActualizada
        listaSencilla[actualizarArticulo-1]["precio"] = precioActualizado
        listaSencilla[actualizarArticulo-1]["stock"] = stockActualizado
        listaSencilla[actualizarArticulo-1]["unidad_medida"] = unidadActualizada  
        
        print("Producto # ", actualizarArticulo)
        print("ID", listaSencilla[actualizarArticulo-1]["id"])
        print("Nombre", listaSencilla[actualizarArticulo-1]["nombre"])
        print("Categoria", listaSencilla[actualizarArticulo-1]["categoria"])
        print("Precio", listaSencilla[actualizarArticulo-1]["precio"])
        print("Stock", listaSencilla[actualizarArticulo-1]["stock"])
        print("Unidad de Medida",listaSencilla[actualizarArticulo-1]["unidad_medida"])
     
    elif(opcionUsuario==5):
        
        print("#################")
        print("#### Eliminar Persona Individual ####")
        print("#################")
        
        opcionEliminar= int(input("Ingresa el id que deseas eliminar"))
        print("##################")
        print("Producto a eliminar  # ", opcionEliminar)
        print("ID", listaSencilla[opcionEliminar-1]["id"])
        print("Nombre", listaSencilla[opcionEliminar-1]["nombre"])
        print("Categoria", listaSencilla[opcionEliminar-1]["categoria"])
        print("Precio", listaSencilla[opcionEliminar-1]["precio"])
        print("Stock", listaSencilla[opcionEliminar-1]["stock"])
        print("Unidad de Medida",listaSencilla[opcionEliminar-1]["unidad_medida"])
        
        
        
        opcionIndividual = int(input("¿Estás seguro de eliminar a esta persona? (1.Si,2.No):"))
        
        
        if (opcionIndividual==1):
            listaSencilla.pop(opcionIndividual-1)
            print("Usuario eliminado!")
        else:
            print("Gracias por confirmar!")
            
            
        
    elif(opcionUsuario==6):
        print("Chaousssss")
        booleanito=False
    else:
        print("No es una opción válida")