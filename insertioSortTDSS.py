def organiza(lista, pos):
    aux = lista[pos]
    while pos > 0 and lista[pos-1] > aux:
        lista[pos] = lista[pos-1]
        pos = pos - 1

    lista[pos] = aux    


def insertionSort(vetor):
    for i in range(1, len(vetor)):
        organiza(vetor, i)


l = [4, 7, 0, -4, 6, 3, 8, 0]
insertionSort(l)
print(l)