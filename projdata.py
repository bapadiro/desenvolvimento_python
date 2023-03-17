def isUltimoDiaDoMes(dia, mes, ano):
    #TODO fazer essa função
    return False

def amanha(dia, mes, ano):
    if (isUltimoDiaDoMes(dia, mes, ano)):
        if mes != 12:
            return 1, mes + 1, ano
        else:
            return 1, 1, ano + 1
    else:            
        return dia + 1, mes, ano

def dataFutura(dia, mes, ano, qtdDias):
    data = amanha(dia, mes, ano)    
    i = 1    
    while i < qtdDias:
        data = amanha(data[0], data[1], data[2])
        i = i + 1

    return data[0], data[1], data[2]

resp = dataFutura(20, 5, 2020, 11)
print(resp)


