def buscaBinaria(matriz, x):
    lin = len(matriz)
    col = len(matriz[0])
    ini = 0
    fim = lin * col - 1
    while ini < fim:
        meio = (ini + fim) / 2
        l = meio / col
        c = meio % col
        if matriz[l][c] < x:
            ini = meio + 1
        elif matriz[l][c] > x:
            fim = meio - 1
        else:
            return [l, c]

    return [-1, -1]