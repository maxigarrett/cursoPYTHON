"""LOCALE.
Un detalle importante a tener en cuenta a la hora de trabajar en Python con fechas, es el idioma en que está configurado,
para no complicar la experiencia a los usuarios.
Vamos a importar el módulo LOCALE y ver como tenemos configurado nuestro Python
"""
import datetime
import locale

# idioma=locale.setlocale(locale.LC_ALL,'')
# print(idioma)# no anda tendria que decir spanish_Argentina

"""En nuestro caso, lo tenemos bien configurado en nuestro Windows y esto es importante, porque dentro de las posibilidades que nos 
ofrece el módulo de fechas, es mostrar días y meses por su nombre, por lo que sería conveniente poder hacerlo en el idioma del usuario
final.
Si quisiéramos cambiar el idioma, por ejemplo, porque estuviese en inglés, solo debemos poner entre las comillas, las letras ‘es’.
Veamos un ejemplo de la utilidad de configurar el idioma y por qué debemos hacerlo para minimizar los resultados indeseados.

El método STRFTIME nos da información de la fecha con diferentes formatos, por ejemplo, %A simboliza el nombre del día, %d, el número 
de día y %B el mes.
Al no configurar el idioma en ES el resultado que vemos por pantalla no es el esperado.
"""

# locale.setlocale(locale.LC_ALL,'es') se tendria q ver la fecha en español pero no anda
fecha=datetime.datetime.now()
print(fecha.strftime('%A %d %B'))