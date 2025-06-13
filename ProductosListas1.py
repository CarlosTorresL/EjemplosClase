productos=[]

while True:
  sw=1
  
  print("Bienvenidos al Registro de Productos\n1-Registrar Producto\n2-Consultar Producto\n3-Listar Productos\n4-Salir")
  try:
   op=int(input("Ingrese Opción: "))
   if op==1:
      while sw==1:
        encontrado=False
        codigo=input("Ingrese código de producto: ")
        if len(codigo)==4:
           if len(productos)==0:
             break
           else:
             for prod in productos:
               if prod[0]==codigo:
                 encontrado=True
                 break 
           if encontrado:
              print("Código ya existe")
           else:
             break
        else:
          print("El codigo debe tener 4 dígitos")
      nombre=input("Ingrese nombre de producto: ")
      while True:
        precio=int(input("Ingrese precio de producto: "))
        if precio>0:
          break
        else:
          print("El precio debe ser mayor a 0")
      while True:
        stock=int(input("Ingrese stock de producto: "))
        if stock>0 and stock<100:
          break
        else:
          print("El stock debe ser mayor a 0 y menor a 100")
      producto=[codigo,nombre,precio,stock]
      productos.append(producto)
   elif op==2:
    cod=input("Ingrese codigo a consultar")
    valido=False
    for prod in productos:
      if prod[0]==cod:
        print("Código:",prod[0])
        print("Nombre:",prod[1])   
        print("Precio:",prod[2])   
        print("Stock:",prod[3])
        valido=True
        break
    if valido:
        print("Producto encontrado")
    else:
        print("Producto no encontrado") 
   elif op==3:
    print("Listado de Productos")
    print("********************")
    for prod in productos:
        
         print("Código:",prod[0])
         print("Nombre:",prod[1])   
         print("Precio:",prod[2])   
         print("Stock:",prod[3])
         print("********************")
    
   elif op==4:
    print("Gracias! Hasta Luego")
    break     

  except:
   print("Ingrese data válida")