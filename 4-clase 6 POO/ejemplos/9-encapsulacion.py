class Persona:
    # se encapsula en privado con dos guiones por delante
    __nombre="maxi var privada"

    # metodo seter para modificar el valor de la variable
    def set_nombre(self,nombre):
        self.__nombre=nombre
    #metodo get para obtener el valor de la variable 
    def get_nombre(self):
        return self.__nombre


    def get_saludar(self):
        return self.__saludar()    
    #metodo encapsulado 
    def __saludar(self):
        print("metodo pricado")

persona1=Persona()
persona1.set_nombre('jorge')
print(persona1.get_nombre())
persona1.get_saludar()
