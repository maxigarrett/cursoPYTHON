class Auto:
    color=''
    puertas=0
    def __init__(self,color,puertas):
        self.color=color
        self.puertas=puertas

auto1=Auto('rojo',4)
print("el auto tiene color",auto1.color,'y tiene ',auto1.puertas,'puertas')