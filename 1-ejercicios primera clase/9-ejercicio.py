#Escribir una función en Python para calcular el factorial de un número entero positivo.
#Basarse en la siguiente definición:
#El factorial de un número entero positivo n, se define como el producto de todos los números enteros positivos menores o iguales
#a n. El factorial de cero es 1.
#Por ejemplo, el factorial de 4 será 4x3x2x1 = 24.


def factorial(num):
    if (num==0 or num==1):
        resultado=1
        print(resultado)
    else:
        cont=0
        for item in range(1,num):
            cont+=(num*item)
            var=print(num,'X',item,'=',cont)
        return var
            

factorial(4)