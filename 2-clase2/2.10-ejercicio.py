"""Modificar el ejercicio anterior, para que el usuario pueda en cada opción del programa, ingresar dos números enteros y que en
 cada opción a esos números se les aplique una suma, una resta, una división o una multiplicación.
Agregar una nueva opción para que el programa funcione permanentemente hasta que el usuario la seleccione y el programa finalice
 su ejecución. 
"""

bol=True
print("elija la opcion del mensaje que quiere ver")
print()
numero1=int(input("ingrese el primer numero"))
numero2=int(input("ingrese el segundo numero"))
print()
eleccion=int(input("elija una opcion \n 0 SALIR \n 1-SUMAR \n 2-RESTAR \n 3-MULTIPLICACION  \n 4-DIVISION \n"))
while bol:
    if (eleccion==0):
        break
    elif (eleccion==1):
        print(numero1,"+",numero2,"=",(numero1+numero2))

    elif (eleccion==2):
        print(numero1,"-",numero2,"=",(numero1-numero2)) 

    elif (eleccion==3):
        print(numero1,"x",numero2,"=",(numero1*numero2))

    elif (eleccion==4):
        if(numero2==0):
            print("no se puede dividir por 0 \n")
            numero2=int(input("ingrese el segundo numero de nuevo mayor a 0 por favor"))
        print(numero1,"/",numero2,"=",(numero1/numero2)) 

    eleccion=int(input("elija una opcion \n 0 SALIR \n 1-SUMAR \n 2-RESTAR \n 3-MULTIPLICACION  \n 4-DIVISION \n"))
    print()
print("chau gracias por utilizar este menu")