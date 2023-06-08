import os
import time
#import msvcrt

x=1
pago=0
dinero=0
vuelto=0
sumapago=0
pago2=0
variablenueva=0

while dinero<=0:
 dinero=int(input("Ingrese la cantidad de dinero a pagar que sea mayor a CERO:\n"))
 time.sleep(1)
 #os.system("cls")
 monto=dinero

while sumapago<dinero:
  i=True
  while i:
     pago=int(input(f"Ingrese monto a pagar nro {x}: "))
     if pago<=0:
      print("Ingrese monto mayor a cero")
      i=True
      time.sleep(2)
      #os.system("cls")
     else:
      monto=monto-pago
      sumapago=sumapago+pago
      if monto>0:
       print(f"Le queda por pagar: ${monto}")
       #print("Presione tecla para continuar")
       #msvcrt.getch()
      #os.system("cls")
      x+=1 
      i=False


if sumapago>dinero:
   vuelto=sumapago-dinero
   print(f"Se pasó del monto\nSu vuelto es: ${vuelto} ")
   print(f"Se hicieron {x-1} ingresos de pagos")
   #print("Presione tecla para continuar")
   #msvcrt.getch()
   #os.system("cls")
elif sumapago==dinero:
   print("Monto exacto pagado")
   print(f"Se hicieron {x-1} ingresos de pagos")