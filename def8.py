def histograma(matriz):
    #([][] -> list)
    conta = [0] * 201

    for lin in matriz:
        for vl in lin:
            conta[vl] = conta[vl] + 1

    return conta

    