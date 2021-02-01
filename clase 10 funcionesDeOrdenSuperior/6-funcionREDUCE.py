"""Esta es otra función de orden superior, toma como argumentos una colección de datos y los reduce a un solo valor en base a una
 función simple que también le pasamos como argumento.
Esta función se encuentra dentro del módulo FUNCTOOLS, por lo que deberemos importarla.
Por ejemplo, queremos sacar la sumatoria de todos los valores cargados en una lista.
"""
from functools import reduce
valor=[2,3,4,5,6,7,8,9,10]

def sumar(a,b):
    return a+b
    #Lo que hace el código es sumar todos los valores de la lista, REDUCE va haciendo el acumulado de cada suma antes de seguir con el
    #siguiente elemento de la lista.
print(reduce(sumar,valor))

# También podemos hacer uso de una función LAMBDA:
print(reduce(lambda x,y: x+y,valor))