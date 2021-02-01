"""Funciones de orden superior.
Repasemos el concepto de función de orden superior.
Si bien Python, es un lenguaje orientado a objetos, permite el desarrollo de aplicaciones o códigos de manera estructurada y funcional,
 lo cual no es un detalle menor para este lenguaje ya que una de sus principales aplicaciones es la resolución de problemas de ciencia e
ingeniería.Por eso es necesario comprender bien el uso de funciones y ver todas las opciones y herramientas que Python nos pone al 
alcance de la mano, una de ellas, es la función de orden superior.
Definimos una función de orden superior como aquella capaz de recibir como parámetro a otras funciones y devolver, en casos particulares,
una función como resultado.
Esto no es exclusivo de Python, está presente en otros lenguajes de programación y en temas matemáticos.

Resumiendo, y para que quede claro, decimos que una función de orden superior es una función que cumple al menos una de las siguientes
condiciones:

1-	Recibe una o más funciones como entrada.
2-	Devuelve una función como salida.

"""
def suma(a,b):
    return (a+b)
    
def resta(a,b):
    return (a-b)

def multiplicacion(a,b):
    return (a*b)

def division(a,b):
    return (a/b)

# Escribimos la función de orden superior.  
# la funcion que devuelve es una de las creadas tanto suma como resta,etc
def calcular(fn,a,b):
    return fn(a,b) 

# primer parametro la funcion suma despues los parametros de la funcion suma que recibe dos numeros
print(calcular(suma,1,1))
print(calcular(resta,1,1))