cripto=[]
cant=[]
cotiz=[]
i=0



while i<2:
    cripto.append(input("Ingrese el nombre de la moneda: "))
    cant.append(float(input("ingrese la cantidad de: "+cripto[i]+": " )))
    cotiz.append(float(input("ingrese la cotizacion de: "+cripto[i]+": ")))
    i=i+1

i=0

while i<2:
    print("Moneda:",cripto[i],"cantidad: ",str(cant[i]),"cotizacion: ",str(cotiz[i]))
   
    i=i+1
    

