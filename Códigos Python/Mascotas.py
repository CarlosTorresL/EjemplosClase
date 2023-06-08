import random as r
import os
import time
import msvcrt as m

mascotas=[]
mascota=[]

def limpia_pantalla(seg):
   time.sleep(seg)
   os.system("cls")

def menu():#Función retorna la opción elegida al MAIN
    print("1.Registro de mascota")
    print("2.Buscar mascota")
    print("3.Reportes de mascotas")
    print("4.Listar mascotas")
    print("0.Salir")
    op=int(input("Ingrese Opción:\n>"))
    return op

def listar_mascotas():
    for lista in mascotas:
       for mascota in lista:
          print(mascota)
       print("---------------")


def registrar():
    
    while True:#Valida que rut sea alfanumérico y que tenga entre 8 y 9 caracteres
     idmascota= input("Ingrese ID Mascota: ")
     if (len(idmascota)==5) and idmascota.isdigit():
        break
     else:
        print("Ingrese ID válido")
    while True:
       
     nom_mascota=input("Ingrese Nombre Mascota: ")
     nom_dueno=input("Ingrese Dueño Mascota: ")
     if len(nom_mascota)<1 or len(nom_dueno)<1:
        print("Debe ingresar nombre")
     else:
        break
    
    while True:
      reg=int(input("1.Perro 2.Gato: "))
      if reg==1:
        tipo="P"
        break
      elif reg==2:
        tipo="G"
        break
      else:
        print("Ingrese opción válida")
    
    mascota=[idmascota,nom_mascota,nom_dueno,tipo]
    mascotas.append(mascota)
    print("Registro Exitoso")
    limpia_pantalla(2)
def buscar(id):
    i=1
    for lista in mascotas:
       if lista[0]==id:#Recibe el rut ingresado en la opción 2 y se valida que sea igual al que hay en las listas
        print(f"ID Mascota: {lista[0]} ")
        print(f"Nombre Mascota: {lista[1]} ")
        print(f"Nombre Dueño: {lista[2]} ")
        if lista[3]=="P":
             print("Tipo:  Perro")
        else:
             print("Tipo:  Gato")
          
        print("----------------------")
        i=0
    
    if i==1:
       print("No se encontró a la mascota")
       limpia_pantalla(2.5)
    print("Presione cualquier tecla para continuar")
    m.getch()
    limpia_pantalla(2)
    
       
       
def reporte_mascota(tipo):
   cont=0
   print("------Reportes--------")
   for lista in mascotas:
      if lista[3]==tipo:
        cont+=1
        print(f"ID Mascota: {lista[0]} ")
        print(f"Nombre Mascota: {lista[1]} ")
        if lista[3]=="P":
             print("Tipo:  Perro\n")
        else:
             print("Tipo:  Gato\n")
        print(f"Sr/a: {lista[2]}\nA su mascota: {lista[1]}\nLe hacen falta {r.randrange(1,10)} vacunas ")
        print("----------------------")
   if tipo=="P":
        print(f"Hay registrados {cont} Perros en el Sistema")
   else:
        print(f"Hay registrados {cont} Gatos en el Sistema")
   print("Presione cualquier tecla para continuar")
   m.getch()
   limpia_pantalla(2)
#MAIN PROGRAM
while True:
  try:  
    opcion=menu()
    
    if opcion==1:
       registrar()
    elif opcion==2:
       while True:
         id=input("Ingrese ID de mascota a buscar\n")
         if (len(id)==5) and id.isdigit():
             buscar(id)
             break
         else:
             print("Ingrese ID válido")
         
    elif opcion==3:
       while True:
        tipo=int(input("¿Qué reportes desea ver?\n1.Perros\n2.Gatos\n>"))
        if tipo==1:
          t="P"
          break
        elif tipo==2:
          t="G"
          break
        else:
           print("Ingrese opción válida")
       reporte_mascota(t) 
    elif opcion==4:
        print(f"Listado de Mascotas\nTotal:{len(mascotas)}")
        listar_mascotas()

    elif opcion==0:
        for i in range(4,0,-1):
           print(f"Saliendo en {i}")
           limpia_pantalla(1)
        break
    else:
        print("Opción Incorrecta")  
  except :
     print("Error Inesperado")