""""Escribir un programa que le pida al usuario que ingrese un número por teclado, lo eleve al cubo y muestre el resultado por 
pantalla. El programa deberá seguir funcionando hasta que el usuario ingrese el número cero."""

numero=int(input("ingrese un numero y sera elevado al cubo"))
print()
while (numero!=0):
    desicion=int(input("desea salir precione el 0 y se mostrara el resultado de lo contrario se le pedira que ingrese otro numero"))
    print()
    if(desicion==0):
        break
    else:
        print()
        numero=int(input("ingrese un numero nuevo  y sera elevado al cubo"))
numero=numero**3
print(numero)