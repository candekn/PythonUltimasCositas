import requests
#
# q : La ciudad, el pais
# units: La medida en que se muestran los datos, por defecto es en F, si ponemos metrics cambia a C
# appid: es el apikey
#
r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Buenos%20Aires,AR&units=metric&appid=")
print("Codigo de estado: ",r.status_code)
temperatura = r.json()["main"]["temp"]
presion = r.json()["main"]["pressure"]
humedad = r.json()["main"]["humidity"]
nubes = r.json()["clouds"]["all"]
viento = r.json()["wind"]["speed"]
visibilidad = r.json()["visibility"]

print("Temperatura actual: ",temperatura)
print("Presion: ",presion)
print("Lo que mata: ",humedad)
print("Nubes: ",nubes)
print("Visibilidad: ",visibilidad)
print("Viento: ",viento)

if humedad>50 and presion>1013 and nubes >50 and visibilidad<10000 and viento>0:
    print("******Alta probabilidad de lluvia******")
    
