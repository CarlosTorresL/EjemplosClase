import os
import time 
import msvcrt


switch=1

while switch==1:

 print("Este es una prueba de menú\n1-Sumar dos números\n5-Salir\n")

 opcion=int(input("Ingrese su opción"))
 
 if opcion==1:
    os.system("cls")
    num1= int(input('Ingrese el nro 1\n'))
    num2= int(input('Ingrese el nro 2\n'))
    suma=num1+num2
    print (f'la suma de ambos números es: {suma}')

 elif opcion==5:
    for x in range(5,0,-1):
        os.system("cls")
        print(f"Saliendo en {x}")
        time.sleep(1)

        os.system("cls")
    switch=0
 else:  
    print('Opción no Válida')
    print('Presione tecla para continuar')
    msvcrt.getch()
    os.system("cls")