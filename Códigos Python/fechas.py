#from IPython.core.display import clear_output
#import IPython
from datetime import datetime

import time
import os
import msvcrt

#Función para retornar la fecha actual
def fecha(date): 
  months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] 
  #print("Tipo de dato: ",type(months))
  time.sleep(1)
  day = date.day 
  days = ("Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo")
  #print("Tipo de dato: ",type(days))
  time.sleep(1)
  dia = days[date.weekday()] 
  dia2 = date.isocalendar()[2]-1
  month = months[date.month - 1] 
  year = date.year 
  messsage = "{} {} de {} del {} y es el día nro {} de la semana".format(dia,day, month, year,dia2)
 
  return messsage
#Limpia pantalla
os.system("cls")
#Solicita ingresar una tecla específica para continuar
print("Presione 'ñ' para continuar...")
key = None
while key != 'ñ':
    key = msvcrt.getwch()
#Solicita presionar cualquier tecla para continuar
print("Presione alguna tecla para continuar...")
msvcrt.getch()
os.system("cls")
print("Cargando..")
#Tiempo de Espera
time.sleep(2)
os.system("cls")


#Asignación de hora actual y fecha con isocalendar(AÑO-NRO SEMANA-NRO DE DIA EN LA SEMANA)
now = datetime.now() 
print(fecha(now))
print("\nFecha con ISOCALENDAR")
print(datetime.now().isocalendar())

#HORA
tiempo=datetime.now().time()
hora=tiempo.hour
min=tiempo.minute
sec=tiempo.second
if sec<10 and sec>0:
  print(f"Hora actual: {hora}:{min}:0{sec}")
else:
  print(f"Hora actual: {hora}:{min}:{sec}")