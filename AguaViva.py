mediaAnoAnterior = float(input("Media do ano passado: "))

consumoVigente = float(input("Consumo vigente: "))

valorUnitario = 0

if consumoVigente < 20:
    valorUnitario = 2.0
elif consumoVigente < 35:
    valorUnitario = 3.5
elif consumoVigente < 50:
    valorUnitario = 5.5
else:
    valorUnitario = 7.0

valorConta = consumoVigente * valorUnitario

if consumoVigente < mediaAnoAnterior:
    print("Valor ", valorConta)
    desconto = valorConta * 0.2
    print("desconto ", desconto)
    print("Valor final ", valorConta - desconto)

elif consumoVigente > mediaAnoAnterior * 1.1:
    print("Valor ", valorConta)    
    multa = valorConta * 0.3
    print("multa ", multa)
    print("Valor final ", valorConta + multa)

else:
    print("Valor final ", valorConta)    