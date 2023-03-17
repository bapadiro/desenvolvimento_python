def insereOrdenado(x, lista):
    i = 0

    while i < len(lista) and lista[i] < x:
        i = i + 1    

    lista.insert(i, x)

v = [1, 5, 8, 12]
insereOrdenado(0, v)
print(v)
