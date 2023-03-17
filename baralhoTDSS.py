def imprimeCarta(carta):
    if carta[0] == 1:
        return "A" + carta[1]
    else:    
        return str(carta[0]) + carta[1]

def imprimeMao(colecao):
    resp = ""
    for c in colecao:
        resp = resp + " " + imprimeCarta(c)

    return resp    

#retorna um baralho
def getBaralho():
    ases = ((1, "♣"), (1, "♥"), (1, "♠"), (1, "♦"))
    dois = ((2, "♣"), (2, "♥"), (2, "♠"), (2, "♦"))
    return ases + dois

mao = getAses()
print(imprimeMao(mao))

