class Persona:
    persona=''
    def __init__(self,nombre):
        self.nombre=nombre
    
    # metodo destructor
    def __del__(self):
        print('La persona ',self.nombre,' ha sido eliminada.')

persona = Persona('jose')
print('El nombre de la persona creada es ',persona.nombre)
# se eleimina la persona que le pasemos por parametros
del(persona)
