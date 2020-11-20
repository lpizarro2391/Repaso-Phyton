n=int(input("Ingrese el valor a calcular el factorial:" ))
fact = 1
for elem in range(1,n+1):
    fact=elem*fact
    print("El factorial de",n,"es",fact)