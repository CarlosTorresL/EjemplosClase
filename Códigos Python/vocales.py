vocal=0
consonante=0
flag=True

#Ciclo para preguntar por palabra válida(alfabeticos) y se pasa todo a minuscula
while flag:
  palabra=input(("Ingrese una palabra: "))
  if palabra.isalpha():
    palabra_min=palabra.lower()
    flag=False
  else:
    print("Ingrese palabra válida-Sin espacios ni caracteres no alfabeticos")
    flag=True

#Se recorre cada caracter en la palabra ingresada y se ve si es vocal o no
for x in palabra:
  if x in "aeiou":
    vocal+=1
  else:
    consonante+=1


print(f"Cantidad de Consonantes: {consonante}\nCantidad de vocales: {vocal}")