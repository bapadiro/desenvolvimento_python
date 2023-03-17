import random

#retorno um conjunto de tamanho qtd
#contendo as pedras do domino
def distribui(pedras, qtd):
    retorno = []
    while qtd > 0:
        aux = pedras.pop(qtd)
        retorno.append(aux)
        qtd = qtd - 1
    
    return retorno

#retorna uma lista contendo 28 pedras que 
#representam o jogo de domino
def criaDomino():
    retorno = []
    j = 0
    while j <= 6:
        i = j
        while i <= 6:
            retorno.append([j, i])
            i = i + 1
        j = j + 1

    return retorno

def naoHaGanhador(listaA, listaB):
    if len(listaA) > 0 and len(listaB) > 0:
        return True
    else:
        return False

def mistura(lista):
    for x in range(1, 100):
        i = random.randint(0, len(lista)-1)
        j = random.randint(0, len(lista)-1)
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp

def colocaPedra(p, pontas, mesa):
    if len(mesa) == 0:
        mesa.append(p)
        pontas.append(p[0])
        pontas.append(p[1])

    elif p[0] == pontas[0]:
        mesa.insert(0, p)
        pontas[0] = p[1]
    
    elif p[0] == pontas[1]:
        mesa.append(p)
        pontas[1] = p[1]
    
    elif p[1] == pontas[0]:
        mesa.insert(0, p)
        pontas[0] = p[0]
    
    elif p[1] == pontas[1]:
        mesa.append(p)
        pontas[1] = p[0]            

def jogadaCpu(mao, pontas, extras):
    i = 0
    while i < len(mao):
        p = mao[i]
        if p[0] in pontas or p[1] in pontas:
            mao.pop(i)
            return p
        i = i + 1
        if i == len(mao) and len(extras):
            mao.append(extras.pop())  #pescando

    return [-1, -1]

def jogadaHomem(mao, pontas, extras):
    print(pontas)
    pos = -1
    while pos == -1 and len(extras) > 0:
       print(mao)
       pos = int(input("Digite a posicao da pedra ou -1 para compra: "))
       if pos != -1:
           pedra = mao.pop(pos)
           return pedra
       else:
           mao.append(extras.pop())    

    return [-1, -1] #passei a vez

domino = criaDomino()
mistura(domino)
maoHomem = distribui(domino, 7)
maoCpu = distribui(domino, 7)
mesa = []
extremos = []
i = 0
while naoHaGanhador(maoHomem, maoCpu):
    print(mesa)
    if i % 2 == 0:
        pedra = jogadaHomem(maoHomem, extremos, domino)
    else:    
        pedra = jogadaCpu(maoCpu, extremos, domino)
    i = i + 1
    colocaPedra(pedra, extremos, mesa)

