x= int(input("Ingrese el primer numero x: "))
y=int(input("ingrese el segundo numero y: "))
z=int(input("Ingrese el tercer numero z: "))

def max(x,y):
    if x > y:
        maximo = x
    else:
        maximo = y
    return maximo
print("el numero maximo entre", x, ",", y, "y",z, "es",max(max(x,y),z))