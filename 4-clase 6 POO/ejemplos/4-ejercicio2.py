"""Modificar la clase del ejercicio anterior para que reciba la operación a realizar, que puede ser suma, resta o producto y 
dos números con los cuáles hará dicha operación y muestre el resultado."""


class Calculadora:
    def sumar(self,proceso,a,b):
        if(proceso=="sumar"):
            print('la suma es:', a+b)
        elif(proceso=='restar'):
            print('la resta es:', a-b)
        elif(proceso=='dividir'):
            print('la division es:', a/b)
        elif(proceso=='multiplicar'):
            print('la multiplicacion es:', a*b)
cal=Calculadora()
cal.sumar('multiplicar',5,4)