#ex 13 lista 3
#ex 14 lista 3
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

dataValida = True

if dia < 1 or dia > 31 or mes < 1 or mes > 12:
    dataValida = False
if dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    dataValida = False

if mes == 2 and dia >= 29:
    #teste do ano bissexto
    if dia > 29:
        dataValida = False
    elif ano % 4 != 0  or  ano % 100 == 0 and ano % 400 != 0:
        dataValida = False

if dataValida:  #dataValida == True
    print("Data válida")
else:
    print("Data inválida")