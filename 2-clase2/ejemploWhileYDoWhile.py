#while
"""contador=1
while contador<=10:
    print(contador)
    contador+=1
print("fin")"""

"""notas=[]
nota=0
while nota!=-1:
    nota=int(input("ingrese la nota del 1 al 10 y -1 para salir"))
    if(nota==-1):
        break
    notas.append(nota)
print("nostas ingresadas",notas)
print("nostas sumadas",sum(notas))
print("nostas promediadas",sum(notas)/len(notas))"""






#---------------------------------------------------------
#ya que el do while no existe se hace de esta manera
"""contador1=0
while True:
    print(contador1)
    contador1+=1
    if(contador1==11):
        break
print("fin do while")"""


#ciclo for 
numeritos=[1,2,3,4,5]
for item in range(0,len(numeritos)):
    print(numeritos[item])
print()
#for con tres valores
#A la función range() le podemos agregar un tercer valor, para indicarle el incremento o decremento que queremos obtener. 
#va del 0 hasta el 10 pero de dos en dos
for item in range(0,10,2):
    print(item)