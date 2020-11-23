import random
moneda= str(input("Ingrese la moneda"))
cantidad=float(input("ingrese la cantidad de monedas"))
count=0

while count< 7:
    profit=random.uniform(-0.03,0.03)
    cantidad=cantidad+(cantidad*profit)
    count=count+1
print("Saldo de: ", moneda,"el dia", count,"es de:",cantidad,"con una ganancia de",profit*100,"%")