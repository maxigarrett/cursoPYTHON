#Escribir un programa que pida ingresar un número entero mayor que cero por teclado.
#Verificar si el número ingresado es múltiplo de  2, 3, 4, 5, 6, 7,8 o 9.
#Armar una lista con los números encontrados (por ejemplo, si el número ingresado es múltiplo de 3,6 y 7, armamos una lista que
#contenga estos tres números).
#Mostrar la lista por pantalla, ordenada de mayor a menor.
#En caso de que el número ingresado no sea múltiplo de estos números, mostrar por pantalla el mensaje “No se encontraron
#divisores exactos”.


numero=int(input("ingrese un numero entero"))

lista=[]
if(numero<=0):
    print("ingrese un numero mayor a 0")
for item in range(1,numero +1):#para q arranque de 1 y valla hasta el numero que digito el susuario
    if(numero % item==0):#si el numero que escribio el usuario dividido por los numero q recorremos da 0 es divisor 
        lista.append(item)
    
print("ingresaste el numero ",numero," y los multiplos son: ", lista)