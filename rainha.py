import stack

def criaMatriz(dimensao):
    matriz = []
    for i in range(dimensao):
        matriz.append([' '] * dim)
    return matriz

def possoColocarRainha(matriz, l, c):
    x = 0
    while x < len(matriz):
        if matriz[l][x] == 'Q' or matriz[x][c] == 'Q':
            return False
        x = x + 1

    #checando nordeste
    x = l
    y = c
    while x >= 0 and y < len(matriz):
        if matriz[x][y] == 'Q':
            return False
        x = x - 1
        y = y + 1    

    #checando sudoeste
    x = l
    y = c
    while x < len(matriz) and y >= 0:
        if matriz[x][y] == 'Q':
            return False
        x = x + 1
        y = y - 1    

    #checando sudeste
    x = l 
    y = c
    while x < len(matriz) and y < len(matriz):
        if matriz[x][y] == 'Q':
            return False
        x = x + 1
        y = y + 1

    #checando noroeste
    x = l 
    y = c
    while x >= 0 and y >= 0:
        if matriz[x][y] == 'Q':
            return False
        x = x - 1
        y = y - 1
    return True

    
#posiciona uma rainha na linha lin da matriz de forma
#que ela não sofra ataque de outra rainha. Esse pocionamento
#será a partir da coluna col da linha.
#A função retorna o índice da coluna onde a rainha posicionada ou
#-1 se não foi possível colocar a rainha.
def posicionaRainha(matriz, lin, col):
    tamanho = len(matriz)
    while col < tamanho:
        if possoColocarRainha(matriz, lin, col):
            matriz[lin][col] = 'Q'
            return col
        col = col + 1
    return -1

dim = 8
tab = criaMatriz(dim)
pos = 0
lin = 0
pilha = []
col = 0

while lin < dim:
    pos = posicionaRainha(tab, lin, col)
    if pos != -1:
        stack.put(pilha, [lin, pos])
        lin = lin + 1
        col = 0        
    else:
        #não consegui posicionar rainha na linha lin
        # volto para linha anterior, retiro a rainha 
        # da linha anterior, desempilho a pilha e
        # tento posicionar a rainha numa outra coluna
        lin = lin - 1
        coordenada = stack.pop(pilha)
        col = coordenada[1]
        tab[lin][col] = ' '
        col = col + 1        

print(pilha)
for lin in tab:
    print(lin)