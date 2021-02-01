#Si creamos tres listas. La primera contiene 4 números, la segunda contiene 5 letras y en la tercera le cargamos como elementos
#las dos listas anteriores.¿Cuántos elementos contendrá la tercera lista? Demostrar mediante un breve código.

lista=[1,2,3,4]
lista2=["a","b","c","d","e"]
lista3=[]
lista3.append(lista)
lista3.append(lista2)
contador=[]
for item in range(0,len(lista3)):
    contador+=lista3[item]#agregamos al array contador todo el array lista3 para que sean uno solo

    
print("la lista tiene",len(contador),"elementos")


