"""La comprensión de listas nos permite resolver en pocas líneas de código, estructuras que normalmente nos llevarías varias líneas más.
Por ejemplo, si vamos queremos crear una lista con todas las letras de un mensaje, esto es lo que haríamos:
"""
lista=[]
for letras in 'taller integrador':
    lista.append(letras)
print(lista)

print()
print("compresion de lista")
"""Si aplicamos la comprensión de listas de Python, lo haríamos de esta manera:"""
# La sintaxis es muy sencilla, definimos la lista como veníamos haciendo, y dentro ponemos la variable donde vamos a guardar el
#  recorrido del bucle, y a continuación el bucle en una sola línea.
lista2=[letras for letras in 'taller integradoe']
print(lista2)

print()
print("otro ejemplo de forma normal normal")
"""OTRO EJEMPLO: queremos hacer una lista de los números del 10 al 20 elevados al cubo. La siguiente es la forma tradicional de 
resolverlo:
"""
lista3=[]
for x in range(10,21):
    lista3.append(x**3)
print(lista3)
print()
print("ejemplo de compresion de lista")
lista4=[(x**3) for x in range(10,21)]
print(lista4)


print()
print("otro ejemplo de forma normal normal con condicional")
"""OTRO EJEMPLO: Vamos a agregarle a nuestra lista una condición, por ejemplo, queremos crear una lista que contenga los múltiplos de
3 que están entre el 1 y el 20.
Método tradicional:
"""
lista5=[]
for x in range(1,21):
    if x % 3 == 0:
        lista5.append(x)
print(lista5)

print()
print("otro ejemplo de forma COMPRECION LISTA normal con condicional")
# LISTA = [Variable a recorrer - Iteración - Condición]
lista6=[x for x in range(1,21) if x % 3 ==0]
print(lista6)
