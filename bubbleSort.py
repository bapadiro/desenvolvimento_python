def subir(lista):
    i = len(lista) - 1
    while i > 0:
        if lista[i-1] > lista[i]:
            aux = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = aux
        i = i - 1

def bubbleSort(vetor):
    for i in range(len(vetor)):
        subir(vetor)


vetor = [10, 15, 8, 19, 30, 12, 84, 5, 10, 17]
bubbleSort(vetor)
print(vetor)
