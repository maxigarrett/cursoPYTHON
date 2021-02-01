"""Escribir un programa que le solicite al usuario ingresar 10 palabras, luego le pida ingresar una más y le diga si esa última
palabra ingresada se encuentra entre las 10 palabras ingresadas anteriormente."""

array_palabras=[]
contador=0
print("ingrese 10 palabras")
print()
for item in range(1,4 +1):
    palabra=input("ingrese la palabra")
    array_palabras.append(palabra)

ultima_palabra=input("ingrese la palabra para buscar coincidencia")
for item in range(0,len(array_palabras)):
    if(array_palabras[item]==ultima_palabra):
        contador+=1

if (contador==1):
    print("palabra",ultima_palabra," encontrada")
else:
    print("palabra no encontrada") 