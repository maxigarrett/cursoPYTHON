"""Python nos permite de manera muy sencilla establecer el valor de la DOCSTRING, lo que debemos hacer es insertar en la primera línea,
 después de la declaración de la variable, un comentario de triple comilla:"""
def sumar(a,b):
    """esta funcion recibe dos valores """
    return print("suma=",a+b)

sumar(1,1)

"""Si ejecutamos el código, no veremos ningún cambio, lo que debemos hacer para utilizar la documentación ingresada es hacer uso de la 
función HELP.
"""
help(sumar)