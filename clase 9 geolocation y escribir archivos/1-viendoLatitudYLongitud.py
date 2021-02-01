# importamos el modulo pero primero lo instalamos en la consola con:  pip install geopy
from geopy.geocoders import Nominatim

geolocator=Nominatim(user_agent="gma")

# creamos en una lista los domicilios 
lista=["malaspina,396,Rio Gallegos,Argentina", "CRISTOBAL COLON ,107,Rio Gallego,Argentina"]

# nos traemos su latitud y longitud
for i in lista:
    location=geolocator.geocode(i)
    print((location.latitude,location.longitude))
    print(location.address)
    