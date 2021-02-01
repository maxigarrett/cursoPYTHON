class Promocion_a():
    descuento_a = 10

class Promocion_b():
    descuento_b = 15

# heredeamos de dos clases diferentes
class Cliente(Promocion_a,Promocion_b):
    pass

maxi=Cliente()
print(maxi.descuento_a)
print(maxi.descuento_b)
