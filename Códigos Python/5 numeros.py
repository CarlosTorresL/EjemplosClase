may_0=0
men_0=0
igual_0=0
i=1
#Ingreso número por teclado y lo guardo en num
while i<=5:
    num=int(input(f"Ingrese el número {i}: "))
    if num>0:
        may_0=may_0+1
    elif num==0:
        igual_0=igual_0+1
    else:
        men_0=men_0+1
    i=i+1

print(f"NUMEROS MAYORES A 0: {may_0}\nNUMEROS MENORES A 0: {men_0}\nNUMEROS IGUALES A 0: {igual_0}")

