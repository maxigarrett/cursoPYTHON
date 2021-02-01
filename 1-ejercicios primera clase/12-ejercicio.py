"""Escribir un programa que llene una lista con 50 números al azar y muestre por pantalla el número (o números) que más se
repite. """
from random import randint,random
lista=[]
for i in range(1,50):
    lista.append(randint(0,50))
print(lista)
print()
print("lista nueva")
for i in range(0,len(lista)):
    if(lista[i]==i):
        print(i)

