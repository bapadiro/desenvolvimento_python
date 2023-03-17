def contagem(valor, conjunto):
    contador = 0
    for info in conjunto:
        if info == valor:
            contador = contador + 1

    return contador

letras = ['a', 'b', 'e', 'a', 'c', 'e', 'a', 'b', 'a']

contabilizada = []

for valor in letras:
    if not valor in contabilizada:
        qtd = contagem(valor, letras)
        print(valor,qtd,"vezes")
        contabilizada.append(valor)
