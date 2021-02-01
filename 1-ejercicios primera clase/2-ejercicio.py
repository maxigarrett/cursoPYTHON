#Desarrollar un programa que solicite al usuario los lados de un rectángulo y calcule su perímetro y su superficie.
#Informar ambos resultados por pantalla.


lado1=int(input("ingrese la base del triangulo"))
lado2=int(input("ingrese la altura del triangulo"))
print()
perimetro=lado1*2 + lado2*2
superficie=lado1*lado2
print("perimetro del rectangulo=",perimetro)
print("superficie del rectangulo=",superficie)