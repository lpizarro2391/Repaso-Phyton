n=int(input("Valor a calcular el factorial:"))
elem=1
fact=1

while elem<=n:
    fact=fact*elem
    elem=elem+1
    print("El factorial de",n,"es:",fact)

