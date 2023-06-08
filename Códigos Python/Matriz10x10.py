matriz=[]
cont=1
#Se llena la matriz con los asientos con números del 1 al 100
for i in range(4):
    lista=[]
    for j in range(4):
        lista.append(cont)
        cont+=1
    matriz.append(lista)


vendidos=[]

while True:
    ocupado=False
    print("ASIENTOS DISPONIBLES")
    for lista in matriz:
     print(f"{lista}")
    print("Ingrese asiento")
    asiento=int(input(">"))
    for a in vendidos:
      if asiento==a:
         ocupado=True
    print(f"Asientos vendidos: {vendidos}")
    for i in range(4):
        for j in range(4):
            if matriz[i][j]==asiento:
                ocupado=False
                print("Asiento Disponible")
                matriz[i][j]="X"
                vendidos.append(asiento)
                break

    if ocupado:
        print("Asiento ya ocupado, elija otro")
    else:
       print("Asiento comprado, desea continuar? S/N")
       conti=input(">")
       if conti=="N":
           break
    

              