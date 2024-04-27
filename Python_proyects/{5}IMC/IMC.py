#calculadora de indice de masa corporal
peso_=float( input("Ingrese su peso en Kilogramos (Kg) "))
altura_=float( input("Ingrese su altura en metros (m) "))
IMC_=(peso_/(altura_ ** 2))
if IMC_ <  18.5:
    print("Bajo peso IMC=",round(IMC_,4))
elif IMC_<=24.9 and IMC_>=18.5:
    print("Peso normal IMC=",round(IMC_,4))
elif IMC_<=29.9 and IMC_>=25:
    print("Sobrepeso IMC=",round(IMC_,4))
elif  IMC_>=30:
    print("obesidad IMC=",round(IMC_,4))
else:
    print("dato no valido")
