criptos=("BTC","ETC","XRP","BCC","ETC")
i=0
total=0

while i<3:
    cripto= input("Ingrese el nombre de la moneda")
    if cripto in criptos:
        i+1
        cant=""
        while not cant.replace('.',',',1).isdigit():
            cant= input("Indique la cantidad de +"+cripto+".")
        else:
            cotiz=""
        while not cotiz.replace('.',',',1).isdigit():
            cotiz=input("Indique la cotizacion en USD de"+cripto+".")
        else:
            total= total+float(cant)*float(cotiz)
    else:
        print("Moneda Invalida")
    print("El total en USD que tiene el usuario es de",str(total))
        
        

 


    


