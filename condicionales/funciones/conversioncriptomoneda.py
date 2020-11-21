bitcoin= float(input("ingrese la cantidad de bitcoin: "))
Ethereum= float(input("ingrese la cantidad de Ethereum: "))
Litecoin=float(input("ingrese la cantidad de Litecoin: "))
TotalEUR=0

def ConversionCriptomoneda(bitcoin,Ethereum,Litecoin):

    bitEUR=6500
    
    ETEUR=493
    
    LTEUR=104
    
    TotalEUR=(bitcoin*bitEUR)+(Ethereum*ETEUR)+(Litecoin*LTEUR)

    print("el total de Euros es",TotalEUR)

ConversionCriptomoneda(bitcoin,Ethereum,Litecoin)