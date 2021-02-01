def m2(v):
    if v % 2==0:
        print("es multiplo de 2")
    else:
        print("no es multiplo de 2")
def m3(v):
    if v % 3==0:
        print("es multiplo de 3")
    else:
        print("no es multiplo de 3")
# funcion de orden superior
def multiplo(v,fn):
    return fn(v)


# cuerpo del programa
multiplo(12,m2)
multiplo(12,m3)
multiplo(4,m3)
"""Lo que hicimos fue definir dos funciones (m2 y m3) que se encargan de recibir un número y mostrar por pantalla si el número recibido es múltiplo o
 no de dos (m2) y lo mismo para verificar si es múltiplo o no de 3 (m3).
A continuación, definimos nuestra función de orden superior (múltiplo) que además de recibir un valor, también recibe por parámetro otra función.
Para invocarla lo hacemos como a cualquier otra función a la que le pasamos parámetros.
"""