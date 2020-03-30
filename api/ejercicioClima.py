import requests
r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Buenos%20Aires,AR&units=metric&appid=a41c27c9feb20967e253140e845e2322")
temp = r.json()["main"]["temp"]
presion = r.json()["main"]["pressure"]
humedad = r.json()["main"]["humidity"]
print("\nDatos: ")
if temp>25:
    print("Está caluroso")
elif temp <=25 and temp >=15:
    print("Está templado")
else:
    print("Está frío")
    

print("La temperatura es: ",temp)
print("La presion es: ",presion)
print("La humedad es: ",humedad)