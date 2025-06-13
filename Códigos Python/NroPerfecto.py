suma=0
print("NÚMERO PERFECTO 1")
x=int(input("Ingrese el número: "))

for i in range(1,x):
  if x%i==0:
    suma=suma+i

if suma==x:
  print(f"El número '{x}' es perfecto!")
else:
  print(f"El número '{x}' NO es perfecto!")
