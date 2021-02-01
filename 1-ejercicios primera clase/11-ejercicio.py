"""Escribir una función que encuentre los números primos comprendidos entre dos números enteros ingresados por teclado."""

primos = []
def primo(num):
    #un numero n es primo si (n-1)! + 1 es multiplo de n
    factorial = 1

    for i in range(1, num):
        factorial*=i

    if (factorial+1)%num == 0:
        primos.append(num)

num1 = int(input("Ingrese el numero donde comienza el intervalo: "))
num2 = int(input("Ingrese el numero en el que termina el intervalo: "))

if num1<num2:
    for i in range(num1,num2):
        primo(i)
else:
    print("El segundo numero debe ser mayor que el primero.")

print("Los numeros primos entre",num1,"y",num2,"son",primos)
