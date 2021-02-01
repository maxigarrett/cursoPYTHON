class Auto:
    color='sin dato'
    puerta='sin dato'
    combutibble='sin dato'

    # simpre hay que pasarle por parametro a los metodos self para que funcione
    # en caso de usar mas atributos en la funcion separ en comas y el self  se ecribe una sola vez 
    def pintar(self,pintura):
        # el self es lo mismo que el this es para referenciar a el atributo
        self.color=pintura
    

# instancio un objeto
fiat= Auto()
fiat.pintar('rojo')
print(fiat.color)

# tambien se puede agregar atributos que no existan en la clase
fiat.ruedas=4
print('ruedas',fiat.ruedas)