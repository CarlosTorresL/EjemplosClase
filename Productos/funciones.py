import os
import time as t

producto=[]
productosGeneral=[]

def limpiarPantalla():
    t.sleep(2)
    os.system("cls")
    
def menu():
    print("1.Registrar Producto\n2.Listar Productos\n3.Buscar Producto\n0.Salir")
    op=input("Elija Opción: ")
    return op


def registrarProd():
    
    while True:
     codigo=input("Ingrese código (4 caracteres): ")
     if len(codigo)==4:
         break
     else:
        print("Ingrese código válido")

    nombre=input("Ingrese nombre del producto: ")
    
    
    precio=(input("Ingrese precio $: "))
    while not(precio.isdigit):
     precio=(input("Ingrese precio $: "))
     
    precio=int(precio)
    
    stock=int(input("Ingrese Stock: "))
    while stock<=0 or stock>=100:
      stock=int(input("Ingrese Stock: "))
    
    producto=[codigo,nombre,precio,stock]
    productosGeneral.append(producto)
    

def listarProd():
    print("LISTADO DE PRODUCTOS:")
    print("---------------------")
    for lista in productosGeneral:
            
            print(f"Código: {lista[0]} ")
            print(f"Nombre: {lista[1]} ")
            print(f"Precio: {lista[2]} ")
            print(f"Stock: {lista[3]} ")
            print("***************")
            
def buscarProd(cod):
    i= False
    for lista in productosGeneral:
        if lista[0]==cod:
            print(f"Código: {lista[0]} ")
            print(f"Nombre: {lista[1]} ")
            print(f"Precio: {lista[2]} ")
            print(f"Stock: {lista[3]} ")
            print("***************")
            i=True
            
        
    if not i:
        print("No existe el producto")