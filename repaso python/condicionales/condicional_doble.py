x= int(input("ingrese las horas trabajadas en la semana"))
pago_hora=10
if x<=40:
        Monto_pago_hora=pago_hora*x
        print("Total a cobrar:",str(Monto_pago_hora))
else:
        sobretiempo=x-40
        total_cobro=pago_hora*x + 1.5*sobretiempo
        print("Total a cobrar:",str(total_cobro))



