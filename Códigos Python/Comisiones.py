import os
import time
import msvcrt

flag=True
while flag:
  nombre = input("Indique su nombre:\n")
  nombre=nombre.lower()
  if nombre.isalpha() and nombre!=" ":
     flag=False
  else:
     flag=True
     print("Ingrese Nombre válido\n")
     print("Presione una tecla para continuar")
     msvcrt.getch()
     os.system("cls")


os.system("cls")
time.sleep(2)

ventas = int(input("¿Cuánto ha vendido?\n"))
os.system("cls")
comisiones = round(ventas * 0.13)
total = round(ventas+comisiones)
nombre=nombre.upper()

print(f"HOLA USUARIO: {nombre}\nSUS VENTAS HAN SIDO: {ventas}\nLA COMISIÓN DEL 13% es: {comisiones}"
      f"\nEL TOTAL DE GANANCIA ES: {total}")