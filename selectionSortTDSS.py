#encontra e retorna a posição do menor
#elemento da lista a partir da posição i
def menor(lista, i):
    posMenor = i
    while i < len(lista):
        if lista[i] < lista[posMenor]:
            posMenor = i
        i = i + 1

    return posMenor

def selectionSort(vetor):
    i = 0
    while i < len(vetor) - 1:
        m = menor(vetor, i)
        vetor[m], vetor[i] = vetor[i], vetor[m]
        #aux = vetor[m]
        #vetor[m] = vetor[i]
        #vetor[i] = aux
        i = i + 1

l = [4, 7, 0, -4, 6, 3, 8, 0]
selectionSort(l)
print(l)