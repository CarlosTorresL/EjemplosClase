import time

divisor=0
c=True

while c:
  x=int(input("Ingrese un número para saber si es primo: "))
  for i in range(2,x+1):
    #print(i)
    if x%i==0:
      divisor+=1
  if divisor>1:
    print(f"Número '{x}' no es primo")
  else:
    print(f"Número '{x}' es primo")
  time.sleep(2)
  
 
  x=input("Continuar\n1-Si\n2-No\n")
  if x=="1":
    c=True
  else:
    c=False