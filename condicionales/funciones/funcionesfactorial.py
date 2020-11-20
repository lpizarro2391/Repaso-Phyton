n= int(input("Ingrese el numero a calcular el factorial"))
def factorial(n):
    fact=1
    for elem in range(1,n+1):
        fact=elem*fact
    return fact
print("El factorial de ",n,"es: ",factorial(n))