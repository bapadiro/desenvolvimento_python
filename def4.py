def soma(matriz):
    #(list[][] => tuple)
    somaPos = 0
    somaNeg = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < 0:
                somaNeg = somaNeg + matriz[i][j]
            elif matriz[i][j] > 0:
                somaPos = somaPos + matriz[i][j]

    return (somaPos, somaNeg)

    

