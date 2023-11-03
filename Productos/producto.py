from funciones import *


while True:

 op=int(menu())

 if op==1:
    registrarProd()
    limpiarPantalla()
 elif op==2:
    listarProd()
    print("Presione una tecla")
    input(">")
    limpiarPantalla()

 elif op==3:
     cod=(input("Ingrese codigo a buscar:"))
     buscarProd(cod)
     print("Presione una tecla")
     input(">")
     limpiarPantalla()
 elif op==0:
    print("Hasta Luego")
    limpiarPantalla()
    break

 else:
     print("Opción Inválida")
     limpiarPantalla()