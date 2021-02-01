"""El objetivo de estas funciones anónimas, es poder simplificar la escritura cuando trabajamos con funciones de orden superior,
 por ejemplo, la recientemente vista función FILTER.
Probemos modificar el código reemplazando las funciones simples con funciones LAMBDA en el ejemplo de FILTER con múltiplos de 3 y de 5.

MANERA NORMAL
lista=[23,12,4,7,33,75,2,9,10]
def m3(v):
    if(v % 3==0):
        return True

def m5(v):
    if(v % 5==0):
        return True

print(list(filter(m3,lista)))
print(list(filter(m5,lista)))
"""
# la forma de lambda
lista=[23,12,4,7,33,75,2,9,10]

print(list(filter(lambda x : x % 3==0, lista)))
print(list(filter(lambda x : x % 5==0, lista)))