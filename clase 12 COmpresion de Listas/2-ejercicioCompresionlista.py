"""OTRO EJEMPLO: un último ejemplo donde veremos cómo crear una lista a partir de otra, y ambas listas creadas mediante comprensión en 
una sola línea de código.

Problema: crear una lista que contenga los números pares, de una lista que contiene los números del 1 al 10 elevados al cubo.
"""
# FORMA TRADICIONAL
potencia=[]
for x in range(1,10):
    potencia.append(x**3)
pares=[]
for x in potencia:
    if x % 2 ==0:
        pares.append(x)
print(pares)

# COMPRECION DE LISTA
# hacemos el for y a la hora de recorrer  en ves de usar range entre corchetes elevamos al cubo con bucle del 1 al 10 para despues 
# preguntar cuales son pares
listaAll=[x for x in [z**3 for z in range(1,10)] if x % 2 ==0 ]
print(listaAll)