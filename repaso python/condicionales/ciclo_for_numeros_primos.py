inf= int(input("ingrese el numero inferior: "))
sup=int(input("ingrese el numero superior: "))
print("los # primos entre",inf, "y ", sup," es: ")
for num in range(inf,sup+1):
    for i in range(2, num):
        if (num%i)==0:
            break
        elif i ==num-1:
            print(num,"es un numero primo")