try:
    valor=int(input("ingrese  un numero"))
except :
    print("eeror")



# Si, por ejemplo, ponemos nuestro ejemplo dentro de una estructura WHILE, se seguiría ejecutando hasta que ingresemos
#  un valor correcto.
while (True):
    try:
        valor=int(input("ingrese  un numero"))
        break
    except :
        print("error ingresa un numero")
print("has ingresado un numero")