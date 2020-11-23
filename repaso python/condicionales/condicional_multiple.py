peso= float(input("ingrese el peso en kg:"))
altura=float(input("ingrese la altura mts:"))
IMC= peso/altura**2

if IMC<18.5:
    print("bajo peso")
elif IMC >=18.5 and IMC <25:
    print("Normal")
elif IMC>=25 and IMC<30:
    print("Sobrepeso")
elif IMC>=30 and IMC<35:
    print("Obesidad Leve")
elif IMC>=35 and IMC<40:
    print("Obesidad Leve")
else:
    IMC>40
    print("Obesidad Morbida")
    
