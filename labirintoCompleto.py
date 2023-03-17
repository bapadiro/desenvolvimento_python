import queue

def criaLabirinto(dimLin, dimCol):
    matriz = []
    for i in range(dimLin):
        matriz.append([' '] * dimCol)

    matriz[0][2] = matriz[0][3] = '#'
    matriz[1][1] = matriz[1][4] = matriz[1][6] = matriz[1][8] = matriz[1][9] = '#'       
    matriz[2][2] = matriz[2][4] = matriz[2][6] = matriz[2][10] = '#'         
    matriz[3][1] = matriz[3][3] = matriz[3][7] = matriz[3][8] = '#'        
    matriz[4][3] = matriz[4][5] = matriz[4][9] = '#'
    matriz[5][1] = matriz[5][8] = '#'

    return matriz

def listaVizinhos(tab, pos, maxLin, maxCol):
    resp = []
    lin = pos[0]
    col = pos[1]
    #norte
    #se tem posicao valida e nessa posicao a
    #matriz esta livre:
    if lin - 1 >= 0 and tab[lin-1][col] == ' ':
        resp.append((lin-1, col))
    #leste
    if col + 1 < maxCol and tab[lin][col+1] == ' ':
        resp.append((lin, col+1))
    #sul
    if lin + 1 < maxLin and tab[lin+1][col] == ' ':
        resp.append((lin+1, col))
    #oeste
    if col - 1 >= 0 and tab[lin][col-1] == ' ':
        resp.append((lin, col-1))

    return resp        


mat = criaLabirinto(6, 11)
fila = []

queue.put(fila, (0,0))
mat[0][0] = (-1, -1)
acheiSaida = False
posSaida = (5, 10)

while not acheiSaida:
    elem = queue.get(fila)    
    if elem == posSaida:
        acheiSaida = True

    vizinhos = listaVizinhos(mat, elem, 6, 11)
    for viz in vizinhos:
        l = viz[0]
        c = viz[1]
        mat[l][c] = elem
        queue.put(fila, viz)

lin = 5
col = 10
print((5, 10))
while mat[lin][col] != (-1, -1):
    pos = mat[lin][col]
    print(pos)
    lin = pos[0]
    col = pos[1]
