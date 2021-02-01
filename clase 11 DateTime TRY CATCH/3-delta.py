"""Veamos como sumarle una determinada cantidad de tiempo a nuestro objeto fecha.
Lo primero es crear un objeto del tipo TIMEDELTA en el que dejaremos especificados los valores que serán sumados a nuestra fecha, 
por ejemplo, queremos crear un delta que le sume a nuestra fecha (y a todas las fechas que necesitemos) 4 días y 17 horas.
"""

import datetime

fecha=datetime.datetime.now()
sumar=datetime.timedelta(days=4,hours=17)
nueva_fecha=fecha+sumar
print("actual",fecha.strftime('%A %d %B'))
print("sumamos 4 dias y 17 hs",nueva_fecha.strftime('%A %d %B'))