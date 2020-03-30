import requests
#TRabajando con la API de dolarsi
r = requests.get("https://www.dolarsi.com/api/api.php?type=cotizador")
#Recorro el json
for j in r.json():
    if j["casa"]["nombre"] == "Dolar": #busco Dolar
        dolar = j ["casa"] #Guardo los datos en var dolar
    
venta = dolar["venta"] #guardo en var el precio de venta
venta= venta.replace(",",".") #reemplazo la , por .
venta = float(venta) #convierto a float
print(type(venta)) #verifico que es el tipo correcto
#Y con eso ya puedo trabajar :)
