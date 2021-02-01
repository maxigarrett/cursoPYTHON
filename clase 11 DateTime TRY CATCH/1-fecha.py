import datetime

fecha=datetime.datetime.now()
print(fecha)#veremos la fecha actual con la Hs actual

print(fecha.year)#vemos el año accediendo con el metofo year de nueestro objeto fecha

print()
print("fecha actual usando todods los metodos")
print()
print("AÑO:",fecha.year)
print("MES:",fecha.month)
print("DIA:",fecha.day)
print("HORA:",fecha.hour)
print("MINUTO:",fecha.minute)
print("SEGUNDOS:",fecha.second)
print("MICROSEGUNDOS:",fecha.microsecond)

print()
print("fecha manual")
print()
fecha2=datetime.datetime(2020,12,31)#se cargan como una tupla o array y una ves creado no podemos modificarlo 
# fecha2.year=2222 esto tiraria error porque no se puede modificar

# LA FORMA DE MODIFICAA SERIA CON REPLACE
print (fecha2.replace(year=2021))
