"""Modificar el siguiente código para que no de error al recibir un argumento que no es del tipo Lista.

def lista(argumento):
    print(argumento)
    print(len(argumento))
lista([1,"hola",['a','b','c']])
"""

def lista(argumento):
    if(lista==[]):
        print(len(argumento))
    else:
        print(argumento)
        
lista([1,"hola",['a','b','c']])
