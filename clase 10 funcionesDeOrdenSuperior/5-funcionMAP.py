"""Esta función es de uso similar a la función FILTER con la diferencia que la función simple recibida como parámetro, se aplica a todos
los elementos de la lista que se pasa junto con la función y el resultado es una lista con la misma cantidad de elementos que la lista
original.

Veamos un ejemplo sencillo, tenemos una lista con números y una función que recibe un valor y lo eleva al cuadrado.
Mediante el uso de MAP aplicamos la función a todos los elementos de la lista.
"""

valor=[2,3,4,5,6,7,8,9,10]
valor2=[1,4,3,7,4,12,9,0,1]
def cuadrado(x):
    return pow(x,2)

print(list(map(cuadrado,valor)))

# Podemos modificar el código del ejemplo para utilizar una función LAMBDA:
print(list(map(lambda x: pow(x,2),valor)))

"""Uno de los beneficios de la función MAP es que evita el uso de estructuras de repetición.
Además, podemos utilizarlo sobre mas de una lista u objeto iterable, por ejemplo, tenemos dos listas de números y queremos obtener
la suma de los elementos que tengan el mismo índice
"""
print(list(map(lambda x,y: x+y ,valor,valor2 )))#sumamos los dos array cada posicion con cada posicion