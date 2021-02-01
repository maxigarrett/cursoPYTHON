"""Hacer un menú de cuatro opciones, que le permita al usuario navegar por cuatro módulos diferentes del programa. Mostrar en
cada módulo un título diferente para verificar que funciona correctamente"""

bol=True
print("elija la opcion del mensaje que quiere ver")
print()
print()
eleccion=int(input("elija una opcion \n 0 SALIR \n 1-HOLA \n 2-ADIOS \n 3-COMO ESTAS \n 4-SUERTE \n"))
while bol:
    if (eleccion==0):
        break
    elif (eleccion==1):
        print("HOLA")  
    elif (eleccion==2):
        print("ADIOS")
    elif (eleccion==3):
        print("COMO ESTAS")
    elif (eleccion==4):
        print("SUERTE")
    eleccion=int(input("elija una opcion \n 0 SALIR \n 1-HOLA \n 2-ADIOS \n 3-COMO ESTAS \n 4-SUERTE \n"))
    print()
print("chau gracias por utilizar este menu")
    


