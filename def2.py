import random

def geraListaAleatoria(n):
    lista = []
    while n > 0:
        num = random.randint(1, 1001)
        lista.append(num)
        n = n - 1
        #lista.append(random.randint(1, 1001))
    return lista


listaRandomica = geraListaAleatoria(23)
print(listaRandomica)    

