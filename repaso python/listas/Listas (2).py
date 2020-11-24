import requests
_ENDPOINT = "http://api.binance.com"

def _url(api):
    return _ENDPOINT+api

def get_price(moneda):
    return requests.get(_url("/api/v3/ticker/price?symbol="+moneda))
   
def esmoneda(moneda):
    criptos = ["BTC", "BCC","LTC","ETH","ETC","XRP"]
    return  moneda in criptos

def esnumero(numero):
    return numero.replace('.','',1).isdigit()

monedas=[]
cantidades=[]
cotizaciones=[]
i=0

while i<3:
    moneda=input("Ingrese el nombre de la moneda")
    while not esmoneda(moneda):
        print("Moneda invalida")
        moneda=input("Ingrese el nombre de la moneda")
    else:
        monedas.append(moneda)
        data = get_price(moneda+"USDT").json()
        cotizaciones.append(float(data["price"]))
        cantidad =input("Indique la cantidad de "+moneda+": ")
        while not esnumero(cantidad):
            cantidad: input("Indique la cantidad de "+moneda+": ")
        else: 
            cantidades.append(float(cantidad))
        i+=1
i=0
total=0

while i<3:
    total+=cantidades[i]*cotizaciones[i]
    print("Moneda:", monedas[i],
        "Cantidad: ", cantidades[i],
        "Cotizacion",cotizaciones[i],
        "Cantidad de USDT",cantidades[i]*cotizaciones[i])
    i+=1

print("Total de USDT es" , str(total))